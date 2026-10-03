from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


#prompt
prompt=PromptTemplate(
    template="""
    You are an AI Tutor.
    Explain The Following topic to a student in a simple and beginner-friendly way:
    topic {topic}

    """,
    input_variables=["topic"]
)


#Model
model=ChatGroq(model="openai/gpt-oss-20b")

#Parser
parser=StrOutputParser()


#step-1 : invoke the prompt
prompt_value=prompt.invoke({"topic":"Machine Learning"})


#step-2 : Send the prompt to the model
model_output=model.invoke(prompt_value)


#Step-3 : Parse the model's response
final_output=parser.invoke(model_output)


print(final_output)