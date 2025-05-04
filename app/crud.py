from sqlalchemy.orm import Session
from app.models import Node
from app.database import SessionLocal

# Adds a new node under the specified parent ID
def add_node(label: str, parent_id: int):
    session = SessionLocal()

    # Check if the parent exists
    if parent_id is not None:
        parent = session.get(Node, parent_id)
        if not parent:
            session.close()
            raise ValueError("Parent node not found")

    # Create the new node and attach it
    node = Node(label=label, parent_id=parent_id)
    session.add(node)
    session.commit()
    session.refresh(node)
    session.close()

    return {"id": node.id, "label": node.label}

# Builds the full tree recursively from all nodes in the DB
def get_full_tree():
    session = SessionLocal()
    all_nodes = session.query(Node).all()

    # Map node IDs to tree node structures
    node_map = {
        node.id: {"id": node.id, "label": node.label, "children": []}
        for node in all_nodes
    }

    roots = []
    for node in all_nodes:
        if node.parent_id:
            node_map[node.parent_id]["children"].append(node_map[node.id])
        else:
            roots.append(node_map[node.id])

    session.close()
    return roots