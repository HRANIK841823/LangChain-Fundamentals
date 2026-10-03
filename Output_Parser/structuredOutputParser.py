from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import (StructuredOutputParser,ResponseSchema)

#.env
load_dotenv()

#Model
model=ChatGroq(model="openai/gpt-oss-20b")

#Define the schema
response_schema=[
    ResponseSchema(
        name="Fact_1",
        description="The first fact about the topic"
    ),
    ResponseSchema(
            name="Fact_2",
            description="The second fact about the topic"
        ),
    ResponseSchema(
                name="Fact_3",
                description="The third fact about the topic"
            ),
    ResponseSchema(
            name="Fact_4",
            description="The forth fact about the topic"
        ),
    ResponseSchema(
            name="Fact_5",
            description="The five fact about the topic"
        ),
]


#Define Parser
parser=StructuredOutputParser.from_response_schemas(response_schema)

#Create the prompt
template=PromptTemplate(
    template="""
    Give me 5 Facts about {topic}.
    {format_instruction}
""",
    input_variables=["topic"],
    partial_variables={"format_instruction":parser.get_format_instructions()}
)

#create the chain
chain=template | model | parser

result=chain.invoke({
    "topic":"ML"
})

print(result)


print(result['Fact_2'])


# All ok but no validation at all so we need pydantic for validation man