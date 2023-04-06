def main():
    option = 0
    while option !=3:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 1:
            password = int(input("Please enter your password to encode: "))
            i = 0
            encode = ""
            while i<len(str(password)):
                encode = encode + str(int(str(password)[i:i+1])+3)
                i+=1
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            print('The encoded password is',encode,end = "")
            print(", and the original password is",password, end = ".\n")

if __name__ == "__main__":
    main()