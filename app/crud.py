from sqlalchemy.orm import Session
from app.models import Node
from app.database import SessionLocal

def add_node(label: str, parent_id: int):
    session = SessionLocal()
    parent = session.get(Node, parent_id)
    if not parent:
        session.close()
        raise ValueError("Parent node not found")
    node = Node(label=label, parent_id=parent_id)
    session.add(node)
    session.commit()
    session.refresh(node)
    session.close()
    return {"id": node.id, "label": node.label}

def get_full_tree():
    session = SessionLocal()
    all_nodes = session.query(Node).all()
    node_map = {node.id: {"id": node.id, "label": node.label, "children": []} for node in all_nodes}
    roots = []
    for node in all_nodes:
        if node.parent_id:
            node_map[node.parent_id]["children"].append(node_map[node.id])
        else:
            roots.append(node_map[node.id])
    session.close()
    return roots