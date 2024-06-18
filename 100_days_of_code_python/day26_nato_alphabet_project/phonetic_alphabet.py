import pandas

data = pandas.read_csv("phonetic_alphabet.csv")
alpha_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
output = [alpha_dict[letter] for letter in word]
print(output)

