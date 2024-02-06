my_username = "Vital Vortex"
my_password = "VV1234"

input("Welcome to this page!")
input("To let you pass, you will first have to log-in.")
user_name = input("Name: ")
user_password = input("Password: ")
if user_name == my_username and user_password == my_password:
    print("PASSWORD: VALID.\nYou may proceed to the next interface.")
    input()
else:
    input("PASSWORD OR USERNAME INVALID.")
    user_answer1 = input("Would you like to try again?")
    while user_answer1 == "Yes" or "yes":
