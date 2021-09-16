import open3d as o3d

from pc_util import read_point_cloud, random_sampling


def create_sphere_at_xyz(xyz, radius, colors=None, resolution=4):
    """create a mesh sphere at xyz
    Args:
        xyz: arr, (3,)
        colors: arr, (3, )
    Returns:
        sphere: mesh sphere
    """
    sphere = o3d.geometry.TriangleMesh.create_sphere(radius=radius, resolution=resolution)
    # sphere.compute_vertex_normals()
    if colors is None:
        sphere.paint_uniform_color([0.7, 0.1, 0.1])  # To be changed to the point color.
    else:
        sphere.paint_uniform_color(colors)
    sphere = sphere.translate(xyz)
    return sphere


def create_pcd_mesh(point_cloud, radius=0.005, colors=None):
    """create a mesh spheres for all coordinates in point_cloud
    Args:
        point_cloud: arr, (m, 3)
        colors: arr, (3, )
    Returns:
        mesh_pcd: obj, mesh point cloud
    """
    mesh = []
    for i in range(point_cloud.shape[0]):
        mesh.append(create_sphere_at_xyz(point_cloud[i], radius=radius, colors=colors))

    mesh_pcd = mesh[0]
    for i in range(1, len(mesh)):
        mesh_pcd += mesh[i]
    return mesh_pcd


if __name__ == '__main__':
    point_cloud = read_point_cloud('pc.ply')
    pc_mesh = create_pcd_mesh(point_cloud)
    o3d.io.write_triangle_mesh('pc_mesh.ply', pc_mesh)

    # create a sparse mesh
    sparse_point_cloud = random_sampling(point_cloud, n=2048)
    pc_mesh = create_pcd_mesh(sparse_point_cloud, radius=0.01)
    o3d.io.write_triangle_mesh('sparse_pc_mesh.ply', pc_mesh)
