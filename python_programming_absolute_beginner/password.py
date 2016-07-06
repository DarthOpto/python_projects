# Password
# Demonstrates the if statement

print("Welcome to Security Systems, Inc.")
print("-- where security is our middle name -- \n")

password = raw_input("Please enter your password: ")

if password == "secret":
    print("Access Granted")
    print("Welcome, you must be very important")
else:
    print("Access Denied" * 5)

raw_input("\n\nPress the ENTER key to exit.")
