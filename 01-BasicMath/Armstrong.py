def armstrong(n):
    original = n
    digit = 0
    l=len(str(n))
    sum=0
    while original >0:
        digit = original % 10
        sum = sum + digit**l
        original = original //10
    if sum == n:
        return "True"
    else:
        return "False"
a = int(input("enter a number: "))
print(armstrong(a))
