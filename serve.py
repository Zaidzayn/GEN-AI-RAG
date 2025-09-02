from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
from pydantic import BaseModel
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Model
model = ChatGroq(model="gemma2-9b-It", groq_api_key=groq_api_key)

# Prompt
generic_prompt = ChatPromptTemplate.from_messages([
    ("system", "Translate the following English text to French."),
    ("user", "{text}")
])


# Output parser
output_parser = StrOutputParser()

# Chain
chain = generic_prompt | model | output_parser


# FastAPI app
app = FastAPI(title="LangServer with Groq", version="1.0")

# Add LangServe route
add_routes(app, chain, path="/chain")

# Run
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost")
