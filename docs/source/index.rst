.. Censys-Take-Home documentation master file, created by
   sphinx-quickstart on Wed Jan 12 17:36:09 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Censys-Take-Home
============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Setup
------

Install Censys

::

   pip install censys

To configure your search credentials run :code:`censys config` or set both :code:`CENSYS_API_ID` and :code:`CENSYS_API_SECRET` environment variables.

::

   $ censys config
   Censys API ID: XXX
   Censys API Secret: XXX
   Successfully authenticated for your@email.com

How to Run
-----------

Install dependencies

::

   cd Censys-Take-Home
   pip install pandas

Run the program in CLI

::

   python3 main.py

This will return a csv file named :code:`out.csv`. The output path is the same location of the :code:`main.py` file.
To change the output location, edit the filepath variable in :code:`main.py`.

