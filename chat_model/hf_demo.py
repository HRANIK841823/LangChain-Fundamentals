from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="conversational",
    max_new_tokens=100

)

chat_model = ChatHuggingFace(llm=llm)

result = chat_model.invoke(
    "What is the capital of Bangladesh?"
)

print(result.content)