from fastapi import FastAPI

app = FastAPI()

tasks= [
    {
        "id":1,
        "title":"learn FastApi",
        "completed":False
    }
]
task_id_counter=2

@app.get("/")
def home():
    return {"message": "Task Api"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task:dict):
    global task_id_counter
    new_task ={
        "id":task_id_counter,
        "title":task["title"],
        "completed":False
    }
    tasks.append(new_task)
    task_id_counter +=1
    return new_task
