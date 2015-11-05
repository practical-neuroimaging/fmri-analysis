####################
Into four dimensions
####################

Download the 4D image file :download:`ds114_sub009_t2r1.nii` to your working directory.

Start at the IPython console.  We recommend you begin your IPython console session with these standard lines::

    # Compatibility with Python 3
    from __future__ import print_function, division

    # Interactive graphs for matplotlib at the IPython prompt
    %matplotlib

    # Standard imports of libraries
    import numpy as np
    import matplotlib.pyplot as plt

``ds114_sub009_t2r1.nii`` is a four-dimensional (X, Y, Z, t) BOLD image.

Import the ``nibabel`` module, and load the image with nibabel to create an
image object.

.. code:: python

    # Load image object using nibabel

In the usual way get the array data from this image. What is the image
shape?

.. code:: python

    # Get image array data from image object

Select the 1st volume (time index 0) from 4D image data array, by
slicing over the last dimension. What shape is it?

.. code:: python

    # Get the 1st volume and show shape

Use matplotlib to show the central slice over the third dimension:

.. code:: python

    # Matplotlib display of the center slice, slicing over the 3rd dimension

Get the standard deviation across all voxels in the 3D volume (the first
volume):

.. code:: python

    # Standard deviation across all voxels for 1st volume

Now get the second 3D volume in the 4D time series.

Plot the center slice (slicing over the third dimension). Show the
standard deviation.

.. code:: python

    # Get the second 3D volume.
    # Show the central slice (over the 3rd dimension).
    # Get the standard deviation across all voxels

Do the same for the third volume in the 4D time series:

.. code:: python

    # Get the second 3D volume.
    # Show the central slice (over the 3rd dimension).
    # Get the standard deviation across all voxels

Loop over all volumes in the 4D image and store the standard deviation
for each volume in a list. Plot these standard deviation values to see if
there are any volumes with particularly unusual standard deviation.

.. code:: python

    # Get standard deviation for each volume; then plot the values
