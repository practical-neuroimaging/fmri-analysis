#########################
Working with github forks
#########################

In the homework from day 1, we created github repos called ``fmri_methods``.

You should now have several files in these repos from day2 and the day2
homework.

These repositories are not connected on github.

We'd like to make repositories that are coonected on github, to allow us to
use some nice Github features like `pull requests
<https://help.github.com/articles/using-pull-requests>`_.

To do this, we will take the following steps:

* *Fork* a central github repository;
* *Clone* this fork;
* Add a remote for the central repository;

Then we'll be able to use these linked repositories for pull requests.

So:

Go to : https://github.com/practical-neuroimaging/fmri-methods-2015

Click on the *Fork* button at the top right.

If necessary, select your user account as the place to fork to.

Github will take you to the web-page for this fork.

Copy the "HTTPS clone URL" link to the right of the page.

Clone the repo, with something like::

    cd ~/repos
    git clone https://github.com/your-github-username/fmri-methods-2015.git

Check what remotes you have with::

    cd fmri-methods-2015
    git remote -v

You should have a single remote, called ``origin``, pointing to your fork.

Rename this remote to make it clear it is your fork::

    git remote rename origin your-github-username

Now we add a remote for the central repository (the one we just forked)::

    git remote add origin https://github.com/practical-neuroimaging/fmri-methods-2015.git

Fetch the contents of this remote, to get them down to your hard disk::

    git fetch origin

Now you have remotes pointing to your fork, and the central repo.
