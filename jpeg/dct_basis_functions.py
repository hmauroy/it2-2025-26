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
    # C(0) = 1/√2, C(k) = 1 for k > 0
    cu = 1.0 / np.sqrt(2) if u == 0 else 1.0
    cv = 1.0 / np.sqrt(2) if v == 0 else 1.0
    
    for x in range(N):
        for y in range(N):
            # DCT basis function formula
            cos_u = np.cos((2*x + 1) * u * np.pi / (2*N))
            cos_v = np.cos((2*y + 1) * v * np.pi / (2*N))
            basis[x, y] = (2.0 / N) * cu * cv * cos_u * cos_v
    
    return basis

def display_all_basis_functions():
    """
    Calculate and display all 64 DCT basis functions in an 8x8 grid.
    """
    N = 8  # Block size
    
    # Create figure with subplots arranged in 8x8 grid
    fig, axes = plt.subplots(N, N, figsize=(16, 16))
    fig.suptitle('All 64 DCT Basis Functions (8×8 Grid)\n' + 
                 'Frequency increases left→right (horizontal) and top→bottom (vertical)', 
                 fontsize=16, y=0.95)
    
    # Calculate and display each basis function
    for u in range(N):
        for v in range(N):
            # Create the basis function
            basis_func = create_dct_basis_function(u, v, N)
            
            # Display in the corresponding subplot
            im = axes[u, v].imshow(basis_func, cmap='RdBu_r', 
                                  vmin=-0.5, vmax=0.5, interpolation='nearest')
            
            # Add title with frequency indices
            axes[u, v].set_title(f'({u},{v})', fontsize=10, pad=5)
            
            # Remove axis ticks for cleaner look
            axes[u, v].set_xticks([])
            axes[u, v].set_yticks([])
            
            # Add subtle grid lines to show the 8x8 structure
            axes[u, v].set_xticks(np.arange(-0.5, 8, 1), minor=True)
            axes[u, v].set_yticks(np.arange(-0.5, 8, 1), minor=True)
            axes[u, v].grid(which='minor', color='gray', linestyle='-', linewidth=0.5, alpha=0.3)
    
    # Add a colorbar to show the scale
    fig.colorbar(im, ax=axes, shrink=0.8, aspect=30, 
                 label='Amplitude (Red=Positive, Blue=Negative)')
    
    # Add explanatory text
    plt.figtext(0.02, 0.02, 
                'Key Observations:\n' +
                '• (0,0): DC component - constant value (average brightness)\n' +
                '• Top row: Horizontal frequencies only\n' +
                '• Left column: Vertical frequencies only\n' +
                '• Diagonal: Mixed horizontal and vertical frequencies\n' +
                '• Higher indices = higher spatial frequencies = finer details',
                fontsize=10, verticalalignment='bottom',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.tight_layout()
    plt.show()

def display_basis_functions_detailed():
    """
    Display basis functions with more detailed analysis.
    """
    N = 8
    
    # Create a larger figure for detailed view
    fig = plt.figure(figsize=(20, 16))
    
    # Main 8x8 grid of basis functions
    main_grid = plt.subplot2grid((10, 10), (0, 0), colspan=8, rowspan=8)
    
    # Calculate all basis functions and arrange in a single large image
    full_image = np.zeros((N * 8, N * 8))
    
    for u in range(N):
        for v in range(N):
            basis_func = create_dct_basis_function(u, v, N)
            
            # Place each 8x8 basis function in the appropriate position
            row_start = u * N
            row_end = (u + 1) * N
            col_start = v * N
            col_end = (v + 1) * N
            
            full_image[row_start:row_end, col_start:col_end] = basis_func
    
    # Display the complete grid
    im = main_grid.imshow(full_image, cmap='Blues', vmin=-0.5, vmax=0.5)
    main_grid.set_title('All 64 DCT Basis Functions', fontsize=16, pad=20)
    
    # Add grid lines to separate each 8x8 block
    for i in range(1, N):
        main_grid.axhline(y=i*N - 0.5, color='black', linewidth=2)
        main_grid.axvline(x=i*N - 0.5, color='black', linewidth=2)
    
    # Add frequency labels
    main_grid.set_xticks(np.arange(N) * N + N//2 - 0.5)
    main_grid.set_yticks(np.arange(N) * N + N//2 - 0.5)
    main_grid.set_xticklabels([f'v={i}' for i in range(N)])
    main_grid.set_yticklabels([f'u={i}' for i in range(N)])
    main_grid.set_xlabel('Horizontal Frequency Index (v)', fontsize=12)
    main_grid.set_ylabel('Vertical Frequency Index (u)', fontsize=12)
    
    # Add colorbar
    cbar = plt.colorbar(im, ax=main_grid, shrink=0.8)
    cbar.set_label('Amplitude', fontsize=12)
    
    # Add some highlighted examples in smaller subplots
    examples = [(0, 0), (0, 3), (3, 0), (3, 3), (7, 7)]
    example_names = ['DC\n(0,0)', 'Low Horiz.\n(0,3)', 'Low Vert.\n(3,0)', 
                    'Mixed\n(3,3)', 'High Freq.\n(7,7)']
    
    for i, ((u, v), name) in enumerate(zip(examples, example_names)):
        ax = plt.subplot2grid((10, 10), (8, i*2), colspan=2, rowspan=2)
        basis_func = create_dct_basis_function(u, v, N)
        ax.imshow(basis_func, cmap='Blues', vmin=-0.5, vmax=0.5)
        ax.set_title(name, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
    
    plt.tight_layout()
    plt.show()

def analyze_frequency_content():
    """
    Analyze and visualize the frequency content progression.
    """
    N = 8
    
    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    fig.suptitle('DCT Basis Functions: Frequency Content Analysis', fontsize=16)
    
    # Show progression of horizontal frequencies (v increasing, u=0)
    for v in range(4):
        basis_func = create_dct_basis_function(0, v, N)
        axes[0, v].imshow(basis_func, cmap='RdBu_r', vmin=-0.5, vmax=0.5)
        axes[0, v].set_title(f'Horizontal Only\n(u=0, v={v})', fontsize=12)
        axes[0, v].set_xticks([])
        axes[0, v].set_yticks([])
    
    # Show progression of vertical frequencies (u increasing, v=0)  
    for u in range(4):
        basis_func = create_dct_basis_function(u, 0, N)
        axes[1, u].imshow(basis_func, cmap='RdBu_r', vmin=-0.5, vmax=0.5)
        axes[1, u].set_title(f'Vertical Only\n(u={u}, v=0)', fontsize=12)
        axes[1, u].set_xticks([])
        axes[1, u].set_yticks([])
    
    plt.tight_layout()
    plt.show()

def print_basis_function_values():
    """
    Print the actual numerical values for a few basis functions.
    """
    print("NUMERICAL VALUES OF SELECTED BASIS FUNCTIONS")
    print("=" * 60)
    
    examples = [(0, 0), (0, 1), (1, 0), (1, 1)]
    names = ["DC Component", "1st Horizontal Freq", "1st Vertical Freq", "1st Diagonal Freq"]
    
    for (u, v), name in zip(examples, names):
        print(f"\n{name} - Basis Function ({u},{v}):")
        print("-" * 40)
        basis_func = create_dct_basis_function(u, v, 8)
        
        # Print with nice formatting
        for row in basis_func:
            print([f"{val:6.3f}" for val in row])

if __name__ == "__main__":
    print("Generating DCT Basis Functions Visualization...")
    print("This will create three different visualizations:")
    print("1. Standard 8x8 grid of all basis functions")
    print("2. Detailed analysis view")
    print("3. Frequency content progression")
    print()
    
    # Display all basis functions in 8x8 grid
    #display_all_basis_functions()
    
    # Display detailed analysis
    display_basis_functions_detailed()
    
    # Show frequency content analysis
    #analyze_frequency_content()
    
    # Print some numerical values
    #print_basis_function_values()
    
    print("\nVisualization complete! Key takeaways:")
    print("• Each basis function represents a different spatial frequency pattern")
    print("• (0,0) is the DC component - uniform brightness")
    print("• Moving right increases horizontal frequency")
    print("• Moving down increases vertical frequency") 
    print("• Bottom-right corner has the highest frequencies (finest details)")