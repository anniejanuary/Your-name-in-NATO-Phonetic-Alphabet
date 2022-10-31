import pandas

alphabet_pandified = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_pandified.iterrows()}

user_input = input("Enter a word: ").upper()

phonetic_representation = [alphabet_dict[letter] for letter in user_input]
print(phonetic_representation)
