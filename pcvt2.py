import numpy as np
import open3d as o3d

from pc_util import read_point_cloud


def visualize(pc_array):
    if isinstance(pc_array, np.ndarray):
        pc = o3d.geometry.PointCloud(o3d.utility.Vector3dVector(pc_array))
    elif isinstance(pc_array, o3d.geometry.PointCloud):
        pc = pc_array
    o3d.visualization.draw_geometries([pc])


if __name__ == '__main__':
    point_cloud = read_point_cloud('pc.ply')
    visualize(point_cloud)
