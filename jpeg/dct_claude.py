import numpy as np
import matplotlib.pyplot as plt

def dct_2d(block):
    """
    Compute 2D Discrete Cosine Transform on an 8x8 block.
    
    The DCT transforms spatial domain data into frequency domain.
    In JPEG, this helps concentrate energy in low-frequency components,
    making compression more effective.
    
    Args:
        block: 8x8 numpy array of pixel values (typically 0-255, shifted to -128 to 127)
    
    Returns:
        8x8 numpy array of DCT coefficients
    """
    N = 8  # Block size for JPEG
    dct_block = np.zeros((N, N), dtype=np.float32)
    
    # Apply 2D DCT formula
    for u in range(N):
        for v in range(N):
            # Calculate normalization factors
            # C(0) = 1/sqrt(2), C(k) = 1 for k > 0
            cu = 1.0 / np.sqrt(2) if u == 0 else 1.0
            cv = 1.0 / np.sqrt(2) if v == 0 else 1.0
            
            # Initialize sum for this frequency component
            sum_val = 0.0
            
            # Sum over all spatial positions
            for x in range(N):
                for y in range(N):
                    # Core DCT calculation: multiply pixel value by cosine basis functions
                    cos_u = np.cos((2*x + 1) * u * np.pi / (2*N))
                    cos_v = np.cos((2*y + 1) * v * np.pi / (2*N))
                    sum_val += block[x, y] * cos_u * cos_v
            
            # Apply normalization and scaling factor
            dct_block[u, v] = (2.0 / N) * cu * cv * sum_val
    
    return dct_block

def idct_2d(dct_block):
    """
    Compute 2D Inverse Discrete Cosine Transform.
    
    Converts frequency domain coefficients back to spatial domain.
    This is used in JPEG decompression.
    
    Args:
        dct_block: 8x8 numpy array of DCT coefficients
    
    Returns:
        8x8 numpy array of reconstructed pixel values
    """
    N = 8
    block = np.zeros((N, N), dtype=np.float32)
    
    # Apply 2D IDCT formula
    for x in range(N):
        for y in range(N):
            sum_val = 0.0
            
            # Sum over all frequency components
            for u in range(N):
                for v in range(N):
                    # Calculate normalization factors
                    cu = 1.0 / np.sqrt(2) if u == 0 else 1.0
                    cv = 1.0 / np.sqrt(2) if v == 0 else 1.0
                    
                    # Core IDCT calculation
                    cos_u = np.cos((2*x + 1) * u * np.pi / (2*N))
                    cos_v = np.cos((2*y + 1) * v * np.pi / (2*N))
                    sum_val += cu * cv * dct_block[u, v] * cos_u * cos_v
            
            # Apply scaling factor
            block[x, y] = (2.0 / N) * sum_val
    
    return block

def quantize(dct_block, q_table):
    """
    Quantize DCT coefficients using a quantization table.
    
    This is where lossy compression happens in JPEG.
    Higher frequency components are quantized more heavily,
    reducing file size at the cost of some quality loss.
    
    Args:
        dct_block: 8x8 array of DCT coefficients
        q_table: 8x8 quantization table
    
    Returns:
        8x8 array of quantized coefficients
    """
    return np.round(dct_block / q_table)

def dequantize(quantized_block, q_table):
    """
    Reverse quantization by multiplying with quantization table.
    
    Args:
        quantized_block: 8x8 array of quantized coefficients
        q_table: 8x8 quantization table
    
    Returns:
        8x8 array of dequantized DCT coefficients
    """
    return quantized_block * q_table

# Standard JPEG luminance quantization table
JPEG_QUANT_TABLE = np.array([
    [16, 11, 10, 16,  24,  40,  51,  61],
    [12, 12, 14, 19,  26,  58,  60,  55],
    [14, 13, 16, 24,  40,  57,  69,  56],
    [14, 17, 22, 29,  51,  87,  80,  62],
    [18, 22, 37, 56,  68, 109, 103,  77],
    [24, 35, 55, 64,  81, 104, 113,  92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103,  99]
], dtype=np.float32)

