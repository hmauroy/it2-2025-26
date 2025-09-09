import numpy as np
import matplotlib.pyplot as plt

def create_dct_basis_function(u, v, N=8):
    """
    Create a single 2D DCT basis function for frequencies (u,v).
    
    Args:
        u, v: frequency indices (0 to N-1)
        N: block size (8 for JPEG)
    
    Returns:
        N×N numpy array representing the basis function
    """
    basis = np.zeros((N, N), dtype=np.float32)
    
    # Normalization factors - crucial for orthogonality
    cu = 1.0 / np.sqrt(2) if u == 0 else 1.0
    cv = 1.0 / np.sqrt(2) if v == 0 else 1.0
    
    for x in range(N):
        for y in range(N):
            cos_u = np.cos((2*x + 1) * u * np.pi / (2*N))
            cos_v = np.cos((2*y + 1) * v * np.pi / (2*N))
            basis[x, y] = (2.0 / N) * cu * cv * cos_u * cos_v
    
    return basis

def compute_inner_product(func1, func2):
    """
    Compute the inner product (dot product) of two 2D functions.
    This is the sum of element-wise multiplication.
    
    For orthogonal functions, this should be 0 when func1 ≠ func2
    and 1 when func1 == func2 (if normalized).
    """
    return np.sum(func1 * func2)

def demonstrate_orthogonality():
    """
    Demonstrate the orthogonality of DCT basis functions.
    """
    print("DCT BASIS FUNCTIONS ORTHOGONALITY DEMONSTRATION")
    print("=" * 60)
    
    N = 8  # 8x8 blocks
    
    # Generate all 64 basis functions
    basis_functions = {}
    for u in range(N):
        for v in range(N):
            basis_functions[(u, v)] = create_dct_basis_function(u, v, N)
    
    print("1. WHAT IS ORTHOGONALITY?")
    print("-" * 30)
    print("Two functions f and g are orthogonal if their inner product is zero:")
    print("⟨f, g⟩ = ∫f(x,y) × g(x,y) dx dy = 0  (continuous case)")
    print("⟨f, g⟩ = Σf[i,j] × g[i,j]           (discrete case)")
    print()
    
    # Test orthogonality between different basis functions
    print("2. TESTING ORTHOGONALITY")
    print("-" * 30)
    
    # Test a few specific pairs
    test_pairs = [
        ((0, 0), (0, 1)),  # DC vs horizontal frequency
        ((0, 0), (1, 0)),  # DC vs vertical frequency  
        ((1, 0), (0, 1)),  # Horizontal vs vertical
        ((1, 1), (2, 3)),  # Two different diagonal frequencies
        ((0, 0), (0, 0)),  # Same function with itself (should be 1)
    ]
    
    for (u1, v1), (u2, v2) in test_pairs:
        func1 = basis_functions[(u1, v1)]
        func2 = basis_functions[(u2, v2)]
        inner_product = compute_inner_product(func1, func2)
        
        if (u1, v1) == (u2, v2):
            print(f"⟨basis({u1},{v1}), basis({u2},{v2})⟩ = {inner_product:.6f} ← Same function (should be 1)")
        else:
            print(f"⟨basis({u1},{v1}), basis({u2},{v2})⟩ = {inner_product:.6f} ← Different functions (should be 0)")
    
    print()
    
    # Compute the full orthogonality matrix
    print("3. FULL ORTHOGONALITY MATRIX")
    print("-" * 30)
    print("Computing inner products between ALL pairs of basis functions...")
    
    orthogonality_matrix = np.zeros((64, 64))
    basis_list = []
    labels = []
    
    # Create flattened list of all basis functions for easier indexing
    idx = 0
    for u in range(N):
        for v in range(N):
            basis_list.append(basis_functions[(u, v)].flatten())
            labels.append(f"({u},{v})")
            idx += 1
    
    # Compute all pairwise inner products
    for i in range(64):
        for j in range(64):
            orthogonality_matrix[i, j] = np.dot(basis_list[i], basis_list[j])
    
    print(f"Max off-diagonal value: {np.max(np.abs(orthogonality_matrix - np.eye(64))):.2e}")
    print("(This should be very close to zero for perfect orthogonality)")
    print()
    
    return orthogonality_matrix, labels

