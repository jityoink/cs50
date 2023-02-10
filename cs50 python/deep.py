def main():
    answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
    if answer.lower() in [42, "forty two", "forty-two"]:
        print("Yes")
    else:
        print("no you clown")

if __name__ == "__main__":
    main()