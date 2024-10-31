#  Day 71 - Advanced - Deploying Your Web Application

## I dropped the project, too many conflicts 
### Couldn't fix it. There are better projects out there

````bash
Traceback (most recent call last):
  File "s:\path\to\main.py", line 2, in <module>
    from flask import Flask, abort, render_template, redirect, url_for, flash
  File "C:\path\to\AppData\Local\Programs\Python\Python311\Lib\site-packages\flask\__init__.py", line 14, in <module>
    from jinja2 import escape
  File "C:\path\to\AppData\Local\Programs\Python\Python311\Lib\site-packages\jinja2\__init__.py", line 12, in <module>
    from .environment import Environment
  File "C:\path\to\AppData\Local\Programs\Python\Python311\Lib\site-packages\jinja2\environment.py", line 25, in <module>
    from .defaults import BLOCK_END_STRING
  File "C:\path\to\AppData\Local\Programs\Python\Python311\Lib\site-packages\jinja2\defaults.py", line 3, in <module>
    from .filters import FILTERS as DEFAULT_FILTERS  # noqa: F401
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\path\to\AppData\Local\Programs\Python\Python311\Lib\site-packages\jinja2\filters.py", line 13, in <module>
    from markupsafe import soft_unicode
ImportError: cannot import name 'soft_unicode' from 'markupsafe' (C:\path\to\AppData\Local\Programs\Python\Python311\Lib\site-packages\markupsafe\__init__.py)
````