from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app import db, crud

db.init_db()
app = FastAPI()

class NodeCreate(BaseModel):
    label: str
    parentId: int

@app.get("/api/tree")
def get_tree():
    return crud.get_full_tree()

@app.post("/api/tree")
def create_node(node: NodeCreate):
    try:
        return crud.add_node(node.label, node.parentId)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))