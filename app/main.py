from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app import db, crud
from typing import Optional

# Initialize the database schema (if not already created)
db.init_db()

# Create the FastAPI app instance
app = FastAPI()

# Request model for POST /api/tree
class NodeCreate(BaseModel):
    label: str
    parentId: Optional[int] = None

@app.get("/api/tree")
def get_tree():
    """
    Returns the entire tree structure as a nested JSON.
    """
    return crud.get_full_tree()

@app.post("/api/tree")
def create_node(node: NodeCreate):
    """
    Creates a new node and attaches it to the specified parent.
    """
    try:
        return crud.add_node(node.label, node.parentId)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))