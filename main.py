

from flask import Flask, request

app= Flask(__name__)

tarefas = [
    {
        "id": 1,
        "titulo": "estudar java script",
        "descricao": "estudar java script para aprender a construir eventos",
        "status": "em andamento",
        "data_inicio":"12/06/2025",
        "data_termino":"12/07/2025",
        "materia": "dev1"

    },
    {
        "id": 1,
        "titulo": "estudar flask",
        "descricao": "estudar flask para aprender sobre Web Services",
        "status": "em andamento",
        "data_inicio": "18/02/2025",
        "data_termino": "18/03/2025",
        "materia": "dev2"
    },
    {
        "id": 1,
        "titulo": "estudar flask",
        "descricao": "estudar flask para aprender",
        "status": "em andamento",
        "data_inicio": "19/09/2025",
        "data_termino": "19/10/2025",
        "materia": "dev3"
    }

]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return tarefas

@app.route('/tasks/<int:taks_id>', methods =['GET'])
def get_task_by_id(task_id):
    for tarefa in tarefas:
        if tarefa.get('id')== task_id:
            return tarefa
    return 'terefa não encontrada'

@app.route('/tasks', methods =['POST'])
def create_task():
    task = request.json
    ultimo_id = tarefas[-1].get('id') + 1
    task['id=']= 5
    tarefas.append(task)
    return task

@app.route('/tasks/<int:task_id>', methods = ['PUT'])
def update_task(task_id):
    task_seach = None

    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            task_search = tarefa
            
    task_body = request.json
    task_search['titulo'] = task_body.get('titulo')
    task_search['descricao'] = task_body.get('descricao')
    task_search['status'] = task_body.get('status')

    return task_search

@app.route('/tasks/<int:tasks_id>', methods =['DELETE'])
def delet_task(tasks_id):
    for tarefa in tarefas:
        if tarefa.get('id')== tasks_id:
           tarefas.remove(tarefa)
           return {'message': 'tarefa foi deletada'}
    return {'message': 'tarefa nao encontrada'}

if __name__ =='__main__':
    app.run(debug=True)

