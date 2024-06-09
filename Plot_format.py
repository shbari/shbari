import matplotlib.pyplot as plt
import numpy as np
# https://matplotlib.org/1.5.3/users/style_sheets.html
def set_publication_style(ax=None, title='Publication-Ready Plot', xlabel='X-axis label', ylabel='Y-axis label', legend=True):
    """
    Sets up a publication-ready style for matplotlib plots.

    Args:
        ax (matplotlib.axes.Axes, optional): The axes object to apply the style to.
            If None, the current active axes will be used.
        title (str, optional): Title for the plot.
        xlabel (str, optional): Label for the X-axis.
        ylabel (str, optional): Label for the Y-axis.
        legend (bool, optional): Whether to display the legend (default is True).

    Returns:
        None
    """
    if ax is None:
        ax = plt.gca()  # Get the current active axes

    # Adjust font size and style
    plt.rcParams['font.size'] = 12
    plt.rcParams['font.family'] = 'serif'

    # Customize grid lines (remove major ticks)
    #ax.grid(color='gray', linestyle='--', linewidth=0.5, which='minor')
    #ax.grid(color='gray', linestyle='--', linewidth=0.5, which='major')  # Remove this line

    # Customize axis ticks
    ax.tick_params(axis='both', which='both', direction='in', top=True, right=True)

    # Customize legend (added this line)
    if legend:
        ax.legend(frameon=False)

    # Customize title and axis labels
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Customize plot colors (optional)
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])

# Example usage:
x = np.linspace(0, 10, 1000)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y, label='Sin(x)')

# Customize your plot elements
set_publication_style(ax, title='Customized Plot', xlabel='Time (s)', ylabel='Amplitude', legend=True)

plt.tight_layout()  # Ensures labels are not cut off
plt.show()
