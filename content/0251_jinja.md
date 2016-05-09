title: Jinja: Templating Engine for Pelican

![Jinja2 Logo]({filename}images/jinja.png)

### layout.html

```html+jinja
<html>
    <head>
        <title>{% block title %}{% endblock %}</title>
    </head>
    <body>
        {% block body %}{% endblock %}
    </body>
</html>
```

### users.html

```html+jinja
{% extends "layout.html" %}

{% block title -%}
    All Users
{%- endblock %}

{% block body %}
    <ul>
    {% for user in users %}
        <li><a href="{{ user.url }}">{{ user.username }}</a></li>
    {% endfor %}
    </ul>
{% endblock %}
```
