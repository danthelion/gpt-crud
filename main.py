import json

from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn
from langchain import OpenAI, PromptTemplate, LLMChain
load_dotenv()


app = FastAPI()


@app.get("/todo/{api_call}")
async def todo(api_call: str):
    print(f"API call: {api_call}")
    state = json.loads(open("state.json", "r").read())

    print(f"State: {state}")

    prompt_template = """
You have to act as a backend server for a web application that allows users to manage TODO lists.
You receive requests and based on the type and content of the request, you have to update the database state and return
a response.

The database state is a json object that currently looks like this:

{state}

Ther received request is as follows: {api_call}

Based on the request, you have to update the database state and return a response.
If the response does not modify the database state, then return the response without modifying the database state.

If the requested action is not supported, then return a response with status code 400.

If the requested item name or id is not part of the state, then return a response with status code 404.

The response should only contain a valid serialized JSON string using double quotes and strictly nothing else.
Without any quotes. Always start your response with the word "Response: ".
    """

    prompt = PromptTemplate(
        input_variables=["state", "api_call"],
        template=prompt_template,
    )

    llm_chain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0))
    res = llm_chain.predict(state=json.dumps(state), api_call=api_call)
    # clean response
    res = res.split("Response: ")[1]
    # replace single quotes with double quotes
    res = res.replace("'", '"')
    res = json.loads(res)
    if "todos" in res:
        with open("state.json", "w") as f:
            f.write(json.dumps(res))
    return res


if __name__ == "__main__":

    uvicorn.run(app)
