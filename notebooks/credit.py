while True:
    cc_no = input("enter credit card number: ")
    sum = 0
    cclength = len(cc_no)
    print(len(cc_no))
    if len(cc_no) == 16 or 15 or 13:
        for x in range(0,cclength,2):
            a = str(2 * int(cc_no[x]))
            try:
                for y in range(0,2):
                    sum = sum + int(a[y])
            except IndexError:
                continue
        print(sum)
        for x in range(1,cclength,2):
            sum = sum + int(cc_no[x])
        print(sum)
        if sum%10 == 0:
            print("valid credit card")
            if cc_no[0:2] == "34" or "37":
                print("AMEX")
                break
            elif cc_no[0:2] == "51" or "52" or "53" or "54" or "55":
                print("Mastercard")
                break
            elif cc_no[0] == "4":
                print("Visa")
                break
            else:
                print("unknown credit card provider")
                break
        else:
            print("invalid credit card")
            break
    else:
        print("enter 16 characters!")