title: Custom Direct Template

### prjct.html

```html+jinja
{% extends "base.html" %}

{% block title %}prjct Overview - {{ SITENAME }}{%endblock%}}

{% block breadcrumbs %}
    {% if DISPLAY_BREADCRUMBS %}
    <ol class="breadcrumb">
        <li><a href="{{ SITEURL }}" title="{{ SITENAME }}"><i class="fa fa-home fa-lg"></i></a></li>
        <li class="active">prjct</li>
    </ol>
    {% endif %}
{% endblock %}

{% block content %}
    <section id="content">
        <h1>prjct</h1>
        <p>All projects, with their next action items:</p>

        <div class="prjct-projects-list">
        {% for my_project in PRJCT_PROJECTS | sort %}
            {% set my_project = my_project.lower() %}
            <div class="row">
                <div class="prjct-projects-title col-xs-4 col-sm-3">
                    <a name="{{ my_project }}"></a>
                    <a href="{{ SITEURL -}} / {{- TAG_URL | replace('{slug}', my_project | replace("'", "") | lower) }}">
                        {{- my_project | string | replace('_', ' ') | titlecase -}}
                    </a>
                </div>
                <div class="prjct-projects-nextitem col-xs-7 col-sm-9">
                    {% if my_project in PRJCT_TODO %}
                        {{- PRJCT_TODO[my_project].split('\n')[1] | replace('<li class="prjct-task-list-item">', '') | replace('</li>', '') -}}
                    {% else -%}
                        &mdash;
                    {%- endif %}
                </div>
            </div>
        {% endfor %}
        </div>
    </section>
{% endblock %}
```
