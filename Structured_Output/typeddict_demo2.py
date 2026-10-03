from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict, Annotated, List,Literal,Optional,NotRequired
from langchain_core.prompts import load_prompt

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

class ResumeAnalysis(TypedDict):
    candidate_name: Annotated[
        str,
        "Extract the full name of the candidate from the resume"
    ]

    job_title: Annotated[
        str,
        "Identify the candidate's current or most relevant job title"
    ]

    experience: Annotated[
        Literal["Entry_Level","Mid_Level","Senior_Level"],
        "Classify The candidate Exprience Level"
    ]

    skills: Annotated[
        Optional[List[str]],
        "Extract the main technical and professional skills from the resume"
    ]

    education: Annotated[
        str | None,
        "Extract the candidate's highest educational qualification"
    ]

    certifications: Annotated[
        List[str],
        "Extract professional certifications mentioned in the resume"
    ]

    projects: Annotated[
        List[str],
        "Extract important projects mentioned in the resume"
    ]

    strengths: Annotated[
        List[str],
        "Identify the candidate's main professional strengths"
    ]

    areas_to_improve: Annotated[
        List[str],
        "Identify areas where the candidate may need improvement"
    ]

structured_model = model.with_structured_output(
    ResumeAnalysis
)

cv = load_prompt("cv.json")



result = structured_model.invoke(cv.format())

for key, value in result.items():
    print(f"{key}: {value}")