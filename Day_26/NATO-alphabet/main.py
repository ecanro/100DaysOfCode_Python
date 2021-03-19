# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
import pandas


nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(nato_data)
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

print(nato_dict)
word = input("Ingrese una palabra: ").upper()
output_list = [nato_dict[letter] for letter in word]
print(output_list)


