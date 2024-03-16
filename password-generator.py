import random
import string

# password generate function 
def generate_password(length):
    #select all character include lower and upper case letters, digits, and punctuation marks

    #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'!"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~'`
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
