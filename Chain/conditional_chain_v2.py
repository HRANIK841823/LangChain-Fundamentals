from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import  RunnableBranch


load_dotenv()

model=ChatGroq(model="openai/gpt-oss-20b")

parser=StrOutputParser()

#classify the review first
classifier_prompt=PromptTemplate(
    template="""
    You are a movie review classifier:
    classify the following review as either:
    -positive
    -negative
    Return only one word : positive or negative
    Review : {review}
    """,
    input_variables=["review"]
)

classifier_chain=classifier_prompt | model | parser



# step 2 : Positive Prompt
positive_prompt=PromptTemplate(
    template="""
    Reply to this positive movie review in a friendly way : \n {review}
    Review : {review}
    """,
    input_variables=["review"]
)
#Step -3 : Negative Prompt
negative_prompt=PromptTemplate(
    template="""
    reply to this negative movie review by aplogizing and offering help: \n {review}
    Review : {review}
    """,
    input_variables=["review"]
)

    

positive_chain= positive_prompt | model | parser

negative_chain= negative_prompt | model | parser


#Review
# review="The movie was abosolutely Fantastic,I Love every minute of it."
review="The movie war terrible to watch"


#Conditional Chain
sentiment=classifier_chain.invoke({'review':review})

print(sentiment)
conditional_chain=RunnableBranch(
    (
        lambda x:x['sentiment'].strip().lower()=='positive' ,positive_chain
    ),
    negative_chain
)

result=conditional_chain.invoke({"review":review,"sentiment":sentiment})

print(result)