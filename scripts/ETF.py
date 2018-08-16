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

def ETF():
    
    nString = input(' n = ')
    n = int(nString)
    
    relatively_prime = 0
    for i in range(n):
        if gcd(i,n) == 1:
            relatively_prime += 1
            
    print(relatively_prime)

        
def main():
    ETF()

    
if __name__ == "__main__":
    main()