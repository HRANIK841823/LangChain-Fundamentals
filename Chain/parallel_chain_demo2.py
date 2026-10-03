from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


#dot env
load_dotenv()


#Model
model=ChatGroq(model="openai/gpt-oss-20b")

#Parser
parser=StrOutputParser()


prompt1=PromptTemplate(
    template="Generate short and simple notes from the following text  \n {text}",
    input_variables=["text"]
)


prompt2=PromptTemplate(
    template="Generate 5 short question from the following text \n {text}",
    input_variables=["text"]
)

prompt3=PromptTemplate(
    template="Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}",
    input_variables=["notes","quiz"]
)


#Parallel Chain 
parallel_chain=RunnableParallel(
    {
        "notes": prompt1 | model | parser,
        "quiz": prompt2 | model | parser
    }
)

#new chain
chain = parallel_chain | prompt3 | model | parser


text="""

Deep learning is a subset of machine learning that uses multi-layered artificial neural networks to mimic the human brain and automatically learn complex patterns from vast amounts of data.
How It Works
• Neural Networks: Built using an input layer, multiple hidden layers, and an output layer made of interconnected nodes (neurons).
• Layered Processing: Early layers find simple features like lines and edges, while deeper layers combine them to recognize complex shapes and full objects.
• Automatic Learning: It extracts features on its own without needing humans to manually program what to look for


"""



result=chain.invoke({"text":text})


# print("Summary:\n:",result["Summary"])
# print("Question:\n:",result["Question"])

print(result)

chain.get_graph().print_ascii()