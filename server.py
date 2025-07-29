import json
import httpx
import os

from fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('BROWSER_USE_API_KEY')

BASE_URL = 'https://api.browser-use.com/api/v1'

# Bearer token authentication
api_client = httpx.AsyncClient(
    base_url=BASE_URL,
    headers={"Authorization": f"Bearer {API_KEY}"}
)

# Create MCP server with route mapping function
mcp = FastMCP.from_openapi(
    openapi_spec=json.load(open('modified_openapi.json')), 
    client=api_client,
)

if __name__ == "__main__":
    if os.getenv('PREFER_SHTTP') or 1:
        mcp.run("streamable-http")
    else:
        mcp.run()