def visualize_orthogonality(orthogonality_matrix, labels):
    """
    Create visualizations to show orthogonality properties.
    """
    # Create a heatmap of the orthogonality matrix
    plt.figure(figsize=(12, 10))
    
    # Show the full matrix
    plt.subplot(2, 2, 1)
    im = plt.imshow(orthogonality_matrix, cmap='RdBu', vmin=-0.1, vmax=1.1)
    plt.title('Full Orthogonality Matrix\n(White = 1, Blue = 0)', fontsize=12)
    plt.colorbar(im)
    
    # Show a zoomed section (first 16x16)
    plt.subplot(2, 2, 2)
    im2 = plt.imshow(orthogonality_matrix[:16, :16], cmap='RdBu', vmin=-0.1, vmax=1.1)
    plt.title('Zoomed View (First 16×16)', fontsize=12)
    plt.colorbar(im2)
    
    # Show some example basis functions
    plt.subplot(2, 2, 3)
    basis_examples = [
        create_dct_basis_function(0, 0),  # DC component
        create_dct_basis_function(0, 1),  # Low horizontal frequency
        create_dct_basis_function(1, 0),  # Low vertical frequency
        create_dct_basis_function(1, 1),  # Low diagonal frequency
    ]
    
    # Combine basis functions for visualization
    combined = np.hstack([
        np.vstack([basis_examples[0], basis_examples[2]]),
        np.vstack([basis_examples[1], basis_examples[3]])
    ])
    
    plt.imshow(combined, cmap='RdBu', vmin=-0.5, vmax=0.5)
    plt.title('Example Basis Functions\nDC(0,0), H(0,1), V(1,0), D(1,1)', fontsize=12)
    plt.xticks([])
    plt.yticks([])
    
    # Show histogram of off-diagonal values
    plt.subplot(2, 2, 4)
    off_diagonal = orthogonality_matrix[~np.eye(64, dtype=bool)]
    plt.hist(off_diagonal, bins=50, alpha=0.7, color='blue')
    plt.axvline(x=0, color='red', linestyle='--', label='Perfect Orthogonality')
    plt.title('Distribution of Off-Diagonal Values', fontsize=12)
    plt.xlabel('Inner Product Value')
    plt.ylabel('Count')
    plt.legend()
    plt.yscale('log')
    
    plt.tight_layout()
    plt.show()

def demonstrate_why_orthogonality_matters():
    """
    Show why orthogonality is crucial for the DCT to work properly.
    """
    print("\n4. WHY ORTHOGONALITY MATTERS")
    print("-" * 30)
    
    # Create a simple test signal
    test_block = np.zeros((8, 8))
    test_block[2:6, 2:6] = 100  # A square in the middle
    test_block = test_block - 128  # Shift to JPEG range
    
    print("Test signal: 4×4 square in center of 8×8 block")
    print(test_block.astype(int))
    print()
    
    # Compute DCT coefficients manually using basis functions
    N = 8
    coefficients = np.zeros((N, N))
    
    print("Computing DCT coefficients as inner products with basis functions:")
    
    for u in range(N):
        for v in range(N):
            basis_func = create_dct_basis_function(u, v, N)
            # The coefficient is the inner product of signal with basis function
            coefficients[u, v] = compute_inner_product(test_block, basis_func)
            
            if u < 3 and v < 3:  # Show first few coefficients
                print(f"Coefficient ({u},{v}) = ⟨signal, basis({u},{v})⟩ = {coefficients[u, v]:.2f}")
    
    print("\nFull DCT coefficient matrix:")
    print(coefficients.astype(int))
    print()
    
    # Reconstruct the signal using only these coefficients
    reconstructed = np.zeros((N, N))
    
    for u in range(N):
        for v in range(N):
            basis_func = create_dct_basis_function(u, v, N)
            # Each basis function contributes its coefficient amount
            reconstructed += coefficients[u, v] * basis_func
    
    print("Reconstructed signal (should match original):")
    print(reconstructed.astype(int))
    print()
    
    reconstruction_error = np.max(np.abs(test_block - reconstructed))
    print(f"Maximum reconstruction error: {reconstruction_error:.2e}")
    print("(This should be essentially zero due to orthogonality!)")
    
    return test_block, coefficients, reconstructed

if __name__ == "__main__":
    # Run the demonstrations
    orthogonality_matrix, labels = demonstrate_orthogonality()
    
    # Show why orthogonality matters
    test_signal, coeffs, reconstructed = demonstrate_why_orthogonality_matters()
    
    # Create visualizations
    print("\nGenerating visualizations...")
    visualize_orthogonality(orthogonality_matrix, labels)