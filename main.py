from fastapi import FastAPI

app = FastAPI()

tasks= [
    {
        "id":1,
        "title":"learn FastApi",
        "completed":False
    },
    {
        "id":2,
        "title":"learn FastApi",
        "completed":False
    },{
        "id":3,
        "title":"learn FastApi",
        "completed":False
    }
]
task_id_counter=4

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

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}

    return {"error": "Task not found"}


@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: dict):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated_task.get("title", task["title"])
            task["completed"] = updated_task.get("completed", task["completed"])
            return task

    return {"error": "Task not found"}
