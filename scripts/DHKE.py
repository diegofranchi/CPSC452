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
      
def isPrimitiveRoot(a,q):

def ETF(n):  
    relatively_prime = 0
    for i in range(n):
        if gcd(i,n) == 1:
            relatively_prime += 1
            
    return relatively_prime

def DHKE():
    qString = input(' q = ')
    q = int(qString)
    
    if not isPrime(q):
        print(q,'not prime')
        return
        
    aString = input(' a = ')
    a = int(aString)
    
    if not isPrime(a):
        print(a,'not prime')
        return
        
    XaString = input(' Xa = ')
    Xa = int(XaString)
    
    XbString = input(' Xb = ')
    Xb = int(XbString)
    
    
    
    print('C = '+str(m)+'^'+str(e)+' mod '+str(n)+' = '+str(C))
    print('M = '+str(C)+'^'+str(d)+' mod '+str(n)+' = '+str(M))

        
def main():
    RSA()

    
if __name__ == "__main__":
    main()