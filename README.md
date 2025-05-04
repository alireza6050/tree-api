# Tree API

A lightweight HTTP API to manage a tree data structure using FastAPI and SQLite.

## Features

- `GET /api/tree` – Retrieve the entire tree as a nested structure
- `POST /api/tree` – Add a new node to the tree under a parent
- SQLite for simple persistent storage
- Pytest unit tests included
- Easy local setup

---

## ▶️ Getting Started

### 1. Create a Python virtual environment

```bash
python3 -m venv env_treeapi
source env_treeapi/bin/activate
```

### 2. Install the dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the server locally

```bash
uvicorn app.main:app --reload
```

Once running, access:

- `http://localhost:8000/api/tree` – view current tree

---

## Run Tests

```bash
PYTHONPATH=. pytest
```

Tests are located in `tests/test_tree.py`.

---

## 🗂 Project Structure

```
tree-api/
├── app/
│   ├── main.py        # FastAPI app entry
│   ├── crud.py        # DB logic (add/get tree)
│   ├── db.py          # DB init
│   ├── database.py    # DB engine + Base
│   └── models.py      # SQLAlchemy model (Node)
├── tests/
│   └── test_tree.py   # Pytest cases
├── tree.db            # SQLite DB (auto-created)
├── requirements.txt
└── README.md
```

---

## 📮 API Reference

### `GET /api/tree`

Returns the full tree structure from the database.

**Example Response:**
```json
[
  {
    "id": 1,
    "label": "root",
    "children": [
      {
        "id": 2,
        "label": "child1",
        "children": []
      }
    ]
  }
]
```

---

### `POST /api/tree`

Creates a new node under a given parent.

**Request Body:**
```json
{
  "label": "new-node",
  "parentId": 1
}
```

**Response:**
```json
{
  "id": 3,
  "label": "new-node"
}
```

If `parentId` is omitted or `null`, the node will be added as a root.

---

## Notes

- The SQLite database (`tree.db`) is created on the fly in the project root.
- Data persists between runs unless manually deleted.
- To reset, delete the `tree.db` file.
