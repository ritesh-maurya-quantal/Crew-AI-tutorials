from dotenv import load_dotenv
load_dotenv()

from crewai import LLM

llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.1
)

print(llm.call("Hey my name is ritesh"))