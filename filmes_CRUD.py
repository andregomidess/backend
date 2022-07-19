# CRUD -> Create Read Update Delete
import json

class Filme():
    def __init__(self, id: int, nome: str, ano: int, genero: str, duracao: str):
        self.__id = id
        self.__nome = nome
        self.__ano = ano
        self.__genero = genero
        self.__duracao = duracao
    
    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_ano(self):
        return self.__ano
    
    def get_genero(self):
        return self.__genero
    
    def get_duracao(self):
        return self.__duracao
    
    def set_dict(self):
        ret_dict = {self.__id: {'nome': self.__nome, 'ano': self.__ano, 'genero': self.__genero, 'duracao': self.__duracao}}
        return ret_dict
    
class crud():

    def create(self, id: int, nome: str, ano: int, genero: str, duracao: str):
        filme = Filme(id, nome, ano, genero, duracao)
        dict_filme_novo = filme.set_dict()
        with open('db.json', 'r+') as f:
            dict_atual = json.load(f)
            dict_atual.update(dict_filme_novo)
            dict_novo = json.dumps(dict_atual, indent=2)
            f.close()
        with open('db.json', 'w+') as file:
            file.write(dict_novo)
            file.close()
    
    def read(self):
                
            
if __name__ == '__main__':
    c = crud()  
    c.create(6, 'jdjd', 2012, 'acao', '120 min')              