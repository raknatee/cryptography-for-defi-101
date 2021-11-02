def prime_number(end:int)->list[int]:
    primes:list[int] = []
    def is_prime_number(x:int)->bool:
        for i in range(2,x+1):
            if(x%i==0 and x!=i):
                return False
        return True

    for number in range(2,end+1):
       
        if(is_prime_number(number)):
            primes.append(number)

    return primes

