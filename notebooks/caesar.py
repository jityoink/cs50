def caesar():
    while True:
        plaintext = input("plaintext: ")
        check = 0
        key = input("input key: ")
        try:
            key = int(key)
            ciphertext = ""
            for x in range(len(plaintext)):
                if ord(plaintext[x]) in [*range(65,91)]:
                    ciphertext += chr(64 + (ord(plaintext[x]) - 64 + key)%26)
                elif ord(plaintext[x]) in [*range(97,123)]:
                    ciphertext += chr(97 + (ord(plaintext[x]) - 97 + key)%26)
                else:
                    ciphertext += plaintext[x]
            print(ciphertext)
            break
        except ValueError:
            print("enter a number for the key")

caesar()