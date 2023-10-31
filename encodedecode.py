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


def decode(encoded_password):
    new_string = ''
    for i in encoded_password:
        if i == '3':
            new_string += '0'
        elif i == '4':
            new_string += '1'
        elif i == '5':
            new_string += '2'
        elif i == '6':
            new_string += '3'
        elif i == '7':
            new_string += '4'
        elif i == '8':
            new_string += '5'
        elif i == '9':
            new_string += '6'
        elif i == '0':
            new_string += '7'
        elif i == '1':
            new_string += '8'
        elif i == '2':
            new_string += '9'
        else:
            new_string += str(i)
    return new_string

if __name__ == "__main__":
    main()
