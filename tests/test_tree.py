import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from app.main import app
from app.db import init_db
from app.database import SessionLocal
from app.models import Node

client = TestClient(app)

def setup_module(module):
    import os
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "tree.db"))
    if os.path.exists(db_path):
        os.remove(db_path)
    from app.db import init_db
    init_db()

def test_create_root_and_child():
    session = SessionLocal()
    root_node = Node(label="root", parent_id=None)
    session.add(root_node)
    session.commit()
    session.refresh(root_node)

    response = client.post("/api/tree", json={"label": "bear", "parentId": root_node.id})
    assert response.status_code == 200
    assert response.json()["label"] == "bear"
    session.close()

def test_get_tree():
    response = client.get("/api/tree")
    tree = response.json()
    assert response.status_code == 200
    assert isinstance(tree, list)
    assert tree[0]["label"] == "root"
    assert tree[0]["children"][0]["label"] == "bear"
