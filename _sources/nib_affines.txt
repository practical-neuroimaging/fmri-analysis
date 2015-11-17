######################################################
Applying affines with ``nibabel.affines.apply_affine``
######################################################

We often want to apply an affine to an array of coordinates, where the
last axis of the array is length 3, containing the x, y and z
coordinates.

.. nbplot::
    :include-source: false

    import os
    import sys
    sys.path.append(os.path.join('..', 'code'))

Nibabel uses ``nibabel.affines.apply_affine`` for this.

.. nbplot::

    >>> import numpy as np
    >>> import numpy.linalg as npl
    >>> import nibabel as nib

.. nbplot::

    >>> points = np.array([[0, 1, 2], [2, 2, 4], [3, -2, 1], [5, 3, 1]])
    >>> points
    array([[ 0,  1,  2],
           [ 2,  2,  4],
           [ 3, -2,  1],
           [ 5,  3,  1]])

.. nbplot::

    >>> zooms_plus_translations = nib.affines.from_matvec(np.diag([3, 4, 5]), [11, 12, 13])
    >>> zooms_plus_translations
    array([[ 3,  0,  0, 11],
           [ 0,  4,  0, 12],
           [ 0,  0,  5, 13],
           [ 0,  0,  0,  1]])

.. nbplot::

    >>> nib.affines.apply_affine(zooms_plus_translations, points)
    array([[11, 16, 23],
           [17, 20, 33],
           [20,  4, 18],
           [26, 24, 18]])

Of course, this is the same as:

.. nbplot::

    >>> mat, vec = nib.affines.to_matvec(zooms_plus_translations)
    >>> mat.dot(points.T).T + vec.reshape((1, 3))
    array([[11, 16, 23],
           [17, 20, 33],
           [20,  4, 18],
           [26, 24, 18]])

The advantage of ``nib.affines.apply_affine`` is that it can deal with
arrays of more than two dimensions, and it transposes the transformation
matrices for you to apply the transforms correctly.

A typical use is when applying extra affine transformations to a X by Y
by Z by 3 array of coordinates.

``affine_transform`` and the implied coordinate grid
----------------------------------------------------

.. nbplot::

    >>> from scipy.ndimage import affine_transform, map_coordinates

So far we have done all our image resampling with
``scipy.ndimage.affine_transform``.

``affine_transform`` accepts:

-  an array to resample from (``input``);
-  the ``mat`` part of an affine;
-  the ``vec`` (translation) part of an affine;
-  an optional ``output_shape`` (defaulting to ``input.shape``).

``affine_transform`` then generates all the voxel coordinates *implied
by* the ``output_shape``, and transforms them with the ``mat`` and
``vec`` transforms to get a new set of coordinates ``C``. It then
samples the ``input`` array at the coordinates given by ``C`` to
generate the output array.

Making coordinate arrays with meshgrid
--------------------------------------

``affine_transform`` works by using voxel coordinate implied by the
``output_shape``, and transforming those.

``meshgrid`` is a way of making an actual coordinate grid.

As we will see soon, this is particularly useful when we want to use the
more general form of image resampling in
``scipy.ndimage.map_coordinates``.

If we have some shape - say ``output_shape`` - then this implies a set
of coordinates. Let's say ``output_shape = (5, 4)`` - implying a 2D
array.

The implied coordinate grid will therefore have one coordinate for each
pixel (2D voxel) in the (5, 4) array.

Because this array is 2D, there are two coordinate values for each
pixel. For example, the coordinate of the first element in the array is
(0, 0). We can make these i- and j- coordinates with ``meshgrid``:

.. nbplot::

    >>> i_coords, j_coords = np.meshgrid(range(5), range(4), indexing='ij')
    >>> print('i_coords', i_coords)
    i_coords [[0 0 0 0]
     [1 1 1 1]
     [2 2 2 2]
     [3 3 3 3]
     [4 4 4 4]]
    >>> print('j_coords', j_coords)
    j_coords [[0 1 2 3]
     [0 1 2 3]
     [0 1 2 3]
     [0 1 2 3]
     [0 1 2 3]]

We can make this into a shape (2, 5, 4) array where the first axis
contains the (i, j) coordinate.

.. nbplot::

    >>> coordinate_grid = np.array([i_coords, j_coords])
    >>> coordinate_grid.shape
    (2, 5, 4)

Because we have not done any transformation on the coordinate, the i, j
coordinate will be the same as the index we use to get the i, j
coordinate:

.. nbplot::

    >>> print(coordinate_grid[:, 0, 0])
    [0 0]
    >>> print(coordinate_grid[:, 1, 0])
    [1 0]
    >>> print(coordinate_grid[:, 0, 1])
    [0 1]

This then is the coordinate grid implied by a shape of (5, 4).

Now imagine I wanted to do a transformation on these coordinates. Say I
wanted to add 2 the first (i) coordinate:

.. nbplot::

    >>> coordinate_grid[0, :, :] += 2

