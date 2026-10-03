from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import  RunnableBranch


load_dotenv()

model=ChatGroq(model="openai/gpt-oss-20b")

parser=StrOutputParser()


positive_prompt=ChatPromptTemplate.from_template(
    "Review to this positive movie review in a friendly way: \n {review}"

)

negative_prompt=ChatPromptTemplate.from_template(
    "reply to this negative movie review by aplogizing and offering help: \n {review}"
)

positive_chain= positive_prompt | model | parser

negative_chain= negative_prompt | model | parser


conditional_chain=RunnableBranch(
    (
        lambda x: "good" in x["review"].lower(),positive_chain
    ),
    negative_chain
)

result1=conditional_chain.invoke({"review":"The movie was really good and i enjoyed every moment"})


result2=conditional_chain.invoke({"review":"The movie was boring and too long"})


print(result1)

print(result2)
