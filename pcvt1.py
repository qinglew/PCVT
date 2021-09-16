import cv2
import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from pc_util import read_point_cloud


def visualize(pc, save=False, filename='images/pcvt1.png'):
    """
    Point cloud visualization via matplotlib and opencv.

    Parameter
    ---------
        pc: numpy array with size of (n, 3), n is the number
            of point cloud.
    """
    fig = plt.figure(figsize=(4, 4))  # you can adjust the figsize to decide image size

    x, z, y = pc.transpose(1, 0)
    ax = fig.gca(projection=Axes3D.name, adjustable="box")
    ax.axis("off")
    # ax.axis('scaled')
    ax.view_init(30, -45)

    # max, min = np.max(pc), np.min(pc)
    # ax.set_xbound(min, max)
    # ax.set_ybound(min, max)
    # ax.set_zbound(min, max)
    ax.set_xlim((-0.3, 0.3))
    ax.set_ylim((-0.3, 0.3))
    ax.set_zlim((-0.3, 0.3))
    ax.scatter(x, y, z, zdir="z", c=x, cmap="jet")

    fig.canvas.draw()
    img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep="")

    img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    plt.close(fig)

    cv2.imshow('pc', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if save:
        cv2.imwrite(filename, img)


if __name__ == '__main__':
    point_cloud = read_point_cloud('pc.ply')
    visualize(point_cloud, True)
