
## krypteringsverktyget med fernit ## 

import argparse
from cryptography.fernet import Fernet

# Funktion för att generera och spara en nyckel
def generate_key(key_file):
    key = Fernet.generate_key()
    with open(key_file, 'wb') as file:
        file.write(key)
    print(f"Nyckeln är sparad i {key_file}")

# Function för att kryptera en fil
def encrypt_file(key_file, input_file, output_file):
    with open(key_file, 'rb') as file:
        key = file.read()
    fernet = Fernet(key)

    with open(input_file, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)
    with open(output_file, 'wb') as file:
        file.write(encrypted)
    print(f"Filen {input_file} har krypterats till {output_file}")

# Funktion för att dekryptera en fil
def decrypt_file(key_file, input_file, output_file):
    with open(key_file, 'rb') as file:
        key = file.read()
    fernet = Fernet(key)

    with open(input_file, 'rb') as file:
        encrypted = file.read()

    decrypted = fernet.decrypt(encrypted)
    with open(output_file, 'wb') as file:
        file.write(decrypted)
    print(f"Filen {input_file} har dekrypterats till {output_file}")

# Argumentparser för att hantera kommandon
def main():
    parser = argparse.ArgumentParser(description="Krypteringsverktyg med Fernet.")
    parser.add_argument("mode", choices=["generate_key", "encrypt", "decrypt"], help="Välj en funktion att köra.")
    parser.add_argument("--key", help="Sökväg till nyckelfilen.")
    parser.add_argument("--input", help="Sökväg till input-filen.")
    parser.add_argument("--output", help="Sökväg till output-filen.")

    args = parser.parse_args()

    if args.mode == "generate_key":
        generate_key(args.key)
    elif args.mode == "encrypt":
        encrypt_file(args.key, args.input, args.output)
    elif args.mode == "decrypt":
        decrypt_file(args.key, args.input, args.output)


if __name__ == "__main__":
    main()


