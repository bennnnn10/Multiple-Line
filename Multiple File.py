#Vargas, Ruben A.
#BSCPE 1-4
#Object-Oriented Programming

#Header design
print("\033[;33;1;3m=\033[0m" * 70)
print("\033[;1;3mHello, I hope you are doing good!\U0001f600\033[0m".center(81))
print("\033[;33;1;3m=\033[0m" * 70)

#Ask what is the name of the user and greetings
print("")
print("\033[1;3mMy name is \033[;96;1;3mCodeperman\033[0m")
your_name = input("\033[1;3mWWhat is your name? \033[0m")
print("\033[;1;3mNice to meet you! \033[;34;1;3m" + your_name + "\033[0m \033[;1;3m, be ready!\033[0m")

print("")
print("\033[;33;1;3m-\033[0m" * 70)
print("\033[;1;3mLet us start our mission for today!\033[0m".center(81))
print("\033[;33;1;3m-\033[0m" * 70)

#To start writing, open the "mylife.txt" file. The file will be created if it does not already exist.
with open("mylife.txt", "w") as file:

    #Loop until the user decides to end it.
    while True:
        #Request to the user to enter a line of text.
        line = input("\n\033[;34;1;3mEnter line: \033[0m")
        #Add the text line, then a new line character, to the file.
        file.write(f" {line}\n")
        #Ask the user if they want to enter another line of text.
        users_choice = input("\033[;96;1;3mAre there more lines y/n? \033[0m")
        #Continue the loop if the user(s) enter "y" to prompt for another line of text.
        if users_choice.lower() == "y":
            continue
        #Break the loop if the user types "n" to finish the program.
        if users_choice.lower() == "n":
            break

#Close the file
file.close()

print("\033[;33;1;3m-\033[0m" * 70)
print(f"\n\033[31;1;3mCodeperman is leaving.....\033[0m")