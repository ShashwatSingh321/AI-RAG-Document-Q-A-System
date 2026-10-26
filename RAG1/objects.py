from pydantic import BaseModel, Field

class Answer(BaseModel):
    answer: str = Field(description="The answer that is needed for the user question")
    context: str = Field(description="This is the context that the agent to reply to the user question.")