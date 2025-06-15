import matplotlib.pyplot as plt

import seaborn as sns

import matplotlib as mpl
 
# Define your color palette exactly as in the article

pitch_colours = {

    'FF': '#1f77b4', 'SL': '#ff7f0e', 'CH': '#2ca02c',

    'CU': '#d62728', 'FC': '#9467bd', 'SI': '#8c564b'

}
 
def set_styles():

    """Configure global matplotlib and seaborn styles."""

    sns.set_theme(style='whitegrid', palette='deep',

                  font='DejaVu Sans', font_scale=1.5)

    mpl.rcParams['figure.dpi'] = 300
 
def plot_pitch_breaks(df, first_name: str, last_name: str):

    """Scatter horizontal vs. vertical break, colored by pitch type."""

    set_styles()

    fig, ax = plt.subplots()

    ax.scatter(df['pfx_x'], df['pfx_z'],

               c=df['pitch_type'].map(pitch_colours), alpha=0.7)

    ax.set_title(f"{first_name} {last_name} – Pitch Breaks")

    ax.set_xlabel("Horizontal Break (inches)")

    ax.set_ylabel("Vertical Break (inches)")

    fig.savefig(f"{last_name}_{first_name}_pitch_breaks.png")

    plt.close(fig)
 
def plot_zone(df, first_name: str, last_name: str):

    """Plot pitch location heatmap over the strike zone."""

    set_styles()

    fig, ax = plt.subplots()

    sns.kdeplot(x='plate_x', y='plate_z', data=df,

                fill=True, thresh=0.05, levels=100, ax=ax)

    ax.set_title(f"{first_name} {last_name} – Pitch Zone")

    ax.set_xlabel("Plate X")

    ax.set_ylabel("Plate Z")

    fig.savefig(f"{last_name}_{first_name}_pitch_zone.png")

    plt.close(fig)

 