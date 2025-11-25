from google.genai.tools import Tool

def market_search(query):
    return f'Searching job trends for: {query}'

market_search_tool = Tool(
    name='market_search',
    description='Job market search tool.',
    func=market_search
)
