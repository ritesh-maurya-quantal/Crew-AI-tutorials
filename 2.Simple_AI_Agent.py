from dotenv import load_dotenv
load_dotenv()

from crewai import LLM

llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.1
)

from crewai import Agent, Task, Crew

email_assistant = Agent(
    role="Email Assistant",
    goal="Make the email more profesional and concise",
    backstory ="You are an email assistant that helps users improv thier emails to make it sound more professional and well structured.",
    llm = llm
)

input = "hello, my name is ritesh. i am writing to you about a meeting we had last week. i think it was good but we need to discuss some points again. please let me know when you are free to talk."

email_task = Task(
    description=f"Improve the following email to make it more professional and concise: {input}",
    agent =email_assistant,
    expected_output="A professionally written email with proper formatting, no grammatical errors, and a concise structure."
)

crew = Crew(
    agents=[email_assistant],
    tasks=[email_task],
    verbose=True
)

result = crew.kickoff()
print(result)