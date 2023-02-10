def main():
    math = input("math here: ").replace(" ","")
    if "+" in math:
        a = math.split("+")
        for x in range(len(a)):
            a[x] = float(a[x])
        print(round(a[0]+a[1],1))
    if "-" in math:
        a = math.split("-")
        for x in range(len(a)):
            a[x] = float(a[x])
        print(round(a[0]-a[1],1))
    if "*" in math:
        a = math.split("*")
        for x in range(len(a)):
            a[x] = float(a[x])
        print(round(a[0]*a[1],1))
    if "/" in math:
        a = math.split("/")
        for x in range(len(a)):
            a[x] = float(a[x])
        print(round(a[0]/a[1],1))

if __name__ == "__main__":
    main()