``django-masquerade`` Documentation
===================================

Masquerade is a simple app to allow site administrators (IE, any user with
is_staff = True) to browse the site as a different user. 

It is implemented via a middleware that looks for a specific key in the user's
session -- the user to masquerade as. Also included are views and templates
to allow the staff user to enter a username to masquerade and turn off
masquerading as well as a template tag that provides links to these views for
staff users.

Installation
------------
- ``pip install django-masquerade`` (or clone/fork)
- Add ``"masquerade"`` to your ``INSTALLED_APPS`` setting
- Add ``"masquerade.middleware.MasqueradeMiddleware"`` to your
  ``MIDDLEWARE_CLASSES`` setting. Note this must come after Session and
  Authentication middleware classes.
- Include ``masquerade.urls`` from your project's root ``urls`` module
- Optionally load and use the ``masquerade`` template tag library in your templates.

Note that there is one template supplied by this app,
``masquerade/mask_form.html``, which does not inherit from any other template.
I recommend you simply copy this into your own template directory and edit as
needed to match your site's look and feel.

Requirements
------------
``masquerade`` depends on django's SessionMiddleware and, obviously,
``django.contrib.auth``.

The unit tests depend on the mock_ library.

Template Tags
-------------
The ``masquerade`` template tag library provides the following tags:

- ``masquerade_link`` creates a link to either the "Masquerade as user" URL (if
  masquerading is not active) or the "Turn off masquerading" URL (if
  masquerading is active). 

- ``masquerade_status`` displays the name of the (other) user that the
  currently logged in user is masquerading as.

**Note**: These template tags require that the ``request`` object be in the
template context, so use ``RequestContext`` to render the template and make
sure the ``django.core.context_processors.request`` context processor is used.

Settings
--------
The following settings can be set in your project's settings file. 

- ``MASQUERADE_REDIRECT_URL`` (default: "/"). The URL to redirect the user to after
  masquerading is activated.
- ``MASQUERADE_REQUIRE_SUPERUSER`` (default: False). If set to true, only users
  with both is_staff and is_superuser set to True will be allowed to use this
  feature.
- ``MASQUERADE_USERNAME_FIELD`` (default: 'username'). If set, defines the
  property name that is matched on the User model with the supplied masquerade
  username. So custom models that don't have ``username`` but use, for example,
  ``email`` as the identifier can set this to be the field that is filtered
  upon.

.. _mock: http://www.voidspace.org.uk/python/mock/

Signals
-------
``masquerade.signals`` defines two signals that can be attached to:

- ``masquerade.signals.mask_on`` is sent when the user successfully masquerades
  as another user. It is sent two arguments: the request object and
  ``mask_username``, the username of the user being masqueraded as. The
  ``sender`` argument is an instance of ``masquerade.forms.MaskForm``.
- ``masquerade.signals.mask_off`` is sent when a masqueraded user visits the
  ``unmask`` view. It also receives  ``request`` and ``mask_username``
  arguments. The ``sender`` argument is an empty object.
