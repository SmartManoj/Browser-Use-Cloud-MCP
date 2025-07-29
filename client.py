from fastmcp import Client
import asyncio

url = 'http://127.0.0.1:8000/mcp'

async def main():   
    async with Client(url) as client:
        result = await client.list_tools()
        for tool in result:
            print(tool.name)

if __name__ == "__main__":
    asyncio.run(main())
