"""
Histogram-generator.


Author: Claude 4.5 02.12.2025
"""

import matplotlib.pyplot as plt
import numpy as np

def create_histogram(data, class_width=1, color='skyblue', 
                    edge_color='black', edge_width=1.5,
                    font_size=12, title='Histogram', 
                    xlabel='Values', ylabel='Frequency Density'):
    """
    Create a customizable histogram with frequency density (frequency/class_width).
    
    Parameters:
    -----------
    data : array-like
        The data to plot
    class_width : float
        Width of each histogram class/bin
    color : str
        Color of the bars
    edge_color : str
        Color of the bar edges
    edge_width : float
        Width of the bar edges
    font_size : int
        Font size for labels and title
    title : str
        Title of the histogram
    xlabel : str
        Label for x-axis
    ylabel : str
        Label for y-axis (frequency density)
    """
    
    # Calculate bins based on class width
    data_min = np.min(data)
    data_max = np.max(data)
    bins = np.arange(data_min, data_max + class_width, class_width)
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create histogram with density=True (frequency/class_width)
    # This makes height = frequency / class_width
    counts, edges, patches = ax.hist(data, bins=bins, density=False,
                                     color=color, edgecolor=edge_color, 
                                     linewidth=edge_width)
    
    # Calculate frequency density manually
    densities = counts / class_width
    
    # Clear the plot and redraw with density values
    ax.clear()
    
    # Create bars with density heights
    bar_positions = edges[:-1]
    ax.bar(bar_positions, densities, width=class_width, 
           align='edge', color=color, edgecolor=edge_color,
           linewidth=edge_width)
    
    # Customize fonts
    ax.set_title(title, fontsize=font_size + 2, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=font_size)
    ax.set_ylabel(ylabel, fontsize=font_size)
    ax.tick_params(labelsize=font_size - 2)
    
    # Adjust spine widths
    for spine in ax.spines.values():
        spine.set_linewidth(edge_width)
    
    # Add grid for better readability
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)
    
    plt.tight_layout()
    return fig, ax, counts, densities, edges


# Example usage
if __name__ == "__main__":
    # Generate sample data
    np.random.seed(42)
    data = np.random.normal(50, 15, 1000)
    
    # Create histogram with custom parameters
    fig, ax, counts, densities, edges = create_histogram(
        data=data,
        class_width=5,           # Adjust bin width
        color='lightcoral',       # Bar color
        edge_color='darkred',     # Edge color
        edge_width=2,             # Edge width
        font_size=14,             # Font size
        title='Distribution of Sample Data',
        xlabel='Value Range',
        ylabel='Frequency Density'
    )
    
    plt.show()
    
    # Print frequency information
    print("\nClass intervals, frequencies, and densities:")
    for i in range(len(counts)):
        print(f"[{edges[i]:.1f}, {edges[i+1]:.1f}): "
              f"Frequency = {int(counts[i])}, "
              f"Density = {densities[i]:.2f}")
