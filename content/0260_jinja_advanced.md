title: Advanced Jinja
category: Pelican Pieces

### archives.html

```html+jinja
{% extends "base.html" %}

{% block title %}Archives - {{ SITENAME }}{% endblock %}

{% block breadcrumbs %}
    {% if DISPLAY_BREADCRUMBS %}
    <ol class="breadcrumb">
        <li><a href="{{ SITEURL }}" title="{{ SITENAME }}"><i class="fa fa-home fa-lg"></i></a></li>
        <li class="active">Archives</li>
    </ol>
    {% endif %}
{% endblock %}

{% block content %}
    <section id="content">
        <h1>Archives for {{ SITENAME }}</h1>
        <div id="archives">
            {%- set last_year = None -%}
            {%- set last_month = None -%}
            {%- set last_day = None -%}

            {% for article in dates %}
                <div class="row">
                    {% if article.date.year != last_year %}
                        {% if last_year != None -%}
                            <div class="archives-spacer col-xs-12">&nbsp;</div>
                            <div class="archives-spacer col-xs-12">&nbsp;</div>
                        {%- endif %}
                        <div class="archives-date archives-year col-xs-4 col-sm-2 col-sm-offset-2">
                            <a name="{{ article.date.year }}"></a>
                            {{- article.date.year -}}
                        </div>
                        <div class="archives-title col-xs-7 col-sm-6">
                            &nbsp;
                        </div>
                        {%- set last_year = article.date.year -%}
                        {%- set last_month = None -%}
                        {%- set last_day = None -%}
                    {% endif %}
                    {% if article.date.month != last_month %}
                        {% if last_month != None -%}
                            <div class="archives-spacer col-xs-12">&nbsp;</div>
                        {%- endif %}
                        <div class="archives-date archives-month col-xs-4 col-sm-2 col-sm-offset-2">
                        <a name="{{ article.date.year }}-{{ article.date.month }}"></a>
                            {{- article.date|strftime('%B') -}}
                        </div>
                        <div class="archives-title col-xs-7 col-sm-6">
                            &nbsp;
                        </div>
                        {%- set last_month = article.date.month -%}
                        {%- set last_day = None -%}
                    {% endif %}

                    <div class="archives-date categories-timestamp col-xs-4 col-sm-2 col-sm-offset-2">
                        {%- if last_day != article.date.day %}
                            <time datetime="{{ article.date.isoformat() }}">{{ article.date | strftime('%a %-d') }}</time>
                        {% else -%}
                            &nbsp;
                        {%- endif -%}
                    </div>
                    <div class="archives-title col-xs-7 col-sm-6">
                        <a href="{{ SITEURL }}/{{ article.url }}">{{ article.title }}</a>
                        {% if article.subtitle %}<br />{{ article.subtitle }}{% endif %}
                    </div>
                    {%- set last_day = article.date.day %}
                </div>
            {% endfor %}
        </div>
    </section>
{% endblock %}
```
