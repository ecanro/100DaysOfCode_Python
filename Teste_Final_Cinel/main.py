# # 1
from random import  randint
#
# num = randint(1, 1001)
# # print(num)
# if num % 2 == 0:
#     print("PAR")
# else:
#     print("IMPAR")
#
#
# # 2
#
# list = []
#
# for x in range(5):
#     name = input("Por favor insira um nome: ")
#     list.append(name)
# list.sort()
# print(list)
#
# # 3
# num = int(input("Por favor insera um numero: "))
# if num > 0:
#     print(f"O numero inserido {num} é positivo!")
# elif num < 0:
#     print(f"O numero inserido {num} é negativo!")
# else:
#     print(f"O numero {num} é Nulo")
#
# # 4
#
# from time import sleep
#
# num = int(input("Input a negative number please: "))
# if num < 0:
#     for x in range(num, 1):
#         sleep(1)
#         print(x)
#
# # 5
#
# frase = "Programação em Python"
# user_frase = input("Insira una expressão: ")
# print(f"O tamanho da frase e: <<{len(frase)}>>")
# print(f"O tamanho da sua expressão inserida e: <<{len(user_frase)}>>")
# substring = frase.find(user_frase)
# if substring > 0:
#     print(f"<<{user_frase}>> é uma substring de <<{frase}>>")
# else:
#     print(f"<<<{user_frase}>> não é uma substring de <<{frase}>>")
#
#
# #####outra manera
#
# if user_frase in frase:
#     print(f"A expressão <<{user_frase}>> é uma substring da frase <<{frase}>>")
# else:
#     print(f"Não se encontro a expressão <<<{user_frase}>> dentro de <<{frase}>>")
#
# # replace Python into frase
# print(frase.replace("Python", user_frase))
#
#
# # 6
# #function for calculate the len without space
# def function_char(frase):
#     num_of_char = len(frase) - frase.count(" ")
#     print(f"Numero de caracteres da frase: {num_of_char}")
#
#     is_upper, is_lower, is_symbol = 0, 0, 0
#     for char in frase:
#         if 'A' <= char <= 'Z':
#             is_upper += 1
#         elif char.islower():
#             is_lower += 1
#         elif char != 'A' or char != 'Z' and char != "a" or char != "z" or char != " ":
#             is_symbol += 1
#     return is_upper, is_lower, is_symbol;
#
#
# frase = input("Por favor insira uma frase: ")
# answer = function_char(frase)
# print(f"Quantidade de maiúsculas é {answer[0]}")
# print(f"Quantidade de minúsculas é {answer[1]}")
# print(f"Quantidade de digitos é {answer[2]}")
#

# 7

tupla = ()
def criar_tuplo(num1, num2):
    if num1 >= 2 and num2 >= 2:
        for x in range(num1, (num2+1)):
            tupla = tupla+ (x, )
        print(tupla)
    else:
        print("Os numeros inseridos tem que ser maior que 1")


largest_num = 0
smallest_num = 0


def maior_menor(criar_tuplo):
    smallest = tupla[0]
    for e in tupla:
        if e < smallest:
            smallest = e
    print(smallest)

    largest = tupla[0]
    for e in tupla:
        if e > largest:
            largest = e
    print(largest)

num1 = int(input("Insira um numero maior a 1: "))
num2 = int(input("Insira outro numero maior a 1: "))
print(f"The elements in the tuple are: {criar_tuplo}")
maior_menor(criar_tuplo)
maior_menor(criar_tuplo)

# 8
list = []

for x in range(0, 10):
    random_num = randint(2, 500)
    list.append(random_num)

    def func_primo(list):
        for x in list:
            if x > 1:
                s = int(x / 2)
                for i in range(2, s + 1):
                    if x % i == 0:
                        print(x, "not prime")
                        break
                print(x, "prime")
print(list)
func_primo(list)

