def substitution():
    while True:
        plaintext = input("plaintext: ")
        key = input("key: ")
        check = 0
        cipher = set({})
        for x in range(0,len(key)):
            cipher.add(key[x])
        if len(cipher) != 26 or ord(key[x]) not in [*range(65,91),*range(97,123)]:
            check = check + 1
        if len(key) == 26 and check == 0:
            keylookup = dict()
            ascii = [*range(65,91),*range(97,123)]
            a_list = []
            for x in range(52):
                a_list += chr(ascii[x])
            for x in range(0,26):
                keylookup.update({a_list[x]:key[x].upper()})
                keylookup.update({a_list[x+26]:key[x].lower()})
            ciphertext = ""
            for x in range(len(plaintext)):
                if ord(plaintext[x]) in [*range(65,91),*range(97,123)]:
                    ciphertext += keylookup[plaintext[x]]
                else:
                    ciphertext += plaintext[x]
            print(f"ciphertext: {ciphertext}")
            break
        else:
            print("enter 26 unique letters in the key")

substitution()