print("   ____                  _   _         ____                           ")
print("  / ___|_ __ _   _ _ __ | |_(_) ___   / ___|__ _ _ ____   ____ _ ___  ")
print(" | |   | '__| | | | '_ \| __| |/ __| | |   / _` | '_ \ \ / / _` / __| ")
print(" | |___| |  | |_| | |_) | |_| | (__  | |__| (_| | | | \ V / (_| \__ \ ")
print("  \____|_|   \__, | .__/ \__|_|\___|  \____\__,_|_| |_|\_/ \__,_|___/ ")
print("             |___/|_|                                                 ")
print("                                                                      ")
print("     By s4f3s4f4r1                                                    ")
from PIL import Image
import os

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    img = img.convert('RGB')  # Ensure the image is in RGB format
    pixels = img.load()  # Access the pixel data

    # Get the width and height of the image
    width, height = img.size

    # Perform encryption by modifying pixel values
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Encrypt each pixel using the key (simple XOR operation)
            pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    # Save the encrypted image with a new name
    encrypted_image_path = f"encrypted_{os.path.basename(image_path)}"
    img.save(encrypted_image_path)
    print(f"Encrypted image saved as {encrypted_image_path}")


def decrypt_image(image_path, key):
    # Open the encrypted image
    img = Image.open(image_path)
    img = img.convert('RGB')  # Ensure the image is in RGB format
    pixels = img.load()  # Access the pixel data

    # Get the width and height of the image
    width, height = img.size

    # Perform decryption by reverting the encryption process
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Decrypt each pixel using the key (reversing the XOR operation)
            pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    # Save the decrypted image with a new name
    decrypted_image_path = f"decrypted_{os.path.basename(image_path)}"
    img.save(decrypted_image_path)
    print(f"Decrypted image saved as {decrypted_image_path}")


def main():
    # Ask user for input
    choice = input("Choose 'e' for encryption or 'd' for decryption: ").lower()

    # Get the image path from the user
    image_path = input("Enter the image path: ")

    # Check if the image exists
    if not os.path.exists(image_path):
        print("The image file does not exist. Please check the path.")
        return

    # Get the encryption/decryption key
    try:
        key = int(input("Enter the key (integer value): "))
    except ValueError:
        print("Invalid key. Please enter an integer.")
        return

    if choice == 'e':
        encrypt_image(image_path, key)
    elif choice == 'd':
        decrypt_image(image_path, key)
    else:
        print("Invalid choice. Please choose 'e' for encryption or 'd' for decryption.")

# Run the main function
if __name__ == "__main__":
    main()
