from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq



load_dotenv()


prompt1=PromptTemplate(
    template="""
    Evaluate the following Student's Answer.
    Question: {question}
    Student's Answer": {answer}

    Provide a detailed evaluation including:
    -correctness
    -strengths
    -weakness
    -suggestions for improvement

    """,
    input_variables=["question","answer"]
)

prompt2=PromptTemplate(
    template="""
    Convert the following detailed Evaluation into a concise 5-point feedback:
    {evluation}

    """,
    input_variables=["evaluation"]
)


#Model
model=ChatGroq(model="openai/gpt-oss-20b")


parser=StrOutputParser()



#Chain
chain=prompt1 | model | parser | prompt2 | model | parser



result=chain.invoke({
    "question":"What is Machine Learning?",
    "answer":" is a subset of Artificial Intelligence that teaches computers to learn from data and make predictions without being explicitly programmed for every single task."
})

print(result)

chain.get_graph().print_ascii()