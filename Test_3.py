# Write a Python program to check if a string is a palindrome or not. Your program should account for the presence
# of any special characters used in English.

def palindrome(string):
    new_string = ''
    for x in string:
        if x.isalpha():
            new_string += x

    if new_string.lower() == new_string.lower()[::-1]:
        return "String is palindrome"
    else:
        return "String is not a palindrome"


if __name__ == '__main__':
    s = str(input("Enter your string: "))
    print(palindrome(s))
