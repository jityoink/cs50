


while True:
    try:
        height = input('Height (1 to 8 inclusive): ')
        heightint = int(height)
        if heightint >= 1 and heightint <= 8:
            for x in range(1, heightint + 1):
                c_str = (" " * (heightint-x)) + ("#" * x) + "  " + ("#" * x) + "\n"
                print(c_str)
            break
        else:
            print("Input a number from 1 to 8 inclusive")
    except ValueError:
        print("Invalid input, please try again.")
