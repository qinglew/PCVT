import os

import torch
import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm


def draw_any_set(titles, pcds, filename, layout=None, ax_limit=0.3, size=1,
                 apply_ax_limit=True, colors=None, axis_off=True,
                 figuresize=None, wspace=None, hspace=None, set_title=True, show=False):
    """
    flexibly draw a list of point clouds 
    """
    ax_min = 0
    ax_max = 0
    pcd_np_list = []
    for pcd in pcds:
        if isinstance(pcd,np.ndarray):
            pcd = torch.from_numpy(pcd)
        if pcd.shape[0] == 1:
            pcd.squeeze_(0)
        pcd = pcd.detach().cpu().numpy()
        pcd_np_list.append(pcd)
        ax_min = min(ax_min, np.min(pcd))
        ax_max = max(ax_max, np.max(pcd))
    # in case the generated points has a larger range
    # ax_limit = min(max(abs(ax_min),ax_max) * 1.05, 0.5)  

    if layout == None:
        row = 1
        col = len(pcd_np_list)
        fig = plt.figure(figsize=(len(pcds)*4, 4))
    else:
        row, col = layout
    if figuresize is None:
        fig = plt.figure(figsize=(col*4, row*4))
    else:
        fig = plt.figure(figsize=figuresize)

    for i in range(len(pcd_np_list)):
        pcd = pcd_np_list[i]
        ax = fig.add_subplot(row, col, i + 1, projection='3d')
        if colors is None:
            ax.scatter(pcd[:,0], pcd[:,2], pcd[:,1], s=size, label=titles[i])
        elif colors[i] is None:
            ax.scatter(pcd[:,0], pcd[:,2], pcd[:,1], s=size, label=titles[i])
        else:
            ax.scatter(pcd[:,0], pcd[:,2], pcd[:,1], s=size, label=titles[i], color=colors[i])
        if apply_ax_limit:
            ax.set_xlim([-ax_limit, ax_limit])
            ax.set_ylim([-ax_limit, ax_limit])
            ax.set_zlim([-ax_limit, ax_limit ])
        if set_title:
            ax.set_title(titles[i])
        if axis_off:
            plt.axis('off')
        
    if wspace is not None or hspace is not None:
        plt.subplots_adjust(wspace=wspace,hspace=hspace)

    if show:
        plt.show()
    else:
        output_f = os.path.join(filename)
        plt.savefig(output_f)


if __name__ == '__main__':
    point_cloud = np.asarray(o3d.io.read_point_cloud('pc.ply').points)
    point_cloud = point_cloud[np.random.choice(len(point_cloud), 4096, replace=False)]
    draw_any_set(['point cloud'], [point_cloud], 'images/pcvt5.png', axis_off=True)
