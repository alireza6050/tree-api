from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Node(Base):
    __tablename__ = "nodes"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String, nullable=False)
    parent_id = Column(Integer, ForeignKey("nodes.id"), nullable=True)

    children = relationship("Node", back_populates="parent", cascade="all, delete")
    parent = relationship("Node", back_populates="children", remote_side=[id])