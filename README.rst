noffset
===========

Summary
-------

Fast pagination for sql-like databases. **Does not use offset!** `See presentation <https://docs.google.com/file/d/1zaK9h6WtjESetn77XsoK1rqRhXys-vjGu5NQcz40VJSMlpUuQ6ddZdadtYQl/edit?usp=sharing>`_.

Supports: SQLAlchemy.

Explanatory example
--------------

.. code-block:: python

    import noffset.sqla.pagination as pagination

    #### `cursor`, `direction`, `reverse` are optional. If these are not defined func will return param for first page.

    to_template = pagination(sqla_db_object, db_model_class, perpage_items_num, cursor, direction, reverse)

*to_template* is **dict(data, cursor_next, cursor_prev, pages_total)** now.

.. code-block:: html

    data: {{ to_template['data'] }}
    next button: <a href=".../?cursor={{ to_template['cursor_next'] }}&direction=True">next</a>
    prev button: <a href=".../?cursor={{ to_template['cursor_prev'] }}&direction=False">prev</a>

What about *reverse* param? If False last item in DB will be first (like newspapers, comments, etc). If True last item in DB will be honestly last.

Simply. Also see the source code.
