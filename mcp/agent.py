import os
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.auth import AuthCredential, OAuth2Auth, AuthCredentialTypes

# The crucial import from the correct location, provided by your colleague.
from google.adk.tools.mcp_tool.mcp_session_manager \
    import StreamableHTTPServerParams


# The URL of your deployed Cloud Run MCP server.
MCP_SERVER_URL = ...


OAUTH_CLIENT_ID = os.getenv("MCP_OAUTH_CLIENT_ID", "YOUR_OAUTH_CLIENT_ID")
OAUTH_CLIENT_SECRET = os.getenv("MCP_OAUTH_CLIENT_SECRET", "YOUR_OAUTH_CLIENT_SECRET")
OAUTH_TOKEN_URL = os.getenv("MCP_OAUTH_TOKEN_URL", "YOUR_OAUTH_TOKEN_URL")



oauth_credentials = AuthCredential(
    auth_type=AuthCredentialTypes.OAUTH2,
    oauth2=OAuth2Auth(
        client_id=OAUTH_CLIENT_ID,
        client_secret=OAUTH_CLIENT_SECRET,
        token_url=OAUTH_TOKEN_URL
    )
)


tool = MCPToolset(
            connection_params=StreamableHTTPServerParams(
                #headers={
                #"Authorization": f"Bearer {id_token}",
                #"Content-Type": "application/json, text/event-stream",
                #"Accept": "application/json, text/event-stream",
            #},
                url=MCP_SERVER_URL,
                auth_credential=oauth_credentials
            ),
               errlog=None
        )

# Define the agent that will use the remote tools.
root_agent = Agent(
    model="gemini-2.5-flash",
    name="remote_calculator_agent",
    instruction=(
        "You are a helpful math assistant. "
        "You have access to a remote calculator with 'add' and 'subtract' functions. "
        "Use these tools to answer the user's questions."
    ),
    tools=[tool],
)
