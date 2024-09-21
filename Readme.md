
# Cryptic Canvas

A simple Python-based tool for encrypting and decrypting images using a user-provided key. This tool allows you to protect your images by encrypting them and later decrypting them with the same key.

### s4f3s4f4r1 
Developer of this image encryption/decryption tool.
## Overview

The Cryptic Canvas tool provides a simple way to encrypt and decrypt image files. Using a user-defined integer key, the tool modifies the pixel values of an image during encryption, and with the same key, the image can be restored to its original form.

## Features

- **Encrypt Images**: Secure your images by encrypting them with a key.
- **Decrypt Images**: Restore the original image by decrypting it with the same key used for encryption.
- **Key-Based Encryption**: Uses an integer key provided by the user for the encryption and decryption process.

## How to Use

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```bash
    cd <project-directory>
    ```

3. Run the Cryptic Canvas script with `python3`:

    ```bash
    python3 Task_02_Cryptic.py
    ```

4. You will be prompted to choose between encryption (`e`) or decryption (`d`). Enter your choice.

    ```plaintext
    Choose 'e' for encryption or 'd' for decryption: e
    ```

5. Provide the path to the image you want to encrypt or decrypt:

    ```plaintext
    Enter the image path: sample.png
    ```

6. Enter the key (integer value) that will be used for encryption or decryption:

    ```plaintext
    Enter the key (integer value): 123456
    ```

7. The encrypted or decrypted image will be saved with a new filename.

    - For encryption, the encrypted image will be saved as `encrypted_<image_name>.png`.
    - For decryption, the decrypted image will be saved as `decrypted_<image_name>.png`.

## Sample Usage

### Encryption Example

```plaintext
Choose 'e' for encryption or 'd' for decryption: e
Enter the image path: sample.png
Enter the key (integer value): 123456
Encrypted image saved as encrypted_sample.png
