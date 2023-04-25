.. Examples of different theme style elements.
   Copyright Ashley. 2023.

Examples
========

Text emphasis
~~~~~~~~~~~~~
A word in *emphasis*.

A pair of words in **strong emphasis**.

A word in `italics`.

.. code-block:: reStructuredText

   A word in *emphasis*.

   A pair of words in **strong emphasis**.

   A word in `italics`.

Links
~~~~~
A hyperlink http://www.python.org.

Web hyperlinks are detected automatically.

Lists
~~~~~
A bullet point list (using ``*`` as the 'bullet'):

 * Item 1
 * Item 2
 * Item 3

.. code-block:: reStructuredText

    * Item 1
    * Item 2
    * Item 3

A numbered list (using ``#.`` as the 'bullet'):

 #. Item 1
 #. Item 2
 #. Item 3

.. code-block:: reStructuredText

    #. Item 1
    #. Item 2
    #. Item 3

Tables
~~~~~~
Both simple tables and grid tables are rendered in the same way.

A simple table:

========  ========  ========
Header 1  Header 2  Header 3
========  ========  ========
Item      Item      Item
Item      Item      Item
Item      Item      Item
========  ========  ========

.. code-block:: reStructuredText

   ========  ========  ========
   Header 1  Header 2  Header 3
   ========  ========  ========
   Item      Item      Item
   Item      Item      Item
   Item      Item      Item
   ========  ========  ========

A grid table:

+----------+----------+----------+
| Header 1 | Header 2 | Header 3 |
+==========+==========+==========+
| Item     | Item     | Item     |
+----------+----------+----------+
| Item     | Item     | Item     |
+----------+----------+----------+
| Item     | Item     | Item     |
+----------+----------+----------+

.. code-block:: reStructuredText

   +----------+----------+----------+
   | Header 1 | Header 2 | Header 3 |
   +==========+==========+==========+
   | Item     | Item     | Item     |
   +----------+----------+----------+
   | Item     | Item     | Item     |
   +----------+----------+----------+
   | Item     | Item     | Item     |
   +----------+----------+----------+


Code
~~~~
In-line ``code``.

.. code-block:: reStructuredText

   In-line ``code``.

A code block, using the ``code-block`` directive, here a Python code snippet.

.. code-block:: python

   # An example function.

   def print_hello_world(times_to_print):
       """ Prints "Hello World!" a given number of times.

       Args:
           times_to_print (int): Number of times a "Hello World!" is
               to be printed.
       """
       for _ in range(times_to_print):
           print("Hello world!")

.. code-block:: reStructuredText

   .. code-block:: python

      # An example function.

      def print_hello_world(times_to_print):
          """ Prints "Hello World!" a given number of times.

          Args:
              times_to_print (int): Number of times a "Hello World!" is
                  to be printed.
          """
          for _ in range(times_to_print):
              print("Hello world!")

Equations
~~~~~~~~~
This Simple theme has only been tested with ``imgmath``, which renders equations as images using `LaTex <https://www.latex-project.org/>`_ as the equation notation interpreter.

A block equation:

.. math::

   \Pi = 4 \sum_{n=0}^{\infty} \frac{(-1)^{n}}{2n+1}

.. code-block:: reStructuredText

   .. math::

      \Pi = 4 \sum_{n=0}^{\infty} \frac{(-1)^{n}}{2n+1}


An example of an in-line text math, such as adding a symbol like :math:`\pi`.

.. code-block:: reStructuredText

   An example of an in-line text math, such as adding a symbol like :math:`\pi`.

Subscript
~~~~~~~~~
Subscript value x\ :sub:`i`\ .

.. code-block:: reStructuredText

   Subscript value x\ :sub:`i`\ .

Superscript
~~~~~~~~~~~
Superscript value, for example three to the power-of two would be 3\ :sup:`2`\ .

.. code-block:: reStructuredText

   Superscript value, for example three to the power-of two would be 3\ :sup:`2`\ .

Images
~~~~~~
An example image.

.. figure:: _static/example_image.jpg
   :width: 80%
   :alt: A test image.

   A test image.

.. code-block:: reStructuredText

   .. figure:: _static/example_image.jpg
      :width: 80%
      :alt: A test image.

      A test image.

Admonitions
~~~~~~~~~~~

Danger:

.. danger::

   This is a danger admonition.

.. code-block:: reStructuredText

   .. danger::

      This is a danger admonition.


Error:

.. error::

   This is an error admonition.

.. code-block:: reStructuredText

   .. error::

      This is an error admonition.

Caution:

.. caution::

   This is a caution admonition.

.. code-block:: reStructuredText

   .. caution::

      This is a caution admonition.

Warning:

.. warning::

   This is a warning admonition.

.. code-block:: reStructuredText

   .. warning::

      This is a warning admonition.


Attention:

.. attention::

   This is an attention admonition.

.. code-block:: reStructuredText

   .. attention::

      This is an attention admonition.

Important:

.. important::

   This is an important admonition.

.. code-block:: reStructuredText

   .. important::

      This is an important admonition.

Note:

.. note::

   This is a note admonition.

.. code-block:: reStructuredText

   .. note::

      This is a note admonition.

Hint:

.. hint::

   This is a hint admonition.

.. code-block:: reStructuredText

   .. hint::

      This is a hint admonition.


Tip:

.. tip::

   This is a tip admonition.

.. code-block:: reStructuredText

   .. tip::

      This is a tip admonition.

A generic admonition:

.. admonition:: Custom admonition title

   This is a generic admonition.

.. code-block:: reStructuredText

   .. admonition:: Custom admonition title

      This is a generic admonition.
