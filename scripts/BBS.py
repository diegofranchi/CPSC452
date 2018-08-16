from fractions import gcd

def BBS():
    pString = input(' p = ')
    p = int(pString)
    
    if p%4 != 3:
        print(p,'not prime enough')
        return
    
    qString = input(' q = ')
    q = int(qString)
    
    if q%4 != 3:
        print(q,'not prime enough')
        return
    
    sString = input(' s = ')
    s = int(sString)
    n = p * q
    
    if gcd(n,s) != 1:
        print(s,'not relatively prime with',n)
        return
    inputString = input(' number of bit sequences to generate? ')
    intput = int(inputString)
    temp = s
    for i in range(intput):
        print('x'+str(i)+' = '+str(temp)+'^2 mod '+str(n)+' = ', end='')
        temp = (temp**2)%n
        print(temp)

        
def main():
    BBS()

    
if __name__ == "__main__":
    main()