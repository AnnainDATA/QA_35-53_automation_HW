print("Task 1")
numbers = [10, 20, 30]
def get_list_element(items, index):
    try:
        print(items[index])
    except IndexError:
        print("Index is out of range!")

get_list_element(numbers, 2)
get_list_element(numbers, 10)
print("-----------------------------------------------------")

print("Task 2")
user1={"name":"Anna",
      "age":30}
def get_user_data(user, key):
    try:
        print(user[key])
    except KeyError:
        print("Key was not found!")
get_user_data(user1, "name")
(get_user_data(user1, "email"))
print("-----------------------------------------------------")

print("Task 3")
def calculate_average(first_value, second_value):
    try:
        a1=float(first_value)
        a2 = float(second_value)
    except ValueError:
        print("Value must be a number!")
    except TypeError:
        print("Invalid data type!")
    else:
        aver = (a1+a2)/2
        print(aver)
calculate_average("10", "20")
calculate_average("hello", "20")
calculate_average(None, 20)
print("-----------------------------------------------------")

print("Task 4")
# def read_number():
#     try:
#         int(input("Enter any number please:"))
#     except (TypeError, ValueError):
#         print("Invalid number!")
#     else:
#         print("Number was entered successfully.")
#     finally:
#         print("Program finished.")
# read_number()
print("-----------------------------------------------------")

print("Task 5")
def validate_age(age):
    if age<0:
        raise ValueError (f"Age ({age}) cannot be negative")
    if age>120:
        raise ValueError (f"Age ({age}) is not realistic")
# validate_age(130)
# validate_age(-5)
try:
    print(validate_age(130))
except ValueError as error:
    print(error)

try:
    print(validate_age(-5))
except ValueError as error:
    print(error)
print("-----------------------------------------------------")

print("Task 5A")
ages=[17,25,-5,150,46,300,99,119]
for age in ages:
    try:
        validate_age(age)
    except ValueError as error:
        print(error)


