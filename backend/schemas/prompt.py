from pydantic import BaseModel


class Prompt(BaseModel):
    prompt: str
    index_name: str
    namespace: str
