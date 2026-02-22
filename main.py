import string
from pyscript import *

def password_checkerv1():
    # Check if username length is at least 7 characters
    if len(document.getElementById("username_inp").value) < 7:
        return "Username not long enough"
    else:
        # Check if username contains both letters and digits
        if not document.getElementById("username_inp").value.isalpha():
            if not document.getElementById("username_inp").value.isdigit():
                print("Valid")
            else:
                return "Please include letters on your username"
        else:
            return "Please include digits on your username"

    # Get the password input
    pass_grab = document.getElementById("password_inp").value

    # Loop through each character to check for special characters
    for char in pass_grab:
        if char in list(string.punctuation):
            return "No Special Characters on your password"
    
    # Check if password length is at least 10 characters
    if len(pass_grab) < 10:
        return "Password not long enough"

    # Check if password contains both letters and digits
    if not pass_grab.isalpha():
        if not pass_grab.isdigit():
            return True
        else:
            return "Please include letters on your password"
    else:
        return "Please include digits on your password"


def check_pass(e):
    # Clears previous output
    document.getElementById("output").innerHTML = ""

    # Calls the password checker function
    result = password_checkerv1()

    # Displays result based on validation
    if result == True:
        document.getElementById("output").style.color = "green"
        document.getElementById("output").innerHTML = f"Your account is valid. Welcome, {document.getElementById("username_inp").value}"
    else:
        document.getElementById("output").style.color = "red"
        document.getElementById("output").innerHTML = result