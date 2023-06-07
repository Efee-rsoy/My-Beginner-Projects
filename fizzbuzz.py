'''
This code prints numbers from 1 to 100 but if the number is multiple of 3 it prints Fizz, if the number is multiple of 5, it prints Buzz,
if the number is multiple of 3 and 5, it prints FizzBuzz.
'''

def fizz_buzz():
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

        

a = fizz_buzz()
print(a)
