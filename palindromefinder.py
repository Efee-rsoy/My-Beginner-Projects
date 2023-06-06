def is_palindrome(x):
    a = x.lower()
    return a[::-1] == a

user_input = input("Enter a string: ")
result = is_palindrome(user_input)
print(result)
