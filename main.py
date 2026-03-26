from fastapi import FastAPI

app = FastAPI()

tarefas = []

@app.get("/tarefas")
def get_tarefas():
    return tarefas

@app.post("/tarefas")
def criar_tarefa(tarefa: dict):
    tarefas.append(tarefa)
    return tarefa

@app.put("/tarefas/{id}")
def atualizar_tarefa(id: int, tarefa: dict):
    tarefas[id] = tarefa
    return tarefa

@app.delete("/tarefas/{id}")
def deletar_tarefa(id: int):
    tarefas.pop(id)
    return {"mensagem": "Tarefa removida"}