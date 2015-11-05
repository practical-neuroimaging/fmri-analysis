##############################
Loading data from NIfTI images
##############################

We will spend a lot of time loading data from medical images.

MRI images for functional MRI are usually stored using the `NIfTi
format`_.

This is a very simple format that is typically a single file with
extension `.nii`.  If the file is compressed, it will end with
``.nii.gz`` instead.

Inside, the file contains:

* 352 bytes of *header* information.  The header gives the 3D or 4D shape of
  the file, and the data type of the pixel (voxel) data among other things.
* Usually, directly after the header, we have the image data.  If the image
  data is shape (I, J, K), and S is the number of bytes to store one pixel
  (voxel) value, then the image data is I * J * K * S in length.  For example,
  the image might be shape 64, 64, 32, and the data type might be 64-bit
  float, which is 8 bytes long, so the image data would be 64 * 64 * 32 * 8
  bytes long.

To load these images, we use the Python package `nibabel`_.

Check if you have this package, start IPython and type::

    In [1]: import nibabel

If this gives you an import error (it probably will), exit from IPython, and
type::

    pip install --user nibabel

Now try to import nibabel again.  It should work.  If it doesn't call over one
of your instructors.

Now, download the example image we are going to use to your working directory:
:download:`ds107_sub001_highres.nii`.

Start IPython.

Import the nibabel library:

.. code:: python

    import nibabel as nib

Load the image:

.. code:: python

    img = nib.load('ds107_sub001_highres.nii')

What type of thing is ``img``?  What attributes and methods does it have?

We can load the image data as an array with:

.. code:: python

    data = img.get_data()

.. include:: links_names.inc
