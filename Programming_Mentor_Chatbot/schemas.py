from typing import List
from pydantic import BaseModel, Field


class ProgrammingResponse(BaseModel):
    """
    Final structured response returned by CodeMentor AI.
    """

    category: str = Field(
        description="The category of the programming question."
    )

    language: str = Field(
        description="Programming language or technology involved."
    )

    answer: str = Field(
        description="Direct answer or solution to the user's question."
    )

    explanation: str = Field(
        description="Detailed but beginner-friendly explanation."
    )

    difficulty: str = Field(
        description="Difficulty level: Beginner, Intermediate, or Advanced."
    )

    time_complexity: str = Field(
        description="Time complexity when applicable. Otherwise N/A."
    )

    space_complexity: str = Field(
        description="Space complexity when applicable. Otherwise N/A."
    )

    concepts: List[str] = Field(
        description="Important programming concepts involved."
    )

    follow_up_question: str = Field(
        description="A useful question the user can ask next."
    )

    confidence: float = Field(
        ge=0,
        le=1,
        description="Confidence score between 0 and 1."
    )