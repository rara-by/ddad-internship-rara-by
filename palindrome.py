def palindromes(p):
    p = p.lower()
    
    if p == p[::-1] and len(p)%2==1:
        print('Odd Palindrome')
    elif p == p[::-1] and len(p)%2==0:
        print('Even Palindrome')
    else:
        print('Not a Palindrome')
        

string  = input()
palindromes(string)
