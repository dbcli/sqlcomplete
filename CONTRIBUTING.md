Development Guide
-----------------
This is a guide for developers who would like to contribute to this project.

Local Setup
-----------

The installation instructions in the README file are intended for users of
sqlcomplete. If you're developing sqlcomplete, you'll need to install it in a slightly
different way so you can see the effects of your changes right away without
having to go through the install cycle everytime you change the code.

It is highly recommended to use virtualenv for development. If you don't know
what a virtualenv is, this [guide]
(http://docs.python-guide.org/en/latest/dev/virtualenvs/#virtual-environments)
will help you get started.

Create a virtualenv (let's call it sqlcomplete-dev). Activate it:

    virtualenv sqlcomplete-dev
    source ./sqlcomplete-dev/bin/activate

Once the virtualenv is activated, `cd` into the local clone of sqlcomplete folder
and install sqlcomplete using pip as follows:

::

    $ pip install --editable .

    or

    $ pip install -e .

This will install the necessary dependencies as well as install sqlcomplete
from the working folder into the virtualenv. By installing it using `pip
install -e` we've linked the sqlcomplete installation with the working copy. So
any changes made to the code is immediately available in the installed version
of sqlcomplete. This makes it easy to change something in the code, run the
tests and check the effects of your change.

Running tests
-------------

Tests use pytest and tox.

Install the requirements for testing:

    $ pip install -r requirements-dev.txt

After that, tests can be run with:

    $ pytest
    

To run the tests in all the supported versions of python: 

    $ tox


Lint
----

We use [black](https://github.com/ambv/black) for maintaining a consistent code format. You can run:

    $ black

That will fix the code formatting for all the files in the current directory.

GitHub Workflow
---------------

If you're new to github this section can help you with the workflow. `Fork the
project <https://github.com/dbcli/sqlcomplete>`_ in github.  Then clone your fork
into your computer (``git clone <url-for-your-fork>``).  Make the changes and
create the commits in your local machine. Then push those changes to your fork.
Then click on the pull request icon on github and create a new pull request.
Add a description about the change and send it along. I promise to review the
pull request in a reasonable window of time and get back to you.

In order to keep your fork up to date with any changes from mainline, add a new
git remote to your local copy called 'upstream' and point it to the main sqlcomplete  
repo.

::

   $ git remote add upstream git@github.com:dbcli/sqlcomplete.git

Once the 'upstream' end point is added you can then periodically do a ``git
pull upstream master`` to update your local copy and then do a ``git push
origin master`` to keep your own fork up to date.
