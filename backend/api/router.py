from fastapi import APIRouter, HTTPException
from agents import exam_agent
from schemas.prompt import Prompt
from thirdparty.pinecone_client import pc

router = APIRouter(prefix="/api")


@router.get("/")
def root() -> dict:
    return {"message": "Exam Generator API is running"}


@router.post("/generate-exam")
def generate_exam(prompt: Prompt) -> dict:
    try:
        exam_agent.invoke(prompt)
        return {"message": "Exam generated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/db/indexes")
def get_indexes():
    return [index.to_dict() for index in pc.list_indexes()]
