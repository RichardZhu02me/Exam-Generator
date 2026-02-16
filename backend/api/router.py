from fastapi import APIRouter
from agents import exam_agent
from schemas.prompt import Prompt
from thirdparty.pinecone_client import pc

router = APIRouter(prefix="/api")


@router.get("/")
def root():
    return {"message": "Hello World"}


@router.post("/generate-exam")
def generate_exam(prompt: Prompt):
    try:
        exam_agent.invoke(prompt)
    except Exception as e:
        return {e}

    return {"message": "Exam generated successfully"}


@router.get("/db/indexes")
def get_indexes():
    return [index.to_dict() for index in pc.list_indexes()]
