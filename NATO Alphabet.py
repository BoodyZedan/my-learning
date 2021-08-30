import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
data.to_dict()


data1 = {row.letter: row.code for (index, row) in data.iterrows()}


word = input("Enter a word:").upper()
output = [data1[letter] for letter in word]
print(output)
