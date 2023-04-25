.. Install steps.
   Copyright Ashley. 2023.

Installation
============

Quick start
-----------

.. include:: quick_start.inc

Full steps
----------
#. Confirm Sphinx is installed on your machine with the command:

   .. code-block:: bash

      sphinx-build --version

   If Sphinx is not installed, follow the `Sphinx installation guide <https://www.sphinx-doc.org/en/master/usage/installation.html>`_.

#. If using equations and using LaTeX for rendering equations ensure LaTeX is installed.

#. Clone a local copy of this repo.

#. Edit the documentation project's ``conf.py`` to use this theme, by setting the HTML theme and HTML theme path in ``conf.py``.

   .. code-block:: python

      html_theme = "sphinx-simple-theme"
      html_theme_path = "<path_to_local_copy_of_theme>"

   Use the ``sphinx-quickstart`` command to create a new Sphinx project, if starting a new project this will create a documentation project structure and a new ``conf.py`` file.
