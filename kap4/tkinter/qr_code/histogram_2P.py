"""
Histogram-generator.


Author: Claude 4.5 02.12.2025
"""

import matplotlib.pyplot as plt
import numpy as np

def create_histogram(data_dict, color='skyblue', 
                    edge_color='black', edge_width=1.5,
                    font_size=12, title='Histogram', 
                    xlabel='Values', ylabel='Frequency Density',
                    x_tick_interval=None, y_tick_count=10):
    """
    Create a customizable histogram with frequency density from a dictionary.
    
    Parameters:
    -----------
    data_dict : dict
        Dictionary where each key represents a class with attributes:
        - 'start': x-value where the class begins
        - 'width': width of the class
        - 'frequency': frequency count for the class
        Example: {
            'class1': {'start': 0, 'width': 5, 'frequency': 10},
            'class2': {'start': 5, 'width': 5, 'frequency': 15}
        }
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
    x_tick_interval : float, optional
        Interval between x-axis ticks. If None, uses automatic spacing
    y_tick_count : int
        Approximate number of ticks on y-axis (default: 10)
    """
    
    # Extract data from dictionary
    starts = []
    widths = []
    frequencies = []
    
    for class_name, class_data in data_dict.items():
        starts.append(class_data['start'])
        widths.append(class_data['width'])
        frequencies.append(class_data['frequency'])
    
    # Convert to numpy arrays
    starts = np.array(starts)
    widths = np.array(widths)
    frequencies = np.array(frequencies)
    
    # Calculate frequency densities
    densities = frequencies / widths
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create bars with density heights
    for i in range(len(starts)):
        ax.bar(starts[i], densities[i], width=widths[i], 
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
    
    # Set tick intervals for higher resolution
    if x_tick_interval is not None:
        x_min = np.min(starts)
        x_max = np.max(starts + widths)
        ax.set_xticks(np.arange(x_min, x_max + x_tick_interval, x_tick_interval))
    
    # Set y-axis tick count
    ax.yaxis.set_major_locator(plt.MaxNLocator(y_tick_count))
    
    # Add grid for better readability
    ax.grid(axis='both', alpha=0.8, linestyle='--')
    ax.set_axisbelow(True)
    
    plt.tight_layout()
    return fig, ax, frequencies, densities, starts, widths


# Example usage
if __name__ == "__main__":
    # Create sample data dictionary
    data = {
        'class1': {'start': 0, 'width': 5, 'frequency': 30},
        'class2': {'start': 5, 'width': 10, 'frequency': 90},
        'class3': {'start': 15, 'width': 15, 'frequency': 60},
        'class4': {'start': 30, 'width': 30, 'frequency': 30},
    }
    
    # Create histogram with custom parameters
    fig, ax, frequencies, densities, starts, widths = create_histogram(
        data_dict=data,
        color='dodgerblue',       # Bar color
        edge_color='darkblue',     # Edge color
        edge_width=2,             # Edge width
        font_size=14,             # Font size
        title='Reisetid skolevei VG2 Furuskogen skole',
        xlabel='Minutter skolevei',
        ylabel='Antall per minutt',
        x_tick_interval=5,      # Show tick every 2.5 units on x-axis
        y_tick_count=10           # Show approximately 15 ticks on y-axis
    )
    
    plt.show()
    
    # Print frequency information
    print("\nClass intervals, frequencies, and densities:")
    for i, class_name in enumerate(data.keys()):
        end = starts[i] + widths[i]
        print(f"{class_name}: [{starts[i]:.1f}, {end:.1f}): "
              f"Frequency = {int(frequencies[i])}, "
              f"Density = {densities[i]:.2f}")

