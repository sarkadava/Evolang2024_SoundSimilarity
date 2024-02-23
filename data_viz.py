import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# get the current folder
curfolder = os.getcwd()
datafolder = os.path.join(curfolder, 'datasets')
plotfolder = os.path.join(curfolder, 'plots')


# load in the csv
df = pd.read_csv(os.path.join(datafolder, 'meanDist_pertrial.csv'))

# Set font family to Times
plt.rcParams['font.family'] = 'Times New Roman'

sns.set_style('white')
plt.figure(figsize=(5, 10))  # Adjust the figure size for better visualization
#palette = sns.color_palette("tab10", 1)
# use this as a pallete #7570B3 and black
palette = ['#7570B3']
palette2 = ['#000000']
ax = sns.violinplot(y="Dist_mean", x="word", data=df, dodge=True,
                    palette=palette, split=True, inner=None, edgecolor=None, linewidth=0, legend=False, scale='width', alpha=0.9, cut=0)

for violin in ax.collections:
    bbox = violin.get_paths()[0].get_extents()
    x0, y0, width, height = bbox.bounds
    violin.set_clip_path(plt.Rectangle((x0, y0), width/2, height, transform=ax.transData))

sns.boxplot(y="Dist_mean", x="word", data=df, saturation=1, showfliers=False,
            width=0.2, boxprops={'zorder': 3, 'facecolor': 'none'}, ax=ax)

old_len_collections = len(ax.collections)
sns.stripplot(y="Dist_mean", x="word", data=df, palette=palette2, dodge=True, ax=ax, legend=False, zorder=1, size=3)

for dots in ax.collections[old_len_collections:]:
    dots.set_offsets(dots.get_offsets() + np.array([0, 0]))

plt.xticks(rotation=45)  # Rotate x-axis labels
plt.xticks(fontsize=16)  # Rotate x-axis labels and adjust font size
plt.yticks(fontsize=12)  # Rotate x-axis labels and adjust font size
plt.xlabel('')  # Rename x-axis
plt.ylabel('Average distance per trial', fontsize=17)  # Remove y-axis label
#plt.xlim(0, 1)  # Show x-axis from 0 to 1
# add title
plt.title('Average distance between segments across concepts', fontsize=20)
plt.show()