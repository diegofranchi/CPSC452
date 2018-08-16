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

def FLT():
    pString = input(' p = ')
    p = int(pString)
    
    if not isPrime(p):
        print(p,'not prime')
        return
        
    aString = input(' a = ')
    a = int(aString)
    
    if a >= p:
        print(a,'not less than',p)
        return
        
    eString = input(' exponent = ')
    e = int(eString)
    
    i = 0
    temp = p-1
    while temp*i < e:
        i += 1
    i -= 1
    
    dif = e - (temp*i)
    equation = str(a)+'^'+str(e)+' mod '+str(p)
    flt = '('+str(a)+'^'+str(temp)+' mod '+str(p)+')^'+str(i)
    remainder = '('+str(a)+' mod '+str(p)+')^'+str(dif)
    result = str((a**e)%p)
    
    print(equation+' = '+flt+' * '+remainder+' = '+result)

        
def main():
    FLT()

    
if __name__ == "__main__":
    main()