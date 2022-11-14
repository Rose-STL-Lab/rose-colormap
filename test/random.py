from test_colormap_plt import test_colormap_plt, dirname
from test_colormap_plotly import test_colormap_plotly
import os
from os import listdir
from os.path import join

"""
Generate a lot of images for mosaic effect
"""
if __name__ == '__main__':
    idx = 0
    for _ in range(10):
        for cm_name in ["rose", "rose_muted", "rose_vivid"]:
            test_colormap_plt(cm_name)
            test_colormap_plotly(cm_name)
        # Change image names
        for parent_dir in [join(dirname, 'figs'), join(dirname, 'figs/plotly')]:
            for f in listdir(parent_dir):
                if 'rose' in f:
                    os.rename(join(parent_dir, f), join(parent_dir, f'{idx}.png'))
                    idx += 1
