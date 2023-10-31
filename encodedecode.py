def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        choice = input("\nPlease enter an option: ")

        if choice == '1':
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print(f"Your password has been encoded and stored!\n")

        elif choice == '2':
            if 'encoded_password' in locals():
                decoded_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.\n")
            else:
                print("No encoded password found. Please encode a password first.")

        elif choice == '3':
            break

        else:
            print("Invalid option. Please try again.")


def encode(password):
    encoder_map = {str(i): str((i + 3) % 10) for i in range(10)}
    encoded_password = ''.join([encoder_map[digit] for digit in password])
    return encoded_password




if __name__ == "__main__":
    main()
