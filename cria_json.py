import json

dict_filmes = {
    1: {'nome': 'forrest gump', 'ano': 1994, 'genero': 'drama', 'duracao': '142 min'},
    2: {'nome': 'drive', 'ano': 2011, 'genero': 'acao', 'duracao': '100 min'},
    3: {'nome': 'blade runner 2049', 'ano': 2017, 'genero': 'ficcao cientifica', 'duracao': '163 min'},
    4: {'nome': 'se7en', 'ano': 1995, 'genero': 'crime', 'duracao': '127 min'},
    5: {'nome': '1917', 'ano': 2019, 'genero': 'guerra', 'duracao': '119 min'},
}

string_json = json.dumps(dict_filmes, indent=2)
with open ('db.json', 'w') as f:
    f.write(string_json)