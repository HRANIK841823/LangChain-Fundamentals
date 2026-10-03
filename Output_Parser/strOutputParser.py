from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

#load env
load_dotenv()

#Model
model=ChatGroq(model="openai/gpt-oss-20b")


#prompt
prompt=PromptTemplate.from_template(
    "Explain {topic} in simple terms"
)


#Parser
parser=StrOutputParser()

#chain
chain=prompt | model | parser

result=chain.invoke({
    "topic":"Machine Learning"
})


# print(result)

print(type(result))