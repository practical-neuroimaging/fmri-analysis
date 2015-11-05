###################
An anatomical image
###################

Now we will work with a 3D brain image.

Like the camera image in :doc:`camera`, the pixel data for the 3D
image is in a text file called ``anatomical.txt``.  Download
:download:`anatomical.txt` to your working directory.

I happen to know this image has is length 32 on the third dimension,
but I don't know what the size of the first two dimensions are.

So, I know the image is of shape (``I``, ``J``, 32), but I don't know
what ``I`` and ``J`` are.

Here are the first four lines of ``anatomical.txt``.

::

    0.0000
    0.0000
    53.0000
    43.0000

The data is in the same floating point text format as the camera
picture pixel data.

Real all the lines of the file into an array of float values, as before.

::

    # Read the lines into an array of floats

How many pixel values does this file contain?

When I have my image array correctly shaped, then, if I take a slice
over the third dimension:

::

    slice_on_third = image_array[:, :, 0]

``slice_on_third`` will be shape ``(I, J)`` (the size of the first two
dimensions).

So, how many pixel values does a slice in the third dimension contain
|--| given that we know the third dimension is length 32? Put another
way, what is the value for ``I * J``?

.. code:: python

    # Find the size of a slice over the third dimension
    # P = ?

Call ``P`` the number of values per slice on the third dimension (so
``P == I * J`` where we don't yet know ``I`` or ``J``).

Is this slice over the third dimension square (does ``I == J``)?

We need to find the values for ``I`` and ``J``.

Find candidates for ``I`` by using the modulus operator (``%``) to
find a few numbers between 120 and 200 that divide exactly into the
slice size ``P``. Hint: the first value will be 120.

::

    # Make a list of candidates for I

These numbers are candidates for ``I`` - the first number in the pair
``(I, J)``. We now need to find the corresponding ``J`` for each
candidate for ``I``.

Use the integer division operator (``//``) to get a list of pairs of
numbers ``I`` and ``J`` such that ``I * J == P``. Hint: the first pair
of ``I, J`` is (120, 221).

::

    # Make list of pairs of I, J such that I * J == P

The full image shape will be three values, with one of these ``(I,
J)`` pairs followed by 32. For example, the correct shape might be
(120, 221 , 32) (it isn't!). Try reshaping the pixel data with a few
of the ``(I, J, 32)`` candidates to see which one is likely to be
right. You might want to plot a slice over the third dimension to see
how it looks.

::

    # Make the pixel values list into an array
    # Try reshaping the array with candidate triples of (I, J, 32)
    # Which I, J, 32 triple is the right one?

Finally, save your script that does the correct reshaping as ``anatomical.py``
commit to your repository, and push up to github.

.. include:: links_names.inc
