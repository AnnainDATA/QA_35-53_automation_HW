print('--------------------------1---------------------------')
def print_string_reverse (s):
    if s is None or s == '' or s.isspace():
        print('Wrong string!')
    else:
        for i in s[::-1]:
            print(i)

s="Shalom"
print_string_reverse(s)

print('--------------------------1A--------------------------')
def print_string_reverse1 (s1):
    if s1 is None or s1 == '' or s1.isspace():
        print('Wrong string!')
    else:
        for i in reversed(s1):
            print(i)
s1="Shalom"
print_string_reverse(s1)

print('--------------------------2---------------------------')
def is_isr_phone_number(phone:str):
    if phone is None or phone=="" or str(phone).isspace():
        print("None")
    else:
        if str(phone)[0]=="0" and len(phone)==10 and phone.isdigit():
            print("True")
        else:
            print("False")

is_isr_phone_number("0521234567")
is_isr_phone_number("521234567")
is_isr_phone_number("05212345a7")
is_isr_phone_number("")

print('--------------------------3---------------------------')
def print_substring_reverse(s, start, finish):
    if type(start)!=int or type(finish)!=int or s is None or s=="" or s.isspace() or start>finish or start>len(s)-1 or finish>len(s)-1:
        print("Wrong arg!")
    else:
        s_left=s[:start]
        s_right=s[finish+1:]
        s_middle = s[start:finish + 1][::-1]
        print(s_left+s_middle+s_right)
print_substring_reverse("Shalom", 1, 3)

print('--------------------------4---------------------------')
def get_words_reverse(s):
    for i in s.split(" ")[::-1]:
        print(i, end=" ")
get_words_reverse("Hello my nice world")
print()
print("---------")
get_words_reverse("Vanity of vanities, all is vanity")

print()
print('--------------------------4ADV------------------------')
def print_words_reverse_in_column(s):
    for i in s[::-1].split(" ")[::-1]:
        print(i)
print_words_reverse_in_column("Hello my nice world")
print("---------")
print_words_reverse_in_column("There’s nothing new under the sun")
print()

'''
HW
1.
Write a function print_string_reverse(s)
The function takes a string and prints it to the console in reverse order.
If the string is None, empty, or consists only of spaces, the function should print: Wrong string
Example:
print_string_reverse("Shalom")
Console output:
molahS

2.
Write a function is_isr_phone_number(phone)
The function takes a string and checks whether it is a valid Israeli phone number.
Conditions for a valid number: the first digit must be 0; the total number of characters must be exactly 10; 
all characters must be digits. If the string meets all conditions, the function returns True. 
If it fails to meet the conditions, the function returns False. If the string is None, empty, 
or consists only of spaces, the function returns None.
Examples:
is_isr_phone_number("0521234567") → True
is_isr_phone_number("521234567") → False
is_isr_phone_number("05212345a7") → False
is_isr_phone_number("") → None

3.
Write a function print_substring_reverse(s, start, finish)
The function takes a string, a start index, and a finish index.
It should print a string to the console where the characters from the start index to the finish index 
(inclusive) are reversed, while the remaining characters stay in their original order.
Example:
print_substring_reverse("Shalom", 1, 3)
Original string: Shalom
Substring from index 1 to index 3 inclusive: hal
After reversal: lah
Console output: Slahom
If the string is None, empty, or consists only of spaces, or if the start/finish indices are out of bounds, or if start > finish, the function should print: Wrong args.

4. 
Write a function get_words_reverse(s)
The function takes a string where words are separated by spaces and returns the original string with the word 
order reversed.
Example:
get_words_reverse("Hello my nice world")
Result: world nice my Hello

Advanced
Write a function print_words_reverse_in_column(s)
The function takes a string where words are separated by spaces and prints the words in a column. 
Each word must be printed backwards (reversed).
Example:
print_words_reverse_in_column("Hello my nice world")
Console output:
olleH
ym
ecin
dlrow
'''






