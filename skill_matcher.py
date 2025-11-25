from google.genai.tools import Tool

def skill_matcher(data):
    return {'matches': ['Data Scientist', 'ML Engineer', 'AI Analyst']}

skill_matcher_tool = Tool(
    name='skill_matcher',
    description='Matches skills with roles.',
    func=skill_matcher
)
