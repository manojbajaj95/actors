from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from workflows.chat import BlogWorkflow, ChatWorkflow

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/chat")
async def chat():
    w = ChatWorkflow()
    return w.work()

@app.get("/blog")
async def blog():
    w = BlogWorkflow()
    return w.work()