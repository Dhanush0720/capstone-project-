from google import genai
from google.genai.agent import Agent, Task, Session
from tools.market_search import market_search_tool
from tools.skill_matcher import skill_matcher_tool

session = Session()

profile_agent = Agent(
    name="profile_analyzer",
    instructions="Extract skills, interests, goals from user input as JSON."
)

job_agent = Agent(
    name="job_market_agent",
    instructions="Use tool to fetch job trends.",
    tools=[market_search_tool],
)

matching_agent = Agent(
    name="career_matcher_agent",
    instructions="Match skills with job roles and return ranked list.",
    tools=[skill_matcher_tool],
)

explainer_agent = Agent(
    name="explainer_agent",
    instructions="Generate final recommendation report."
)

def run_system(user_input):
    profile = profile_agent.run(user_input)
    session.save("profile", profile)

    market = job_agent.run(profile)
    session.save("market", market)

    matches = matching_agent.run({"profile": profile, "market": market})

    final = explainer_agent.run(matches)
    return final

if __name__ == '__main__':
    user_input = input("Enter your skills and interests: ")
    print(run_system(user_input))
