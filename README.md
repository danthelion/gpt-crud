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

```shell
curl -X POST -H "Content-Type: application/json" -d '{"command": "I need to buy milk"}' http://localhost:5000/todo
```

