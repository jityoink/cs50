def bulbs():
    while True:
        msg = input("message: ")
        check = 0
        lightbulb = {
            "0" : "⚫",
            "1" : "🟡"
        }
        for x in range(len(msg)):
            if int(ord(msg[x])) > 255:
                check = check + 1
        if check == 0:
            for x in range(0,len(msg)):
                a = bin(ord(msg[x]))[2:]
                a = ("0" * (8-len(str(a)))) + str(a)
                b = ""
                for x in range(len(a)):
                    b += lightbulb[a[x]]
                print(b)
            break
        else:
            print("please enter standard ascii characters only")

bulbs()