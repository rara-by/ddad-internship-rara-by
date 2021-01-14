print("Enter an integer")
n = int(input()) 

def fact(n):
    out = 1
    if n>0 and type(n) is int:
        for i in range(1,n+1):
            out *= i
    return out

print(fact(n))
