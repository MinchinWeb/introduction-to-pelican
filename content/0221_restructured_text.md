title: Restructured Text

- Orginally created for Python documentation.
- well defined specification
- great Python support

```rest
My super title
##############

:date: 2010-10-03 10:20
:modified: 2010-10-04 18:40
:tags: thats, awesome
:category: yeah
:slug: my-super-post
:authors: Alexis Metaireau, Conan Doyle
:summary: Short version for index and feeds

This will be turned into :abbr:`HTML (HyperText Markup Language)`.

.. image:: /path/to/image.jpg

.. code-block:: python
    :classprefix: pgcss
    :linenos: table
    :linenostart: 153

   print("A literal block directive explicitly marked as python code")

A sentence with links to Wikipedia_ and the `Linux kernel archive`_.

.. _Wikipedia: http://www.wikipedia.org/
.. _Linux kernel archive: http://www.kernel.org/
```
