#print("Olá, mundo")
#Criando uma variável no Python!!
fruta_citrica_maio = "melancia"
#Imprimindo a variável
print(fruta_citrica_maio)

#Expressões Matemáticas Python

print (2*3+3**2)

carro = "fox"
print(carro)


#função para adicionar pessoas á lista
def adicionar_pessoa(lista, nome, idade, profissao):
    pessoa = {"nome": nome, "idade": idade, "profissao": profissao }
    lista.append(pessoa)

#função para mostrar as pessoas da lista

def exibir_pessoas(lista):
    print("Lista de pessoas cadastradas")
    for pessoa in lista:
        print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Profissao: {pessoa['profissao']}")

#lista para armazenar pessoas
pessoas = []

#adicionando pessoas em uma lista
adicionar_pessoa(pessoas, "Ana", 25, "Engenheira")
adicionar_pessoa(pessoas, "Bruno", 30, "Professor")
adicionar_pessoa(pessoas, "Carla", 22, "Médica")

#exibindo a lista de pessoas
exibir_pessoas(pessoas)

    