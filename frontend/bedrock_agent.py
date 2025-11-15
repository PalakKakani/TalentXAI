
import boto3
import json
import time

# -----------------------------------------
# AWS CONFIG (YOUR VALUES)
# -----------------------------------------

AGENT_ID = "<YOUR_AGENT_ID>"
ALIAS_ID = "<YOUR_AGENT_ALIAS_ID>"
REGION = "<YOUR_AWS_REGION>"
PORTFOLIO_BUCKET = "<YOUR_BUCKET_NAME>"
HISTORY_TABLE = "<YOUR_DYNAMODB_HISTORY_TABLE>"
PROFILE_TABLE = "<YOUR_DYNAMODB_PROFILE_TABLE>"

# -----------------------------------------
# AWS CLIENTS
# -----------------------------------------
bedrock = boto3.client("bedrock-agent-runtime", region_name=REGION)
polly = boto3.client("polly", region_name=REGION)
s3 = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")

# -----------------------------------------
# CALL MASTER AGENT (Orchestrator)
# -----------------------------------------
def call_master_agent(user_input: str, user_id: str):
    response = bedrock.invoke_agent(
        agentId=AGENT_ID,
        agentAliasId=ALIAS_ID,
        sessionId=user_id,
        inputText=user_input
    )

    output = ""
    for event in response["completion"]:
        if "chunk" in event:
            output += event["chunk"]["bytes"].decode()

    save_chat_history(user_id, "user", user_input)
    save_chat_history(user_id, "agent_raw", output)

    return output

# -----------------------------------------
# SAVE CHAT HISTORY
# -----------------------------------------
def save_chat_history(user_id, role, text):
    table = dynamodb.Table(HISTORY_TABLE)
    table.put_item(
        Item={
            "user_id": user_id,
            "timestamp": str(time.time()),
            "role": role,
            "text": text
        }
    )

# -----------------------------------------
# SAVE PORTFOLIO TO S3
# -----------------------------------------
def save_portfolio_to_s3(html_content, user_id):
    key = f"{user_id}/portfolio.html"
    s3.put_object(
        Bucket=PORTFOLIO_BUCKET,
        Key=key,
        Body=html_content,
        ContentType="text/html"
    )
    return f"https://{PORTFOLIO_BUCKET}.s3.amazonaws.com/{key}"

# -----------------------------------------
# TEXT-TO-SPEECH
# -----------------------------------------
def synthesize_voice(text):
    result = polly.synthesize_speech(
        Text=text,
        VoiceId="Joanna",
        OutputFormat="mp3"
    )
    return result["AudioStream"].read()
