from googlesearch import search as google_search
import json
from typing import Any, Dict, List
from mcp.server.fastmcp import FastMCP
import json

# Initialize the FastMCP server
mcp = FastMCP("Google Search")

@mcp.tool()
def search(query: str, max_results: int = 5) -> str:
    """Search the web using Google.
    
    Args:
        query: The search query
        max_results: Maximum number of results to return (default: 5)
    
    Returns:
        JSON containing title , url , description
    """
    try:
        results = list(google_search(query, num_results=max_results, lang='en', advanced=True))

        # Collect the search results
        res: List[Dict[str, str]] = []
        for result in results:
            res.append(
                {
                    "title": result.title,
                    "url": result.url,
                    "description": result.description,
                }
            )

        return json.dumps(res, indent=2)

    except Exception as e:
        print(e)
        return f"Error performing search: {str(e)}"

def run_server():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    # Run the server using stdio transport
    run_server()
