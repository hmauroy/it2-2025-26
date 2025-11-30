import qrcode
from PIL import Image
import numpy as np

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
    
    # Convert the encoded text to 8-bit binary data
    def convert_to_8bit(data):
        return ''.join(format(ord(char), '08b') for char in data)

    encoded_text = convert_to_8bit(text)

    # Get the QR code matrix (before masking is applied during image generation)
    # The matrix is stored in qr.modules after qr.make() is called
    matrix = qr.modules
    
    img = qr.make_image(fill_color="black", back_color="white")

    return encoded_text, img, matrix, qr

# Function to display the QR code matrix
def display_matrix(matrix):
    print("\nQR Code Matrix (1 = black/filled, 0/None = white/empty):")
    print("=" * 60)
    
    if matrix is None:
        print("Matrix is None")
        return
    
    # Convert to numpy array for easier viewing
    size = len(matrix)
    print(f"Matrix size: {size}x{size}")
    print()
    
    # Display as visual representation
    for row in matrix:
        row_str = ""
        for cell in row:
            if cell is None:
                row_str += "░"  # Empty/white
            elif cell:
                row_str += "█"  # Filled/black
            else:
                row_str += "░"  # Empty/white
        print(row_str)
    
    print("\n" + "=" * 60)
    
    # Display as numeric matrix
    print("\nNumeric representation (first 10 rows):")
    for i, row in enumerate(matrix[:10]):
        row_values = []
        for cell in row:
            if cell is None:
                row_values.append("N")
            elif cell:
                row_values.append("1")
            else:
                row_values.append("0")
        print(f"Row {i:2d}: {' '.join(row_values)}")
    
    if len(matrix) > 10:
        print("... (remaining rows omitted)")

# Function to extract data region (excluding finder patterns and timing)
def analyze_qr_structure(matrix, qr):
    size = len(matrix)
    print(f"\n\nQR Code Structure Analysis:")
    print(f"Version: {version}")
    print(f"Size: {size}x{size}")
    print(f"Error Correction: L (Low - 7% recovery)")
    
    # Access the mask pattern used
    if hasattr(qr, 'mask_pattern'):
        print(f"Mask Pattern: {qr.mask_pattern}")
    else:
        print("Mask Pattern: Not found in qr object")
    
    # Try to access other QR attributes
    print("\nQR Object Attributes:")
    for attr in dir(qr):
        if not attr.startswith('_'):
            try:
                value = getattr(qr, attr)
                if not callable(value):
                    print(f"  {attr}: {value}")
            except:
                pass
    
    # Find finder patterns (top-left, top-right, bottom-left)
    print("\nFinder Patterns located at:")
    print("  - Top-left: (0,0)")
    print(f"  - Top-right: (0,{size-7})")
    print(f"  - Bottom-left: ({size-7},0)")
    
    # Timing patterns
    print("\nTiming Patterns:")
    print(f"  - Horizontal: row 6")
    print(f"  - Vertical: column 6")

# Example usage
text_data = "HEI IT2!"
encoded_text, img, matrix, qr = generate_qr_code(text_data)

print("Input Text:", text_data)
print("Encoded Text (binary):", encoded_text)
print("Binary length:", len(encoded_text), "bits")

# Display the matrix
display_matrix(matrix)

# Analyze structure
analyze_qr_structure(matrix, qr)

# Show the image
img.show()

# Optional: Save matrix to file
def save_matrix_to_file(matrix, filename="qr_matrix.txt"):
    with open(filename, 'w') as f:
        for row in matrix:
            row_str = ""
            for cell in row:
                if cell is None:
                    row_str += "N"
                elif cell:
                    row_str += "1"
                else:
                    row_str += "0"
            f.write(row_str + "\n")
    print(f"\nMatrix saved to {filename}")

save_matrix_to_file(matrix)