string = "Hello * B/e"

for i in string :
    if ("*" or "/") in string :
        global new_string
        new_string = string.replace("*", "×").replace("/", "÷")

print(new_string)