def demonstrate_jpeg_dct():
    """
    Demonstrate the complete JPEG DCT process with a sample 8x8 block.
    """
    print("JPEG DCT Compression Demo")
    print("=" * 50)
    
    # Create a sample 8x8 block with some pattern
    # In real JPEG, pixel values are shifted from [0,255] to [-128,127]
    original_block = np.array([
        [150, 155, 160, 165, 170, 175, 180, 185],
        [145, 150, 155, 160, 165, 170, 175, 180],
        [140, 145, 150, 155, 160, 165, 170, 175],
        [135, 140, 145, 150, 155, 160, 165, 170],
        [130, 135, 140, 145, 150, 155, 160, 165],
        [125, 130, 135, 140, 145, 150, 155, 160],
        [120, 125, 130, 135, 140, 145, 150, 155],
        [115, 120, 125, 130, 135, 140, 145, 150]
    ], dtype=np.float32)
    
    # Shift to center around zero (JPEG preprocessing step)
    shifted_block = original_block - 128
    
    print("Original 8x8 block (shifted to [-128,127]):")
    print(shifted_block.astype(int))
    print()
    
    # Step 1: Apply forward DCT
    dct_coeffs = dct_2d(shifted_block)
    print("DCT coefficients:")
    print(dct_coeffs.astype(int))
    print()
    
    # Step 2: Quantization (lossy compression step)
    quantized = quantize(dct_coeffs, JPEG_QUANT_TABLE)
    print("Quantized coefficients:")
    print(quantized.astype(int))
    print()
    
    # Step 3: Dequantization (decompression starts here)
    dequantized = dequantize(quantized, JPEG_QUANT_TABLE)
    print("Dequantized coefficients:")
    print(dequantized.astype(int))
    print()
    
    # Step 4: Apply inverse DCT
    reconstructed_shifted = idct_2d(dequantized)
    
    # Shift back to [0,255] range
    reconstructed_block = reconstructed_shifted + 128
    
    print("Reconstructed block:")
    print(reconstructed_block.astype(int))
    print()
    
    # Calculate compression metrics
    mse = np.mean((original_block - reconstructed_block) ** 2)
    print(f"Mean Squared Error: {mse:.2f}")
    
    # Count non-zero coefficients (relates to compression ratio)
    non_zero_coeffs = np.count_nonzero(quantized)
    compression_info = f"Non-zero coefficients: {non_zero_coeffs}/64 ({non_zero_coeffs/64*100:.1f}%)"
    print(compression_info)

def visualize_dct_basis():
    """
    Visualize the 2D DCT basis functions to understand what the transform does.
    """
    fig, axes = plt.subplots(8, 8, figsize=(12, 12))
    fig.suptitle('2D DCT Basis Functions (8x8)', fontsize=16)
    
    N = 8
    for u in range(N):
        for v in range(N):
            # Create basis function for frequency (u,v)
            basis = np.zeros((N, N))
            cu = 1.0 / np.sqrt(2) if u == 0 else 1.0
            cv = 1.0 / np.sqrt(2) if v == 0 else 1.0
            
            for x in range(N):
                for y in range(N):
                    cos_u = np.cos((2*x + 1) * u * np.pi / (2*N))
                    cos_v = np.cos((2*y + 1) * v * np.pi / (2*N))
                    basis[x, y] = (2.0 / N) * cu * cv * cos_u * cos_v
            
            # Plot basis function
            im = axes[u, v].imshow(basis, cmap='RdBu', vmin=-0.5, vmax=0.5)
            axes[u, v].set_title(f'({u},{v})', fontsize=8)
            axes[u, v].set_xticks([])
            axes[u, v].set_yticks([])
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Run the demonstration
    demonstrate_jpeg_dct()
    
    # Uncomment to visualize DCT basis functions
    # visualize_dct_basis()