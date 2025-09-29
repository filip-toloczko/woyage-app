from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from openai import AsyncOpenAI
from typing import Optional, List
import os
from dotenv import load_dotenv

#loading in my openAI api key
load_dotenv()

#initialize clients
app = FastAPI(title="Interview Followup Generator")
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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

#endpoint
@app.post("/interview/generate-followups", response_model=Response)
async def generate_followups(request: Request):
    try:
        #creating the system message
        chatGPT_prompt = """You are an interviewer. Your job is to generate one or more concise, relevant follow up questions with brief rationals.
        Make sure to look into gaps or interesting points in their response. Make sure to be precise and specific. Ask questions that will 
        help to demonstrate the candidates skills and previous experience. Sound natural and conversational, as a human interviewer would.
        Make sure to only return the followup question, nothing else."""

        #creating the user's message to chatgpt
        user_message = f"Original Question: {request.question}.\nCandidate's Answer: {request.answer}"
        if request.role:
            user_message += f"\nRole being interviewed for: {request.role}"
        if request.interview_type:
            user_message += f"\nInterview Type: {request.role}"
        user_message += "\nGenerate one follow up question"

        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": chatGPT_prompt},
                {"role": "user", "content": user_message}
            ]
            max_tokens=250
        )

        followup_question = response.choices[0].message.content.strip()

        return Response(
            result="success",
            message="Follow-up question generated",
            data={"followup_question":followup_question}
        )

        


