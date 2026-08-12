import re
print("Task 1------------------------------")
def is_positive_less_than_300(value):
    return(bool(re.fullmatch(r"^[1-9]|[0-9]\d|[12]\d\d$",value)))
print(is_positive_less_than_300("1"))
print(is_positive_less_than_300("15"))
print(is_positive_less_than_300("99"))
print(is_positive_less_than_300("100"))
print(is_positive_less_than_300("299"))
print("-----------------")
print(is_positive_less_than_300("0"))
print(is_positive_less_than_300("300"))
print(is_positive_less_than_300("-5"))
print(is_positive_less_than_300("3.14"))
print(is_positive_less_than_300("abc"))

print("Task 2------------------------------")
def is_number_from_1_to_255(value):
    return(bool(re.fullmatch(r"^[1-9]|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]$",value)))
print(is_positive_less_than_300("256"))

print(is_number_from_1_to_255("1"))
print(is_number_from_1_to_255("25"))
print(is_number_from_1_to_255("100"))
print(is_number_from_1_to_255("255"))
print("-----------------")
print(is_number_from_1_to_255("0"))
print(is_number_from_1_to_255("256"))
print(is_number_from_1_to_255("025"))
print(is_number_from_1_to_255("-1"))
print(is_number_from_1_to_255("2.5"))

print("Task 3------------------------------")
def is_israel_mobile(phone):
    return(bool(re.fullmatch(r"^(\+972|0)5\d-?\d{2}-?\d-?\d-?\d{3}$",phone)))
print(is_israel_mobile("0541234567"))
print(is_israel_mobile("054-1234567"))
print(is_israel_mobile("+97254-123-4567"))
print(is_israel_mobile("058-12-34-567"))
print("-----------------")
print(is_israel_mobile("54-1234567"))
print(is_israel_mobile("054--12-4567"))
print(is_israel_mobile("+972054-123-4567"))
print(is_israel_mobile("97254-123-4567"))

print("Task 4------------------------------")
def is_valid_time(time):
    # return (bool(re.fullmatch("^[0-9]|[12][0-3]:\d[0-9]|[0-5][0-9]$",time)))
    return (bool(re.fullmatch(r"^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$", time)))
print(is_valid_time("00:00"))
print(is_valid_time("09:30"))
print(is_valid_time("14:45"))
print(is_valid_time("23:59"))
print("-----------------")
print(is_valid_time("24:00"))
print(is_valid_time("12:60"))
print(is_valid_time("8:30"))
print(is_valid_time("123:45"))
print(is_valid_time("12-30"))

print("Task 5------------------------------")
def is_israel_car_number(number):
    return(bool(re.fullmatch(r"^(\d{2}-\d{3}-\d{2}|\d{3}-\d{2}-\d{3})$",number)))

print(is_israel_car_number("12-345-67"))
print(is_israel_car_number("99-999-99"))
print(is_israel_car_number("123-45-678"))
print(is_israel_car_number("456-78-901"))
print("-----------------")
print(is_israel_car_number("12345678"))
print(is_israel_car_number("12:345:67"))
print(is_israel_car_number("1-234-56"))
print(is_israel_car_number("1234-56-78"))
print(is_israel_car_number("qq-qqq-qq"))


'''
Task 1. Positive Number Less Than 300
Write a function named is_positive_less_than_300(value).
The function should return True if the string contains a positive integer from 1 to 299.

Valid inputs:
1
15
99
100
299

Invalid inputs:
0
300
-5
3.14
abc

Task 2. Number from 1 to 255
Write a function named is_number_from_1_to_255(value).
The function should validate an integer from 1 to 255 inclusive (no leading zeros permitted).

Valid inputs:
1
25
100
255

Invalid inputs:
0
256
025
-1
2.5

Task 3. Israeli Mobile Phone Number
Write a function named is_israel_mobile(phone).
Validate Israeli mobile phone numbers in valid formats.

Valid inputs:
0541234567
054-1234567
+97254-123-4567
058-12-34-567

Invalid inputs:
54-1234567
054--12-4567
+972054-123-4567
97254-123-4567

Task 4. Time Format Validation
Write a function named is_valid_time(time).
Validate 24-hour time in HH:MM format (two-digit hours and minutes).

Valid inputs:
00:00
09:30
14:45
23:59

Invalid inputs:
24:00
12:60
8:30
123:45
12-30

Task 5. Israeli Vehicle License Plate Number
Write a function named is_israel_car_number(number).
Support both 7-digit and 8-digit Israeli license plate formats:
XX-XXX-XX
XXX-XX-XXX

Valid inputs:
12-345-67
99-999-99
123-45-678
456-78-901

Invalid inputs:
12345678
12:345:67
1-234-56
1234-56-78
'''