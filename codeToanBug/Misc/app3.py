def main():
    print("Welcome to the File Read Challenge!")
    filename = input("Enter filename to read (must be .txt): ")

    if filename.endswith(".txt"):

        try:
            with open(f"./files/{filename}", 'r') as f:
                content = f.read()
            print(content)
        except FileNotFoundError:
            print("File not found!")
    else:
        print("Invalid file extension! Only .txt files are allowed.")

if __name__ == "__main__":
    main()