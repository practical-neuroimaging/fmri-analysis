******************************
Homework for day 3 of analysis
******************************

Make a feature branch for the homework
======================================

First, change directory into your ``fmri-methods-2013`` directory.

Fetch the upstream changes with the homework with::

    git fetch origin

Make a new feature branch to work on with::

    git branch day3-homework origin/master

Connect this branch with your own fork with::

    git checkout day3-homework
    git push your-github-username day3-homework --set-upstream

Getting started with the IPython notebook
=========================================

Go to your ``fmri-methods-2015`` repository and change directory (in the
terminal) to the ``day3`` folder.

You'll find some `IPython notebooks <http://ipython.org/notebook.html>`_ in
that folder.

Make sure you have the IPythono notebook installed.  Check by running
``ipython notebook`` from the command line.  If you installed using Anaconda,
this should work.  If you installed using more standard methods (Python.org
installer on Mac, Linux package manager) then try::

    pip install ipython[notebook]

from the command line.  Please let us know if that does not work for you, we
will try and fix it.

Review and extend slice timing
==============================

Review the page on `slice time correction
<http://practical-neuroimaging.github.io/slice_timing.html>`_ that we looked
at on Monday.

Work through the exercises in the notebook ``slice_timing.ipynb``.  The
solutions are in ``slice_timing_solutions.ipynb``.

Now you know all about slice timing your job is to write a Python script to
run slice timing on a 4D image.

Edit `slice_time_image.py` to implement linear slice timing on an image file.
Check the script runs with ``python slice_time_image.py
ds107_sub012_t1r2.nii``.  You can run the script interactively in the IPython
console with ``run slice_time_image.py ds107_sub012_t1r2.nii``.

When you have finished, ``git add`` your edits to ``slice_time_image.py``,
commit, push up to your github fork, and them make a pull request to the main
repository.  I will review these as they come in.

Feel free to put up questions or point out problems using the `Github issues
<https://github.com/practical-neuroimaging/fmri-methods-2015/issues>`_ for our
repository.

Reading
=======

Read:

* `Optimizing in space
  <https://github.com/practical-neuroimaging/pna2015/blob/master/day9/optimizing_space.ipynb>`_.
  There is a copy of this notebook in your ``day3`` repository if you want to
  try running it interactively;
* About the image affine and `Coordinate transformations
  <http://nipy.org/nibabel/coordinate_systems.html>`_.

.. include:: links_names.inc
