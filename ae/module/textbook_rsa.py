from .prime_number import prime_number



def keygen(p:int,q:int)->dict:
    """
    p,q are prime number
    """
    print(f"keygen with {p=}, {q=}")
    N = p*q
    print(f"N = {p} x {q} = {N}")
    F_N = (p-1)*(q-1)
    print(f"Phi(N) = {p-1} x {q-1} = {F_N}")


    K_Es = coprime(F_N,N)
    print(f"coprime",K_Es)
    picking_index = 0
    K_E = K_Es[picking_index]
    print(f"pick at {picking_index} => {K_E=}")
    
    def find_k_d(e):
        d = 1
        while True:
            print(f"d={d}, e*d={e*d}, e*d % Phi(N)= {(e*d)%F_N} "  )
            if( (e*d)%F_N ==1 and e!=d):
                return d
            d+=1

    K_D = find_k_d(K_E)

    return { 
        "K_E":{"key":K_E,"mod":N},
        "K_D":{"key":K_D,"mod":N}
    }




def coprime(F_N:int,N:int)->list[int]:
    primes = prime_number(F_N)
    print(f"choose e from [{2}, {F_N}] and coprime with {N}, {F_N}")
    coprime = list(filter(lambda x:N%x!=0 and F_N%x!=0,primes))
    
    return coprime
def discrete_log(x:int,key:int,modulus_p:int)->int:
    result = (x**key)%modulus_p
    print(f"{x}**{key} mod {modulus_p} = {result}")
    return result
