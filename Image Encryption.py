from PIL import Image

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size

    # Encrypt each pixel in the image
    for y in range(height):
        for x in range(width):
            # Get the RGB values of the pixel
            r, g, b = img.getpixel((x, y))
            # Apply a basic mathematical operation (XOR) to each color channel with the key
            r_encrypted = r ^ key
            g_encrypted = g ^ key
            b_encrypted = b ^ key
            # Set the encrypted pixel value in the image
            img.putpixel((x, y), (r_encrypted, g_encrypted, b_encrypted))

    # Save the encrypted image
    img.save("encrypted_image.png")
    print("Image encrypted successfully.")

def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    img = Image.open(encrypted_image_path)
    width, height = img.size

    # Decrypt each pixel in the image
    for y in range(height):
        for x in range(width):
            # Get the encrypted RGB values of the pixel
            r_encrypted, g_encrypted, b_encrypted = img.getpixel((x, y))
            # Apply the reverse operation (XOR) to each color channel with the key
            r_decrypted = r_encrypted ^ key
            g_decrypted = g_encrypted ^ key
            b_decrypted = b_encrypted ^ key
            # Set the decrypted pixel value in the image
            img.putpixel((x, y), (r_decrypted, g_decrypted, b_decrypted))

    # Save the decrypted image
    img.save("decrypted_image.png")
    print("Image decrypted successfully.")

# Example usage:
image_path = "original_image.png"  # Replace with the path to your image file
key = 123  # Example key for XOR encryption

# Encrypt the image
encrypt_image(image_path, key)

# Decrypt the encrypted image
decrypt_image("encrypted_image.png", key)