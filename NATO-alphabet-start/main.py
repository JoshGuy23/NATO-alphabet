import pandas

nato_csv = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {
    row.letter: row.code for (index, row) in nato_csv.iterrows()
}

wrong = True

while wrong:
    try:
        user_name = input("Please enter your first name: ").upper()
        nato_name = [nato_dict[letter] for letter in user_name]
    except KeyError:
        print("Please only use letters in the English alphabet.")
    else:
        wrong = False

print(nato_name)
