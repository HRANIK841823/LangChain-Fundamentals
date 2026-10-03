from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

#.env
load_dotenv()

#Model
model=ChatGroq(model="openai/gpt-oss-20b")


#Define Parser
parser=JsonOutputParser()

#Prompt
template=PromptTemplate(
    template="""
    Give me 5 Facts about {topic}.
    {format_instruction}
""",
    input_variables=["topic"],
    partial_variables={"format_instruction":parser.get_format_instructions()}
)

#Prompt Ogrinal Look
# prompt=template.format(topic="Machine Learning")

# print(prompt)


#Chain define
chain= template | model | parser

result=chain.invoke({
    "topic":"Machine Learning"
})
print(result)