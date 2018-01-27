# functions for visualizing voxels as 3D cubes
import numpy as np
import plotly.graph_objs as go

def _to_cube(origin):
    '''Convert a voxel at origin into arrays of vertices and triangular faces.
    Args:
        origin - a 3-tuple, the origin of the cube
    Returns:
        (x, y, z, i, j, k) - 6 integer arrays.
            x, y, z are the cube vertices,
            i, j, k are the cube faces
    '''

    x, y, z = [], [], []
    for v in range(8):
        x.append(origin[0] + v//4)
        y.append(origin[1] + v//2 % 2)
        z.append(origin[2] + v % 2)

    i = [0, 1, 0, 1, 0, 6, 2, 7, 4, 7, 1, 7]
    j = [1, 2, 1, 4, 2, 2, 3, 3, 5, 5, 3, 3]
    k = [2, 3, 4, 5, 4, 4, 6, 6, 6, 6, 5, 5]

    return x, y, z, i, j, k

def mesh_cubes(vox_image: np.ndarray):
    '''Turn a 3d array of 0, 1 values into a list of plotly.go.Mesh3d objects
    that can be plotted.
    Return a list of cubes as Mesh3d objects
    '''

    # must be a 3-d array
    assert vox_image.ndim == 3

    cubes = []

    # iterate over the entire 3d array
    for i_ind in range(vox_image.shape[0]):
        for j_ind in range(vox_image.shape[1]):
            for k_ind in range(vox_image.shape[2]):
                if vox_image[i_ind, j_ind, k_ind] == 1.:
                    # convert the voxel at this position into a cube
                    cube = _to_cube((i_ind, j_ind, k_ind))
                    # append these vertices and faces as a Mesh3d object
                    cubes.append(
                        go.Mesh3d(
                            x = cube[0],
                            y = cube[1],
                            z = cube[2],
                            i = cube[3],
                            j = cube[4],
                            k = cube[5],
                            showscale=True,
                            color='blue'
                        )
                    )

    return cubes
