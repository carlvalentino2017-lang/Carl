import c as c
import math as math
pi = 3.141592653589793
gravidade = 0
jump = 0.01
jump3 = 1
height = 0
jump2 = input("Digite se vc quer que rode? (digite s para sim) ")
if jump2 == "s":
    jump1 = True
    print(height)
elif jump2 != "s":
    jump1 = False
while jump1 == True:
    jump += jump3
    height = jump - gravidade
    if height <= 0:
        gravidade = 0
        height = 0
        print(height)
        break
    jump3 -= 0.05
    if jump3 <= 0:
        jump3 = 0
        gravidade += 0.3
    print(height)
jump1 = False
print(" ")

# class Pessoa:
#     cpf = ""
#     nome = ""
#     idade = ""

#     def __init__(self, cpf , nome, idade):
#         self.cpf = cpf
#         self.nome = nome
#         self.idade = idade
#     def mostrar_arquivos_pessoa(self):
#         print(self.cpf)
#         print(self.nome)
#         print(self.idade, "\n")

# pessoa1 = Pessoa(f"12321424", "alexandrexo", "23")
# pessoa2 = Pessoa("83957343232", "alexandrexa", "20")
# pessoa3 = Pessoa("010101011109", "alexandreko", "18")

# pessoa1.mostrar_arquivos_pessoa()
# pessoa2.mostrar_arquivos_pessoa()
# pessoa3.mostrar_arquivos_pessoa()

class Aluno:
    cpf = ""
    nome = ""
    idade = ""
    notas = []
    matricula = ""
    def __init__(self, cpf , nome, idade, notas, matricula):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.notas = notas
        self.matricula = matricula

    def add_nota(self, nota):
        self.notas.append(nota)

    def calc_media(self):
        soma = 0
        for nota in self.notas:
            soma += nota
        print("media: ", soma/len(self.notas))
    def mostrar_arquivos_aluno(self):
        print(self.cpf)
        print(self.nome)
        print(self.idade)
        print(self.notas)
        print(self.matricula, "\n")

aluno1 = Aluno("0000000002010", "alex", 113, [10, 8 , 9, 9.5, 2, 1.5, 0.5], 837213)
aluno2 = Aluno("123123214", "alexander", 11, [1, 0 , 3, .5, 10, 9.5, 8.9], 837213)
aluno3 = Aluno("1213214", "ana", 13, [10, 8 , 9, 9.5, 8, 7.5, 8.5], 837213)

alunitos = [aluno1, aluno2, aluno3]
for aluno in alunitos:
    aluno.calc_media()
    aluno.mostrar_arquivos_aluno()
