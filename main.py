from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from openai import OpenAI
from typing import Optional
import os
from dotenv import load_dotenv


load_dotenv()

app = FastAPI(title="AI Powered Interview Assistant")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

