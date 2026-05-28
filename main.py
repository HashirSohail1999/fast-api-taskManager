from fastapi import FastAPI

app = FastAPI()

tasks= [
    {"title":"study Fastapi"},
    {"title2":"study Fastapi"},
    {"title":"study Fastapi"}
]

@app.get("/")
def home():
    return {"message": "Task Api"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task:dict):
    tasks.append(task)
    return {"message":"task added"}