import qrcode
from PIL import Image
import re

# Define the error correction level and version for the QR code
error_correction = qrcode.constants.ERROR_CORRECT_L
version = 2

# Function to convert decimal numbers to binary
def convert_to_binary(decimal):
    return bin(decimal)[2:].zfill(8)  # Ensure 8-bit alignment

# Generate QR code from encoded text data
def generate_qr_code(text, mode="utf-8"):
    qr = qrcode.QRCode(
        version=version,
        error_correction=error_correction,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=False)

    print("Modules Matrix:")
    for row in qr.modules:
        print(row)
    
    print(qr.mask_pattern)
    
    

    # Convert the encoded text to 4-bit binary data
    def convert_to_8bit(data):
        return ''.join(format(ord(char), '08b') for char in data)

    encoded_text = convert_to_8bit(text)

    img = qr.make_image(fill_color="black", back_color="white")

    # Add the error correction code and the 4-bit binary data to the image
    if mode == "utf-8":
        text_mode = "text"
        data_mode = "NUL"
        version_error_correction = 1
    elif mode == "ascii":
        text_mode = "ascii"
        data_mode = "ALTO"
        version_error_correction = 3
    else:
        raise ValueError("Unsupported encoding mode")

    #img.save(f"qr_code_{text_mode}_{version_error_correction}.png", "PNG")
    return encoded_text, img

# Example usage
#text_data = input("Enter the text to encode: ")
text_data = "HEI IT2!"
encoded_text, img = generate_qr_code(text_data)

print("Encoded Text:", encoded_text)
img.show()