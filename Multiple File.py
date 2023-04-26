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
        #Continue the loop if the user(s) enter "y" to prompt for another line of text.
        #Break the loop if the user types "n" to finish the program.
#Close the file