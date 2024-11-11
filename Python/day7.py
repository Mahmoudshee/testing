# age = int(input("Enter your age: "))
# # Check if the age condition is met
# if age > 18:
#     gender = input("Enter your gender: ")
#     country = input("Enter your religion: ")
#     # Check gender and religion if the age condition is met
#     if gender == "female" and country == "kenya":
#         print("You are welcome")
#     else:
#         print("You are not allowed to attend this party!!")
# else:
#     # Immediately handle the case for underage
#     print("You are under age!!")

age = int(input("Enter your age: "))
gender = input("Enter your gender: ")
religion = input("Enter your religion: ")

if age < 18:
    print("You are not allowed")
elif gender != "female" and religion != "muslim":
    print("You are not allowed")
else:
    print("You are allowed")
