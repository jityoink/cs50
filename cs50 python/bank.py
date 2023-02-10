def main():
    greeting = input("*customer walks into the store*")
    if "hello" == greeting[:5].lower().strip():
        print("no money for you")
    elif greeting[0].lower == "h":
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()