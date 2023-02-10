def main():
    file_name = input("file name: ").strip().split(".")
    if file_name[-1] in ["gif", "jpg", "jpeg", "png", "pdf", "txt", "zip"]:
        print("." + file_name[-1])
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()
