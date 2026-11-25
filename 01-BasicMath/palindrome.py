def palindrome(n):
    original = n
    rev=0
    while n>0:
        last_digit=n%10
        rev = rev*10 + last_digit
        n=n//10
    return original == rev

n=int(input("enter a number to check if it is palindrome or not: "))
if palindrome(n):
    print(n,' is palindrome')  # this gets printed
else:
    print(n,' is not a palindrome') # or this gets printed
print(palindrome(n))  # this at any cost gets printed
