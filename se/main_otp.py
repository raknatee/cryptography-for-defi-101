def encrypt(msg:str,key:str):
    assert len(msg) == len(key)
    return xor(msg,key)

def decrypt(msg:str,key:str):
    assert len(msg) == len(key)
    return xor(msg,key)

def xor(string1,string2):
    temp = ""
    for s1,s2 in zip(string1,string2):
        temp += str(int( ( bool(int(s1)) != bool(int(s2)) )))
    return temp

if(__name__ == "__main__"):

    msg = "1100"
    key = "0110"

    cipher_text = encrypt(msg,key)
    print(f"{msg=}\n{key=}\n{cipher_text=}")

    assert msg == decrypt(cipher_text,key)