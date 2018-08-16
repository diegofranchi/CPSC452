from fractions import gcd

def isPrime(p):
    if p > 1:
       for i in range(2,p):
           if (p % i) == 0:
               return False
       else:
           return True
    else:
      return False

def ETF(n):  
    relatively_prime = 0
    for i in range(n):
        if gcd(i,n) == 1:
            relatively_prime += 1
            
    return relatively_prime

def RSA():
    pString = input(' p = ')
    p = int(pString)
    
    if not isPrime(p):
        print(p,'not prime')
        return
        
    qString = input(' q = ')
    q = int(qString)
    
    if not isPrime(q):
        print(q,'not prime')
        return
        
    eString = input(' e = ')
    e = int(eString)
    
    mString = input(' M = ')
    m = int(mString)
    
    n = p * q
    totient = ETF(n)
    
    if 1 >= e:
        print(e,'less than 1')
        return
    elif e >= totient:
        print(e,'greater than p*q')
        return
    
    if gcd(e,totient) != 1:
        print('gcd(',e,totient,') != 1')
        return

    d = 0
    while (d*e)%totient != 1:
        d += 1
    
    if 0 > d:
        print('d less than 0')
        return
    elif d > n:
        print ('d greater than n')
        return
        
    if m > n:
        print('m greater than n')
        return
        
    C = (m**e)%n
    M = (C**d)%n
    
    print('C = '+str(m)+'^'+str(e)+' mod '+str(n)+' = '+str(C))
    print('M = '+str(C)+'^'+str(d)+' mod '+str(n)+' = '+str(M))

        
def main():
    RSA()

    
if __name__ == "__main__":
    main()