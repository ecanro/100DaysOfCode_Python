# working with strings
# function to sort frase
def sort(str):
    print(f'Frase usando sorting: {str[num_sorts1:num_sorts2]}')

# function to print frase 2 in 2
def print_f(str):
    print(str[::2])
    print('Frase de 2 en 2: ')
    for e in str[::2]:
        print(f'{e}', end='')
# functional
def print_str(str, num_sorts1, jump):
    seq = str[num_sorts1::jump]
    print(f'a frase fica asim: {seq}')


# sorting
def sort_f(str):
    num_sort = int(input(f'Ingrese um numero entre 1 e {len(str)}: '))
    print(f'Frase imprimiendo até posição {num_sort}: {str[:num_sort+1]}')
    print(f'Frase imprimiendo desde posição {num_sort}: {str[num_sort:]}')
    # for e in str[:num_sort]:
    #     print(f'{e}', end="")
    # for e in str[num_sort:]:
    #     print(f"{e}", end='')


# main script
str = input('Escreva uma frase: ')
print(f'A frase é: {str}')

# tamanho da frase
print(f'O tamanho da frase e com len(): {len(str)}')
#option2 using for loop
qt = 0
for c in str:
    qt += 1
print(f'O tamanho da frase com for: {qt}')

# Mayusculas, minusculas e capitalize
# print('Frase Capitalize, title, mayusculas e minusculas: ')
print(f'Frase usando capitalize: {str.capitalize()}, so imprime a primera Letra da frase en Maiusculas')
print(f'Frase usando tittle: {str.title()}, capitaliza cada palavra da frase')
print(f'Frase usando upper: {str.upper()}')
print(f'Frase usando lower: {str.lower()}')

# print(str.swapcase())
# .islower() or .isupper()
num_sorts1 = int(input(f'Ingrese um valor entre 0 e {len(str)}: '))
num_sorts2 = int(input(f'Ingrese outro valor entre 0 e {len(str)}: '))
jump = int(input('Ingrese o valor do salto entre cada caracter: '))

# how many character occurs in the frase

# for l in str:
#     if l == letter:
#         qt+=1

# find some word in the frase
word = input('Ingrese una palavra a buscar na frase')
position = str.find(word)
if position == -1:
    print('Word not find in the frase: ')
else:
    print(f'The word: {word} is find in the position: {position}')


def count(str):
    qt = 0
    for l in str:
        qt += 1
    print(f'O tamanho da frase e: {qt}')



sort(str)
print_f(str)
sort_f(str)
print_str(str, num_sorts1, jump)
count(str)