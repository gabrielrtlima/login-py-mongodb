import pymongo
import json
import sys
import os

def reiniciar_programa():
    os.execv(sys.executable, ['python'] + sys.argv) 

#CONEXÃO COM O BANCO DE DADOS
client = pymongo.MongoClient("mongodb+srv://loginsystem:123@db.jkcwq.mongodb.net/<users>?retryWrites=true&w=majority")
db = client.users
collection = db["users"]

#FUNÇÃO DE CADASTRO NO BANCO DE DADOS
def cadastrar_db():
    document = {"NOME":nome,
    "EMAIL":email,
    "Usuario":usuario,
    "SENHA":senha,
    "idade":idade}
    id = db.users.insert_one(document).inserted_id
    print(id)

#FUNÇÃO DE CADASTRO DE DADOS
def cadastrar_dados():
    global nome
    global email
    global usuario
    global senha
    global idade
    nome = input('Digite seu nome: ')
    email = input('Digite seu e-mail: ')
    usuario = input('Digite seu nome de usuário: ')
    verificar_usuario()
    senha = input('Digite sua senha: ')
    idade = input('Digite sua idade: ')
    print('Seus dados foram cadastrados!')
    return nome, email, usuario, senha, idade

#FUNÇÃO DE VERIFICAR USUARIO
def verificar_usuario():
    global myquery
    global usuario_fail
    letras = 13 + len(usuario)
    myquery = {"Usuario":usuario}
    mydoc = collection.find(myquery, {"_id": 0, "NOME": 0, "EMAIL": 0, "SENHA": 0, "idade": 0})
    
    for x in mydoc:
        x
        result = json.dumps(x)
        result = result[13:letras]    
        if usuario == result:
            usuario_fail = input('Nome de usuário já existe.\nDIGITE 1 PARA REINICIAR O PROGRAMA OU DIGITE 2 PARA SAIR.\n')    
            if usuario_fail == '1':
                reiniciar_programa()
            else:
                quit()

inicio = input("Bem vindo ao sistema de login v1.0\nDigite 1 se deseja criar uma nova conta | Digite 2 se deseja realizar login\n")

if inicio == '1':
    cadastrar_dados()
    cadastrar_db()