Now my coordinate grid expresses a *mapping* between a given
(:math:`i, j`) coordinate, and the new coordinate (:math:`i', j'`. I
look up the new coordinate using the :math:`i, j` index into the
coordinate grid:

.. nbplot::

    >>> print(coordinate_grid[:, 0, 0])  # look up new coordinate for (0, 0)
    [2 0]
    >>> print(coordinate_grid[:, 1, 0])  # look up new coordinate for (1, 0)
    [3 0]
    >>> print(coordinate_grid[:, 0, 1])  # look up new coordinate for (0, 1)
    [2 1]

This means we can use these coordinate grids as a *mapping* from an
input set of coordinates to an output set of coordinates, for each pixel
/ voxel.

As you can imagine, meshgrid extends simply to three dimensions or more:

.. nbplot::

    >>> output_shape = (5, 6, 7)
    >>> i_coords, j_coords, k_coords = np.meshgrid(range(output_shape[0]), range(output_shape[1]), range(output_shape[2]),
    ...                                            indexing='ij')
    >>> coordinate_grid = np.array([i_coords, j_coords, k_coords])
    >>> coordinate_grid.shape
    (3, 5, 6, 7)

.. nbplot::

    >>> print(coordinate_grid[:, 0, 0, 0])
    [0 0 0]
    >>> print(coordinate_grid[:, 1, 0, 0])
    [1 0 0]
    >>> print(coordinate_grid[:, 0, 1, 0])
    [0 1 0]
    >>> print(coordinate_grid[:, 0, 0, 1])
    [0 0 1]

General resampling between images with ``scipy.ndimage.map_coordinates``
------------------------------------------------------------------------

``map_coordinates`` is the more general of resampling from images with
coordinates.

Instead of using the *implied* coordinate grid, we pass in an actual
coordinate array.

This means that we can resample using coordinate transformations that
can't be expressed as an affine, such as complex non-linear
transformations. ``map_coordinates`` accepts:

-  array array to resample from (``input``);
-  The ``C`` array shape (3,) + output\_shape giving the voxel
   coordinates at which to sample ``input``.

``map_coordinates`` then makes an empty array shape ``D`` where
``D = C.shape[1:]``. For every index ``i, j, k`` it:

-  Gets the 3-length vector ``coord = C[:, i, j, k]`` giving the voxel
   coordinate in ``input``;
-  Samples ``input`` at coordinates ``coord`` to give value ``v``;
-  Inserts ``v`` into ``D`` with ``D[i, j, k] = v``.

This might be clearer with an example. Let's resample a structural to a
functional like we did last week (see
``day10/resampling_with_affines_solutions.ipynb``:

.. nbplot::

    >>> import nibabel as nib
    >>> bold_img = nib.load('ds114_sub009_t2r1.nii')
    >>> mean_bold_data = bold_img.get_data().mean(axis=-1)
    >>> structural_img = nib.load('ds114_sub009_highres.nii')
    >>> structural_data = structural_img.get_data()

We now now the transformation to go from voxels in the structural to
voxels in the (mean) functional:

.. nbplot::

    >>> struct_vox2mean_vox = npl.inv(bold_img.affine).dot(structural_img.affine)
    >>> struct_vox2mean_vox
    array([[ -0.2497,   0.0151,  -0.0027,  63.5174],
           [  0.0115,   0.3242,   0.0137,   1.1053],
           [ -0.0034,  -0.0176,   0.2496, -27.7359],
           [  0.    ,   0.    ,   0.    ,   1.    ]])

Sure enough, if we use this affine to resample the functional image, we
get a functional image with the same voxel sizes and positions as the
structural image:

.. nbplot::

    >>> # Resample using affine_transform
    >>> mat, vec = nib.affines.to_matvec(struct_vox2mean_vox)
    >>> resampled_mean = affine_transform(mean_bold_data, mat, vec, output_shape=structural_data.shape)

To display the plots we first set the plot default to greyscale colormap and
nearest-neighbor interpolation:

.. nbplot::

    >>> # - set gray colormap and nearest neighbor interpolation by default
    >>> plt.rcParams['image.cmap'] = 'gray'
    >>> plt.rcParams['image.interpolation'] = 'nearest'

Then we show the interpolated (resampled) data:

.. nbplot::

    >>> # Show resampled data
    >>> fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    >>> axes[0].imshow(resampled_mean[:, :, 150])
    >>> axes[1].imshow(structural_data[:, :, 150])
    ...

We get the exact same effect with ``map_coordinates`` if we create the
voxel coordinates ourselves, and apply the transform to them:

.. nbplot::

    >>> # Get the I, J, K coordinates implied by the structural data array shape
    >>> I, J, K = structural_data.shape
    >>> i_vals, j_vals, k_vals = np.meshgrid(range(I), range(J), range(K), indexing='ij')
    >>> in_vox_coords = np.array([i_vals, j_vals, k_vals])
    >>> in_vox_coords.shape
    (3, 256, 156, 256)

.. nbplot::

    >>> in_vox_coords[:, 0, 0, 0]
    array([0, 0, 0])

.. nbplot::

    >>> in_vox_coords[:, 1, 0, 0]
    array([1, 0, 0])

Transform using affine:

.. nbplot::

    >>> coords_last = in_vox_coords.transpose(1, 2, 3, 0)
    >>> mean_vox_coords = nib.affines.apply_affine(struct_vox2mean_vox, coords_last)
    >>> coords_first_again = mean_vox_coords.transpose(3, 0, 1, 2)

Use this with ``map_coordinates`` to get the same result as we got for
``affine_transform``:

.. nbplot::

    >>> # Resample using map_coordinates
    >>> resampled_mean_again = map_coordinates(mean_bold_data, coords_first_again)

.. nbplot::

    >>> # Show resampled data
    >>> fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    >>> axes[0].imshow(resampled_mean_again[:, :, 150])
    >>> axes[1].imshow(structural_data[:, :, 150])
    ...
