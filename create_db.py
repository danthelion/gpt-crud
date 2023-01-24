import sqlite3

conn = sqlite3.connect("todos.db")
c = conn.cursor()
c.execute(
    """
    CREATE TABLE todos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        done INTEGER NOT NULL
    )
    """
)
c.execute(
    """
    INSERT INTO todos (name, done) VALUES
    ('Buy milk', 0),
    ('Buy eggs', 0),
    ('Buy bread', 0),
    ('Buy cheese', 0),
    ('Buy butter', 0);
    """
)
conn.commit()
conn.close()
