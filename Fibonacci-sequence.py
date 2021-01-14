n = int(input())

def fibo(n):
    seq = [0]
    i = 0
    sum = 1
    while len(seq) < n and type(n) is int:
        sum = sum + i
        i = seq[-1]
        seq.append(sum)
        
    return seq

print(fibo(n))
    
