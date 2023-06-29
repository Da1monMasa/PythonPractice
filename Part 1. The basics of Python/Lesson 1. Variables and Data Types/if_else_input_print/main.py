
first_name = input("Enter your First Name:")
middle_name = input("Enter your Middle Name:")
last_name = input("Enter your Last Name if it exist:")
if(last_name == None):
    username = f"\n{first_name} \n{middle_name}"
    print(username)
else:
    username = f"\n{first_name} \n{middle_name} \n{last_name}"
    print(username)
