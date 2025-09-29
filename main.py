from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from openai import OpenAI
from typing import Optional, List
import os
from dotenv import load_dotenv

#loading in my openAI api key
load_dotenv()

#initialize clients
app = FastAPI(title="Interview Followup Generator")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#request and response models
class Request(BaseModel):
    question: str = Field(..., min_length=1, max_length=1000, description="the interviewer’s original question.")
    answer: str = Field(..., min_length=1, max_length=2000, description="the candidates response.")
    role: Optional[str] = Field(None, description="target role/title for context.")
    interview_type: Optional[List[str]] = Field(None, description="interview type for context.")

class Response(BaseModel):
    result: str
    message: str
    data: dict