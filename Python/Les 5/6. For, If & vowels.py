s = "Guido van Rossum heeft programmeertaal Python bedacht."
klinker = ["a","e","i","o","u"]
for letter in s:
    if letter in klinker:
        print(letter)