import open3d as o3d
import numpy as np
import h5py


def read_point_cloud(filename, key=None):
    if filename.endswith('.ply') or filename.endswith('.obj'):
        pc = np.asarray(o3d.io.read_point_cloud(filename).points)
    elif filename.endswith('.npz') or filename.endswith('.npy'):
        pc = np.load(filename)
    elif filename.endswith('.txt'):
        pc = np.loadtxt(filename)
    elif filename.endswith('.h5'):
        with h5py.File(filename, 'r') as f:
            pc = f[key]
    
    return pc


def random_sampling(pc, n=2048):
    replace = True if n < pc.shape[0] else False
    inds = np.random.choice(pc.shape[0], n, replace)
    return pc[inds]
