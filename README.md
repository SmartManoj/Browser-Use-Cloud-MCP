# Browser-Use Cloud MCP

A Model Context Protocol (MCP) server that provides access to Browser-Use Cloud API through a standardized interface.

## Overview

This project creates an MCP server that wraps the Browser-Use Cloud API, allowing AI assistants and other MCP clients to interact with browser automation services through a clean, standardized interface.

## Components

- **`server.py`** - Main MCP server implementation using FastMCP
- **`client.py`** - Example client for testing the MCP server
- **`modify_openapi.py`** - Script to fetch and modify the OpenAPI specification
- **`modified_openapi.json`** - Modified OpenAPI spec with clean tool names

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   Create a `.env` file with your Browser-Use Cloud API key:
   ```
   API_KEY=your_browser_use_api_key_here
   ```

## Usage

### Starting the MCP Server

```bash
python server.py
```

The server will start on `http://127.0.0.1:8000/mcp` by default.

### Testing with the Client

```bash
python client.py
```

This will connect to the server and list all available tools.

## API Integration

The server integrates with the Browser-Use Cloud API at `https://api.browser-use.com/api/v1` and provides:

- Bearer token authentication
- Clean tool names (removes `_api_v1_` prefixes)
- Standardized MCP interface

## Development

The `modify_openapi.py` script fetches the original OpenAPI specification from Browser-Use Cloud and modifies it to create cleaner tool names by removing the `_api_v1_` prefix from operation IDs.

## License

This project is open source and available under the MIT License.