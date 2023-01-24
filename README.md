# TODO app powered by GPT-3

This is a simple TODO app powered by GPT-3.

## How to use

1. Create the initial database

```python
python create_db.py
```

2. Start the server

```python
python main.py
```

3. Start sending requests to the server

Request:

```shell
curl -X POST -H "Content-Type: application/json" -d '{"command": "I need to buy bread"}' http://localhost:8000/todo | jq
```

Response:

```json
{
  "message": "The task has been added to your TODO list."
}
```

Request:
```shell
curl -X POST -H "Content-Type: application/json" -d '{"command": "Get all todos"}' http://localhost:8000/todo | jq
```

Response:
```json
[
    {
    "id": 4,
    "name": "Buy cheese",
    "done": 0
  },
...
  {
    "id": 13,
    "name": "buy bread",
    "done": 0
  }
]
```

Request:

```shell
curl -X POST -H "Content-Type: application/json" -d '{"command": "Mark buy bread item as done"}' http://localhost:8000/todo | jq
```

Response:

```json
{
  "message": "The item 'buy bread' has been marked as done."
}
```
