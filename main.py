import json

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from langchain import OpenAI, PromptTemplate, SQLDatabaseChain, SQLDatabase
from pydantic import BaseModel

load_dotenv()

app = FastAPI()


class Command(BaseModel):
    text: str


@app.post("/todo")
async def todo(api_call: Command):
    llm = OpenAI(temperature=0)
    _DEFAULT_TEMPLATE = """
    You have to act as a backend server for a web application that allows users to manage TODO lists.
    You receive requests and based on the type and content of the request, you have to update the database state and return
    a response.

    Given the request, first create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
    Use the following format:

    Question: "Question here"
    SQLQuery: "SQL Query to run"
    SQLResult: "Result of the SQLQuery"
    Answer: "Final answer here"
    JSON: "JSON response here, list of objects"

    Only use the following tables:

    {table_info}
    
    If the request is about needing to do something, add the task to the database as a new TODO item.

    Question: {input}"""
    p = PromptTemplate(
        input_variables=["input", "table_info", "dialect"], template=_DEFAULT_TEMPLATE
    )

    db = SQLDatabase.from_uri("sqlite:///todos.db")

    db_chain = SQLDatabaseChain(llm=llm, database=db, prompt=p)
    return json.loads(db_chain.run(api_call.text).split("JSON: ")[1])


if __name__ == "__main__":
    uvicorn.run(app)
