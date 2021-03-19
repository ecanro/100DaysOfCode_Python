import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
print(nato_dict)



def generate_nato_list():
    word = input("Enter a word: ").upper()
    try:
        output_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_nato_list()
    else:
        print(output_list)



generate_nato_list()