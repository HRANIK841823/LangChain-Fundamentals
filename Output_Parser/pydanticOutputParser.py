from langchain_groq import ChatGroq
from langchain_classic.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv


from pydantic import BaseModel,Field

#.env
load_dotenv()

#Model
model=ChatGroq(model="openai/gpt-oss-20b")

#Define the schema
class ModelEvaluation(BaseModel):
    model_name: str=Field(description="Name of the Machine learning Model")

    accuracy: float=Field(gt=0,lt=1,description="Accuracy of the Model, greather than 0 and less than 1")

    dataset: str=Field(description="Name of the dataset used for evaluation")


#Parser
parser=PydanticOutputParser(pydantic_object=ModelEvaluation)


#prompt
template=PromptTemplate(
    template="""
     Generate the name,accuracy and dataset of a fictional machine learning model trained for {task} {format_instruction}

""",
input_variables=["task"],
partial_variables={"format_instruction":parser.get_format_instructions()}
)


#chain
chain= template | model | parser

result=chain.invoke({
    "task":"image_classification"
})

print(result)

print(result.model_name)
print(result.accuracy)
print(result.dataset)


