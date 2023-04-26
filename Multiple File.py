#Vargas, Ruben A.
#BSCPE 1-4
#Object-Oriented Programming

#To start writing, open the "mylife.txt" file.
with open("mylife.txt", "w") as file:

    #Loop until the user decides to end it.
    while True:
        #Request to the user to enter a line of text.
        line = input("Enter line: ")
        #Add the text line, then a new line character, to the file.
        file.write(f" {line}\n")
        #Ask the user if they want to enter another line of text.
        users_choice = input("Are there more lines y/n? ")
        #Continue the loop if the user(s) enter "y" to prompt for another line of text.
        if users_choice.lower() == "y":
            continue
        #Break the loop if the user types "n" to finish the program.
        if users_choice.lower() == "n":
            break
#Close the file