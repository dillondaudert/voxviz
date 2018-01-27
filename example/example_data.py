# an example voxel image
import numpy as np

# build up the numpy logo
voxels = np.zeros((4, 3, 4), dtype=int)
voxels[0, 0, :] = 1
voxels[-1, 0, :] = 1
voxels[1, 0, 2] = 1
voxels[2, 0, 1] = 1
