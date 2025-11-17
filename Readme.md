# Talent x AI

**An Interactive AI-Driven Career Exploration & Voice Assistant Platform**  

**Talent x AI** is an immersive platform that empowers users to explore career paths, simulate day-to-day experiences, interact with AI-powered agents, and manage personal portfolios. With voice-enabled AI, 3D avatars, and real-time chat agents, SparkPath OS provides a unique, hands-on way to discover and shape your career journey.  

---

## Features

- **Avatar Selector:** Choose from multiple 3D avatars to represent yourself.  
- **Voice Career Copilot:** Converse with AI agents using text or voice input.  
- **Day-in-the-Life Simulation:** Simulate real-world career scenarios.  
- **Spark Hub:** Personalized space to explore tools, resources, and projects.  
- **Portfolio Management:** Save conversation history, generated content, and HTML portfolios to AWS S3.  
- **Audio Interaction:** Record and play back audio conversations with AI agents.  

---

## Tech Stack

- **Frontend:** Streamlit, HTML/CSS, 3D model viewer  
- **Backend:** Python, AWS Bedrock, Amazon Polly, Amazon Transcribe, DynamoDB, S3  
- **Voice Processing:** Streamlit Mic Recorder, PyDub, Wave  
- **Other Libraries:** Pandas, NumPy, SciPy, BeautifulSoup4, Requests  

---
# TalentX AI

**An Interactive AI-Driven Career Exploration & Voice Assistant Platform**  

**TalentX AI** is an immersive platform that empowers users to explore career paths, simulate day-to-day experiences, interact with AI-powered agents, and manage personal portfolios. With voice-enabled AI, 3D avatars, and multi-agent chat functionality, TalentX AI provides a hands-on way to discover and shape your career journey.

---

## Features

- **Avatar Selector:** Choose from multiple 3D avatars to represent yourself.  
- **Voice & Text Career Copilot:** Converse with AI agents using text or voice input in the Multi-Agent Chatbot.  
- **Day-in-the-Life Simulation:** Simulate real-world career scenarios.  
- **Spark Hub:** Personalized space to explore tools, resources, and projects.  
- **Portfolio Management:** Save conversation history, generated content, and HTML portfolios to AWS S3.  
- **Audio Interaction:** Record and play back audio conversations with AI agents.  

---

## Architecture

![TalentX AI Architecture]([path_to_your_architecture_image.png](https://www.canva.com/design/DAG4-0eLrb8/XXjRdnT-jVfMJr1_I7esgg/view?utm_content=DAG4-0eLrb8&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hba620a572b))  

---

## Tech Stack

| Layer                  | Technology / Tools                                                |
|------------------------|------------------------------------------------------------------|
| **Frontend**           | Streamlit, HTML/CSS, 3D model viewer                             |
| **Backend**            | Python, AWS Bedrock, Amazon Polly, Amazon Transcribe             |
| **Agents**             | Multi-Agent Architecture: Master Agent + Sub-Agents             |
| **Database & Storage** | DynamoDB (Chat History & State), S3 (Portfolios + Voice Logs)   |
| **Voice Processing**   | Streamlit Mic Recorder, PyDub, Wave                               |
| **Other Libraries**    | Pandas, NumPy, SciPy, BeautifulSoup4, Requests                   |

---

## Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/talentx-ai.git
cd talentx-ai
Install dependencies:

bash
Copy code
pip install -r requirements.txt
AWS Setup:

S3: Create a bucket to store portfolio files and voice logs.

DynamoDB: Create a table to store chat history and agent states.

AWS Bedrock: Configure your Master and Sub-Agents using Bedrock.

Environment Variables:

Create a .env file with the following:

bash
Copy code
AWS_ACCESS_KEY_ID=<your-access-key>
AWS_SECRET_ACCESS_KEY=<your-secret-key>
AWS_REGION=<your-region>
S3_BUCKET=<your-s3-bucket-name>
DYNAMO_TABLE=<your-dynamodb-table-name>
Run the app:

bash
Copy code
streamlit run app.py
How It Works
Navigation Tabs:

Home: Choose an avatar.

Day-in-the-Life Simulation: Explore career simulations.

Spark Hub: Explore identity, strengths, and confidence labs.

Multi-Agent Chatbot: Interact with agents via text or voice.

Multi-Agent Chatbot:

Text Input: Users type queries to the Master Agent.

Voice Input: Users speak; Amazon Transcribe converts speech to text, sent to Master Agent.

Master Agent: Routes requests to sub-agents (Profile, Skill Mapping, Career Pathway, Portfolio).

Sub-Agents: Process data and update DynamoDB/S3 as needed.

Note: Users of this repo need to create their own Master and Sub-Agents on AWS Bedrock to fully replicate the Multi-Agent system.

