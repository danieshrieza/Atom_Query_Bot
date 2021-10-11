string = "Hello * Bye"

for i in string :
    if ("*" and "o") in string :
        global new_string
        new_string = string.replace("*", "×").replace("o", "O")

print(new_string)

