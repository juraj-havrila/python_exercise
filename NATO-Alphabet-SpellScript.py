import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_Alphabet={row.letter:row.code for (index, row) in data.iterrows()}
user_input=list((input("Please enter your text which you want to have spelled out: ")).upper())
for letter in user_input:
    if letter in NATO_Alphabet.keys():
        print(f"{letter} -- {NATO_Alphabet[letter]}")
    else:
        print("")
