def cc_ver():
    while True:
        cc_no = input("enter credit card number: ")
        sum = 0
        cclength = len(cc_no)
        if len(cc_no) in [13,15,16]:
            for x in range(0,cclength,2):
                a = str(2 * int(cc_no[x]))
                try:
                    for y in range(0,2):
                        sum = sum + int(a[y])
                except IndexError:
                    continue
            for x in range(1,cclength,2):
                sum = sum + int(cc_no[x])
            if sum%10 == 0:
                print("valid credit card")
                if cc_no[0:2] in ["34","37"]:
                    print("AMEX")
                    break
                elif cc_no[0:2] in ["51","52","53","54","55"]:
                    print("Mastercard")
                    break
                elif cc_no[0] in ["4"]:
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

cc_ver()