=======
Ghoster
=======

**ghoster** is a admin theme which includes markdown features for `Django <https://www.djangoproject.com/>`_ users.


Snapshot
========
**regular template:**

..  image:: http://i.imgur.com/WHd6Hlt.png
    :width: 30%

..  image:: http://i.imgur.com/iHal9Jf.png
    :width: 30%

**markdown template:**

..  image:: http://i.imgur.com/sXkcUNu.png
    :width: 30%

..  image:: http://i.imgur.com/FJjOHaK.png
    :width: 30%

Requirements
============

* python >= 2.7
* django >= 1.9

Installation
============

1. Download it from PyPi with ``pip install django-ghoster``
2. Add into the ``INSTALLED_APPS`` before ``django.contrib.admin``:

.. code:: python

    INSTALLED_APPS = [
        ...
        'ghoster',
        'django.contrib.admin',
        ...
    ]

Configuration
=============

In ``models.py``, assume the model is defined as below:

.. code:: python

    from django.db import models

	class MyModel(models.Model):
		# the fields which are rendered into markdown
		char_field = models.CharField(max_length=1024)
		text_field = models.TextField()
		
		# other stuff
		foreign_field = ...
		file_field = ...
		url_field = ...
		...

Then in ``admin.py``, inherit ``GhosterAdmin`` and override ``markdown_field`` and ``title_field`` attributes with the field names.

.. code:: python

    from django.contrib import admin
    from ghoster.admin import GhosterAdmin
    from .models import MyModel
    
    class MyModelAdmin(GhosterAdmin):
        markdown_field = "text_field"
        title_field = "char_field"
        
        # other stuff
        list_display = ...
        list_filter = ...
    
    admin.site.register(MyModel, MyModelAdmin)

Then **ghoster** will render the model-form into 3 parts:

* ``title_field``: this field will be placed in top-bar.
* ``markdown_field``: markdown editor with side-by-side preview.
* ``meta_fieldsets``: the rest of fields will be placed in right-sidebar.

Contributing
============

* Author: `Andy Lin <https://github.com/andysmk2/>`_
* maintainer: `Ryan Chao <https://github.com/ryanchao2012>`_

Every code, documentation and UX contribution is welcome.
If you have any suggestions or bug reports please report them to the issue tracker

