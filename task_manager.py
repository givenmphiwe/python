#program request the username and password if its invalid it keep asking again and again
#if user enters a valid password .program will print the menu
#User will only be able to open one option at a time.

while True:
    usernames = input("Please enter your username: ")
    passwords = input("Please enter your password: ")

    if usernames.lower() and passwords.lower() not in ('admin', 'adm1n'):
        print("Please enter a valid username and password")
    else:
        break
print('\n')
if usernames == "admin" and passwords == "adm1n":

    print("Please select one of the following options:")
    print("r - register user")
    print("a - add task")
    print("va - view all tasks")
    print("vm - view my tasks")
    print("e - exit")
    print('\n')

    user_option = input("Write the abbrivation to select one option of the above: ")

    if user_option == "r":
        confirm = input("please enter your password: ")
        if confirm == "adm1n":
            user = input("Write your new username: ")              #asking the user for new details
            password = input("Write your new password: ")

            with open('user.txt', 'a+') as file:                   
                file.write("registered user: \n" + "username: " + str(user) + '\n' + "password: " + str(password))
                print("Your new password and username have been stored \n")
  
    elif user_option == "a":                                                               #asking the user questions to store in text file
        assigned_to = input("Enter the username of the person the task is assigned to: ")    
        tittle = input("Write tittle of the task: ")
        time = input("Write the due date:")
        descrp = input("Write the description of the task: ")

        with open('tasks.txt', 'w') as file:          #storing the questions in text file
            file.write("Due_date \n" + str(time) + '\n' + str(tittle) + '\n' + str(assigned_to) + '\n' + str(descrp))
            print("Your data is stored.")

    elif user_option == "va":
        print("Enter the username of the person the task is assigned to:")
        print("write tittle of the task:")
        print("write the due date:")
        print("write the description of the task:")     #printing the task the user must do

  
    elif user_option == "vm":
        contents = ""
        with open('tasks.txt', 'r', encoding='utf-8') as f:
            for line in f:
                contents = contents + line
        print(contents)             #printing the tasks completed by user on screen

    elif user_option == "e":
        print(exit)
    
    











    
    
