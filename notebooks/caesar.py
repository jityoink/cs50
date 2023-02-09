def caesar():
    while True:
        plaintext = input("plaintext: ")
        check = 0
        key = input("input key: ")
        try:
            key = int(key)
            for x in range(len(plaintext)):
                if ord(plaintext[x]) not in [*range(65,91),*range(97,123)]:
                    check = check + 1
            if check == 0:
                ciphertext = ""
                for x in range(len(plaintext)):
                    if ord(plaintext[x]) in [*range(65,91)]:
                        ciphertext += chr(64 + (ord(plaintext[x]) - 64 + key)%26)
                    elif ord(plaintext[x]) in [*range(97,123)]:
                        ciphertext += chr(97 + (ord(plaintext[x]) - 97 + key)%26)
                print(ciphertext)
                break
            else:
                print("use only uppercase/lowercase")
        except ValueError:
            print("enter a number for the key")

caesar()