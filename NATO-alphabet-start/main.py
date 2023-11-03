import pandas

nato_csv = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {
    row.letter: row.code for (index, row) in nato_csv.iterrows()
}

user_name = input("Please enter your first name: ").upper()
nato_name = [nato_dict[letter] for letter in user_name]

print(nato_name)
