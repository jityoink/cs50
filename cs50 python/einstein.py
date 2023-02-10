def main():
    try:
        energy = int(input("mass (in kg): ")) * 300000000**2
        print(f"energy = {energy}")
    
    except ValueError:
        print("give a number pls")

if __name__ == "__main__":
    main()