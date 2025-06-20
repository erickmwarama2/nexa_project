
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from beanie import init_beanie, Document, before_event, Insert
from motor.motor_asyncio import AsyncIOMotorClient
from faker import Faker
from typing import Optional
from datetime import datetime
# from transformers import pipeline

class Question(Document):
    question: str
    created_at: Optional[datetime] = None

    @before_event(Insert)
    def set_created_at(self):
        self.created_at = datetime.now()

MONGO_URI = "mongodb://root:password@db:27017?authSource=admin"
# MONGO_URI = "mongodb://localhost:27017"

@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncIOMotorClient(MONGO_URI)
    await init_beanie(database=client.questions, document_models=[Question])
    print("Connected to the database")
    yield
    client.close()

app = FastAPI(lifespan=lifespan)
faker = Faker()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# pipeline = pipeline(task="text-generation", model="gpt2")


@app.post("/ask")
async def ask_question(payload: Question):
    # response = pipeline(payload.question)
    response = faker.text()
    await payload.insert()
    return {"response": response}

@app.get("/history")
async def get_questions():
    questions = await Question.find_all().to_list()
    print(questions)
    return {"response": questions}
