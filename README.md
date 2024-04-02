# Summary:
## Encryption Function (encrypt_image()):

This function takes an image file path and a key as input.
It opens the image, iterates over each pixel, and performs a basic mathematical operation (XOR) on each pixel's RGB values with the provided key.
The result is an encrypted image where each pixel's color values are modified based on the key.
The encrypted image is saved to a file.
## Decryption Function (decrypt_image()):

This function takes an encrypted image file path and the same key used for encryption as input.
It opens the encrypted image, iterates over each pixel, and applies the reverse operation (XOR) to each pixel's RGB values using the provided key.
The result is a decrypted image that restores the original pixel values.
The decrypted image is saved to a file.
## Example Usage:

In the example usage section, you specify the path to the original image file (image_path) and the encryption key (key).
The script encrypts the original image, saves the encrypted image, decrypts the encrypted image, and saves the decrypted image.
You need to replace "original_image.png" with the actual path to your image file and choose a suitable key value for encryption.

# Implementation Example:
This implementation encrypts and decrypts an image using a basic XOR operation with a given key. You can copy and run this code after replacing "original_image.png" with the path to your image file and choosing an appropriate key value. After execution, you'll get two images: encrypted_image.png and decrypted_image.png.
