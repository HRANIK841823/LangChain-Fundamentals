from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Use ChatGoogleGenerativeAI with a currently supported model string
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
result = llm.invoke("What is the Capital of Bangladesh")

print(result.content)
