import numpy as np
import imageio
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist


def fix(im, to_cmap='RdBu_r', from_cmap='jet', threshold=400):
    """ Switch colormaps of bitmap image.
    Parameters
    ----------
    im : str | array, shape (n, m, 3)
        Image array. If str, reads image. Transparency (last dimension = 4) is
        ignored. Image values assumed to be >= 0 and < 256
    to_cmap : str
        Output colormap.
    from_cmap : str
        Input colormap
    threshold : int
        maximal euclidian distance allowed to change pixel color.

    Returns
    -------
    im : array, shape (n, m, 3)
        Image array.
    """
    # read file
    if isinstance(im, str):
        im = np.array(imageio.imread(im))
    if np.ndim(im) != 3 or np.shape(im)[2] not in (3, 4):
        raise ValueError('im must be a filename or array of shape (n, m, 3)')
    # remove transparency
    im = im[..., :3]

    # FIXME ensure data type to check if float or int

    # retrieve colormaps
    # FIXME add option to ad-hoc cmap
    from_cmap = plt.get_cmap(from_cmap)(np.linspace(0, 1, 256))[:, :3] * 255
    to_cmap = plt.get_cmap(to_cmap)(np.linspace(0, 1, 256))[:, :3]

    # loop over rows to avoid memory load
    # FIXME: this could be much clearly improved
    new = list()
    for row in im:
        dists = cdist(row, from_cmap)
        idx = np.argmin(dists, axis=1)
        new.append(to_cmap[idx])
        keep = np.min(dists, 1) > threshold
        new[-1][keep] = row[keep] / 255.
    return np.array(np.reshape(new, np.shape(im)) * 255, np.uint8)
