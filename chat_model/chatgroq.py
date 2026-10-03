from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm=ChatGroq(model="openai/gpt-oss-20b")

result=llm.invoke("What is 2+2")

print(result.content)