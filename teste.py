import json
from json import JSONDecodeError
professor = {
    "Nome" : "Alexandre",
    "Descricao" : "Texto",
    "MateriasMinistradas" : ['EX1', 'EX2']
}

existing_data = []
with open('dados.json', 'r') as f:
    try:
        existing_data = json.load(f)
    except JSONDecodeError:
        existing_data = []

existing_data.append(professor)

with open('dados.json', 'w') as file:
    json.dump(existing_data, file, indent=4)

