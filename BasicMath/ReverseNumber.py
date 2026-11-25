def reverseNumber(n):
    n2=str(n)
    rev=n2[::-1]
    return rev
n=int(input("Enter a numberto reverese:"))
print(reverseNumber(n))

"""
rev=0
while n>0:
    last_digit= n%10
    rev= rev*10 + last_digit
    n=n//10
return rev
"""
