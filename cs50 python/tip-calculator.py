def main():
    while True:
        try:
            dollars = float(input("amount owed: ")[1:])
            percentage = float(input("what percentage to tip? ")[:-1])/100
            print("$" + str(round(dollars*percentage,2)))
            break
        except ValueError:
            print("give a number")
21
if __name__ == "__main__":
    main()