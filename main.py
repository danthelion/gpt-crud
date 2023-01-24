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
async def todo(command: Command):
    p = PromptTemplate(input_variables=["input", "table_info", "dialect"], template=open("command.template").read())
    chain = SQLDatabaseChain(llm=OpenAI(temperature=0), database=SQLDatabase.from_uri("sqlite:///todos.db"), prompt=p)
    return json.loads(chain.run(command.text).split("JSON: ")[1])


if __name__ == "__main__":
    uvicorn.run(app)
