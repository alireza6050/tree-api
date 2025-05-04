# Defines the Node model representing tree nodes with parent-child relationships
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

# SQLAlchemy model for a node in the tree structure
class Node(Base):
    __tablename__ = "nodes"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String, nullable=False)
    parent_id = Column(Integer, ForeignKey("nodes.id"), nullable=True)
    