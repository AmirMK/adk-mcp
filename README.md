# 🧠 Custom ADK Agent with MCP for Vertex AI Agent Engine

This sample demonstrates how to build and deploy a **custom agent** using the [Agent Development Kit (ADK)] with an **MCP ** backend. The agent can be:

- Used as an **independent API** to integrate into custom applications, or  
- Registered in **Agentspace** to provide a unified user interface and interaction experience.


---

## 🛠️ Prerequisites

- A working **MCP server** accessible via URL.  
  If you don't have one, follow the instructions in this [MCP setup guide](https://cloud.google.com/run/docs/tutorials/deploy-remote-mcp-server).
- A Google Cloud project with Vertex AI and Agent Engine APIs enabled.
- A GCS bucket for staging deployment artifacts.

---

## 📦 Setup Instructions

### 1. Install Dependencies

```bash
pip install google-adk[adk,agent_engine]
```
### 2. Configure Environment

In `./mcp/.env`, insert your **Google Cloud Project ID**:

```env
GOOGLE_CLOUD_PROJECT="your-project-id"
```

### 3. Connect MCP Server

In `./mcp/agent.py`, update the MCP server URL:

```python
MCP_SERVER_URL = "https://your-mcp-server-url"
```

### 4. Run the Agent Locally

Use the following command to start the agent locally:

```bash
adk web
```
This launches the agent on http://localhost:8000 for local testing.

### 5. Deploy to Vertex AI Agent Engine

Edit `deploy.py` and set the following variables:

```python
project_id = "your-project-id"
location = "us-central1"  # or your preferred region
staging_bucket = "gs://your-gcs-bucket"
```

Then deploy using:

```bash
python deploy.py
```

### 📡 Call Agent via API

Here is an example to invoke your deployed agent using Python:

```python
from vertexai import agent_engines

project_id = "your-project-id"
location = "your-region"
agent_engine_id = "your-agent-id"
user = "your-username"

# Get deployed agent
adk_app = agent_engines.get(
    f"projects/{project_id}/locations/{location}/reasoningEngines/{agent_engine_id}"
)

# Create a new session
session = adk_app.create_session(user_id=user)
session_id = adk_app.list_sessions(user_id=user)['sessions'][0]['id']

# Send a message
message = "What is the result of 67 - 23?"
for event in adk_app.stream_query(user_id=user, session_id=session_id, message=message):
    print(event)

# Print final response
print('----')
print(event['content']['parts'][0]['text'])
```

This will deploy the agent to Vertex AI Agent Engine and return a REASONING_ENGINE_ID needed to query your agent.


### 🧩 Optional: Integrate with Agentspace

You can register this agent in **Agentspace** to make it accessible through the Agentspace UI, enabling a seamless multi-agent experience for end users.
