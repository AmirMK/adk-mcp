import os
import vertexai
from dotenv import load_dotenv
from simple_mcp import root_agent
from vertexai import agent_engines

# Load environment variables from .env file
load_dotenv()

PROJECT_ID = ....
LOCATION = "us-central1"
STAGING_BUCKET = ...

if not all([PROJECT_ID, LOCATION, STAGING_BUCKET]):
    raise ValueError(
        "Please set GOOGLE_CLOUD_PROJECT, GOOGLE_CLOUD_LOCATION, and STAGING_BUCKET environment variables."
    )

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    staging_bucket=STAGING_BUCKET,
)

# Add python-dotenv to requirements for loading the .env file
REQUIREMENTS = ["google-cloud-aiplatform[adk,agent_engines]", "python-dotenv", "requests"]

print("Creating Reasoning Engine...")
remote_app = agent_engines.create(
    agent_engine=root_agent,
    display_name='math_assistant',
    description="Agent calculator with 'add' and 'subtract' functions",
    requirements=REQUIREMENTS,
    extra_packages=['simple_mcp']
)

print(f"Reasoning Engine created: {remote_app.resource_name}")
print(f"You can now update your .env file with REASONING_ENGINE_ID={remote_app.name}")
