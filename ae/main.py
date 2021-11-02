from module.textbook_rsa import keygen,discrete_log

"""
prime number < 100
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
"""


KE_KD = keygen(2,7)
K_E = KE_KD["K_E"]
K_D = KE_KD["K_D"]

print(f"{K_E}")
print(f"{K_D}")



msg = 2
print(f"{msg=}")
cipher_text = discrete_log(msg,K_E["key"],K_E["mod"])
print(f"{cipher_text=}")
assert msg < K_E["mod"]

assert msg == discrete_log(cipher_text,K_D["key"],K_D["mod"])
