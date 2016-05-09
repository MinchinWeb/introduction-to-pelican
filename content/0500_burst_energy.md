title: Example 2: Burst Energy

- [Example]({filename}/webpages/burstenergy/localhost+8001/index.html)
- formerly a production site
- I'd generate locally and then send a zip file to the hosting provider
- used *Invoke* to automate site generation
- use automation to generate graphs for the site as part of the build process (before running Pelican)
- use automation to generate javascript files needed elsewhere (after running Pelican)
- use automation to make sure the zip file is a consistent format

### tasks.py

```python
# Altered fabfile to use with Invoke
from invoke import run, task

# from fabric.api import *
# import fabric.contrib.project as project
import os
# import sys
# import SimpleHTTPServer
# import SocketServer
import zipfile
from build_js import build_js
from floating_rate_vs_rro_graph import make_graph

# Local path configuration (can be absolute or relative to fabfile)
env_deploy_path = 'output'
env_zipfile = 'burstenergy.zip'


@task
def clean():
    if os.path.isdir(env_deploy_path):
        run('rm -rf ' + env_deploy_path)
        run('mkdir ' + env_deploy_path)


@task
def build():
    run('pelican -s pelicanconf.py')
    build_js()
    make_graph()


@task
def rebuild():
    clean()
    build()


@task
def regenerate():
    run('start pelican -r -s pelicanconf.py')
    build_js()
    make_graph()


@task
def serve():
    run('cd ' + env_deploy_path + ' && start python -m http.server')


@task
def reserve():
    build()
    build_js()
    make_graph()
    serve()


@task
def preview():
    run('pelican -s publishconf.py')


@task
def build_zip():
    zipf = zipfile.ZipFile(env_zipfile, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(env_deploy_path):
        for file in files:
            absfile = os.path.join(root, file)
            zfile = absfile[len(env_deploy_path)+len(os.sep):]  # relative path
            zipf.write(absfile, zfile)
    zipf.close()


@task
def zip():
    clean()
    build()
    build_zip()


@task
def develop():
    clean()
    regenerate()
    serve()


@task
def build_dieppe():
    run('pelican -s pelicanconf-dieppe.py')


@task
def less():
    run('lessc theme\\burst-energy\\less\\bootstrap.burst-energy.less > ' +
        env_deploy_path + '\\css\\style.css')
    #   lessc theme\burst-energy\less\bootstrap.burst-energy.less > output\css\style.css


@task
def take_screenshot():
    from ghost import Ghost

    url = "http://localhost:8000"
    gh = Ghost()

    # We create a new page
    page, page_name = gh.create_page()

    # We load the main page of ebay
    page_resource = page.open(url, wait_onload_event=True)

    # Save the image of the screen
    page.capture_to("burst-energy.png")

```

### build_js.py

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

'''
This builds the JavaScript files that are used by the MySecure content.

Build the site first, then this will put the JS files in the output directory.
'''


def build_js():
    from pelicanconf import OUTPUT_PATH
    from bs4 import BeautifulSoup
    import os
    import re
    import codecs

    'configuration'
    'form file'
    FORM_FILE = (os.path.dirname(os.path.realpath(__file__)) + os.sep +
                 OUTPUT_PATH + os.sep)
    FORM_FILE += 'mysecure' + os.sep + 'signup.html'

    'output directory'
    JS_PATH = (os.path.dirname(os.path.realpath(__file__)) + os.sep +
               OUTPUT_PATH + os.sep + 'js')

    'Placeholder text'
    placeholder = 'PLACEHOLDER'

    "test existence of 'form file'"

    with open(FORM_FILE, "r") as FORM_FILE_HANDLE:
        soup = BeautifulSoup(FORM_FILE_HANDLE, "lxml")

    "create `title.js`"
    "document title"
    with open(JS_PATH + os.sep + 'title.js', "w") as TITLE_JS:
        print("var titleblock = ''", file=TITLE_JS)
        print("titleblock += '{}'".format(soup.title), file=TITLE_JS)
        print("", file=TITLE_JS)
        # ToDo: Select the title dynamically,
        #                               based on the file it's called from"

        "meta -- viewport"
        viewport = soup.find('meta', {'name': 'viewport'})
        print("titleblock += '{}'".format(viewport), file=TITLE_JS)
        print("", file=TITLE_JS)

        #  link to css
        # css_files = soup.findAll('link',{'rel':'stylesheet'})
        # for css in css_files:
        #   print ("titleblock += '{}'".format(css), file = TITLE_JS)

        print("document.write(titleblock);", file=TITLE_JS)

    "create `header.js` and `footerinfo.js`"
    on_header = True
    my_re2 = re.compile('</?body>')
    my_re4 = re.compile(placeholder)
    on_header = True
    with codecs.open(JS_PATH + os.sep + 'header.js', "w", "utf-8") \
            as HEADER_JS:
        with codecs.open(JS_PATH + os.sep + 'footerinfo.js', "w", "utf-8") \
                as FOOTER_JS:
            print("var headerblock = ''", file=HEADER_JS)
            print("var footerblock = ''", file=FOOTER_JS)
            for line in str(soup.find('body')).split('\n'):
                line2 = my_re2.sub('', line)
                if my_re4.search(line2):
                    on_header = False
                    line2 = ''
                if on_header:
                    print("headerblock += '{}'".format(line2), file=HEADER_JS)
                else:
                    print("footerblock += '{}'".format(line2), file=FOOTER_JS)
            print("document.write(headerblock)", file=HEADER_JS)
            print("document.write(footerblock)", file=FOOTER_JS)

if __name__ == "__main__":
    build_js()
```

### floating_rate_vs_rro_graph.py

```python
#   This generated the graph show the comparision between the RRO and our
#   floating rate.
#   This graph is displayed on https://www.burstenergy.ca/rates/floating/


Months = ['2014-01', '2014-02', '2014-03', '2014-04', '2014-05', '2014-06', 
          '2014-07', '2014-08', '2014-09', '2014-10', '2014-11', '2014-12',
          '2015-01', '2015-02', '2015-03', '2015-04', '2015-05', '2015-06',
          '2015-07', '2015-08', '2015-09', '2015-10', '2015-11', '2015-12',
          '2016-01', '2016-02', '2016-03', '2016-04']

# both floating and RRO for Edmonton
RRO =    [ 8.689,     7.471,     6.991,     6.986,      8.922,    5.995,
           7.198,     8.021,     7.954,     8.737,      7.127,    7.545,
           7.302,     6.583,     5.431,     5.832,      4.337,    4.089,
           6.140,     5.813,     5.387,     5.498,      5.212,    5.489,
           5.304,     4.753,     4.521,     3.65]

Floating = [ 6.149,  11.730,     5.903,     4.438,      7.328,    5.909,
            15.801,   6.239,     3.710,     4.011,      5.378,    4.049,
             5.001,   4.831,     3.294,     3.282,      7.461,   13.218,
             3.692,   4.952,     3.327,     3.412,      3.403,    3.333,
             3.441,   2.907,     2.617,     2.503]

# NGX Spot Prices
NGX =    [3.8412,    5.4560,    5.1446,    4.4361,     4.4374,   4.3885,
          4.2005,    3.8446,    3.8608,    3.7947,     3.7084,   3.6218,
          3.0539,    2.7301,    2.7503,    2.5161,     2.5477,   2.5729,
          2.5976,    2.7783,    2.7699,    2.6217,     2.4256,   2.3347,
          2.3324,    2.0379,    1.5752,    1.3116]

NG_margin = 0.90


def make_graph(Months_Plotted=12):
    import os
    from pathlib import Path
    from statistics import mean

    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    from pylab import savefig
    from datetime import datetime
    # for nicer colours, importing is enough
    import seaborn as sns

    """Convert *Months* to numbers"""
    for i in range(len(Months)):
        year, month = map(int, Months[i].split('-'))
        Months[i] = mdates.date2num(datetime(year, month, 1))

    """drop last month on RRO if we have more data than for the floating"""
    if len(RRO) > len(Floating):
        my_RRO = RRO[:-1]
        my_Months = Months[:-1]
    else:
        my_RRO = RRO
        my_Months = Months
    my_Floating = Floating
    my_NG = [i + NG_margin for i in NGX]

    if len(my_Months) > Months_Plotted:
        my_Floating = my_Floating[-Months_Plotted:]
        my_RRO = my_RRO[-Months_Plotted:]
        my_Months = my_Months[-Months_Plotted:]
        my_NG = my_NG[-Months_Plotted:]

    # averages
    average_RRO = [mean(my_RRO) for i in my_Months]
    average_Floating = [mean(my_Floating) for i in my_Months]
    average_NG = [mean(my_NG) for i in my_Months]

    """Now let's plot!"""
    # make the final image 800px wide
    fig = plt.figure(dpi=72, figsize=(800/72/1.19, (800*1/2)/72/1.19))
    graph = fig.add_subplot(111)
    # Plot the two lines
    line_RRO = graph.plot(my_Months, my_RRO, sns.xkcd_rgb["pale red"], label="RRO")
    line_Burst = graph.plot(my_Months, my_Floating, sns.xkcd_rgb["medium green"], label="Burst Energy")
    #line_ave_RRO = graph.plot(my_Months, average_RRO, sns.xkcd_rgb["pale red"], label=None, linestyle='--')
    #line_ave_Burst = graph.plot(my_Months, average_Floating, sns.xkcd_rgb["medium green"], label=None, linestyle='--')


    # x axis -- list the months on the 1st
    graph.set_xticks(my_Months)
    graph.set_xticklabels([mdates.num2date(date).strftime("%b '%y") for date in my_Months])
    # y axis -- min is 0, label
    plt.ylim(ymin=0)
    plt.ylabel("\u00A2 / kWh, for Edmonton")
    # add legend
    graph.legend()

    # current file location (this script file)
    p = Path(os.path.realpath(__file__))
    # drop script file name
    p = p.parents[0]
    # location of where we want to save the graph
    # p = p / "content" / "images" / "floating-rate-vs-rro.png"
    p = p / "floating-rate-vs-rro.png"

    savefig(str(p), bbox_inches='tight')
    # plt.show()

    """Now let's plot (Natural Gas!"""
    # make the final image 800px wide
    fig = plt.figure(dpi=72, figsize=(800/72/1.19, (800*1/2)/72/1.19))
    graph = fig.add_subplot(111)
    # Plot the two lines
    #line_RRO = graph.plot(my_Months, my_RRO, sns.xkcd_rgb["pale red"], label="RRO")
    line_Burst = graph.plot(my_Months, my_NG, sns.xkcd_rgb["medium green"], label="Burst Energy")
    #line_ave_RRO = graph.plot(my_Months, average_RRO, sns.xkcd_rgb["pale red"], label=None, linestyle='--')
    #line_ave_Burst = graph.plot(my_Months, average_NG, sns.xkcd_rgb["medium green"], label=None, linestyle='--')


    # x axis -- list the months on the 1st
    graph.set_xticks(my_Months)
    graph.set_xticklabels([mdates.num2date(date).strftime("%b '%y") for date in my_Months])
    # y axis -- min is 0, label
    plt.ylim(ymin=0, ymax=6)
    plt.ylabel("$ / GJ, for Alberta")
    # add legend
    graph.legend()

    # current file location (this script file)
    p = Path(os.path.realpath(__file__))
    # drop script file name
    p = p.parents[0]
    # location of where we want to save the graph
    # p = p / "content" / "images" / "floating-rate-vs-rro.png"
    p = p / "natural-gas.png"

    savefig(str(p), bbox_inches='tight')
    # plt.show()


def averages(Months_Plotted=12):
    import statistics

    """drop last month on RRO if we have more data than for the floating"""
    if len(RRO) > len(Floating):
        my_RRO = RRO[:-1]
        my_Months = Months[:-1]
    else:
        my_RRO = RRO
        my_Months = Months
    my_Floating = Floating
    my_NG = [i + NG_margin for i in NGX]

    if len(my_Months) > Months_Plotted:
        my_Floating = my_Floating[-Months_Plotted:]
        my_RRO = my_RRO[-Months_Plotted:]
        my_Months = my_Months[-Months_Plotted:]
        my_NG = my_NG[-Months_Plotted:]

    ave_RRO = statistics.mean(my_RRO)
    ave_Floating = statistics.mean(my_Floating)
    ave_NG = statistics.mean(my_NG)

    print("For the last {} months, the average is:".format(Months_Plotted))
    print("{}For the RRO,           {:.3f} ¢/kWh".format("  ", ave_RRO))
    print("{}For the Floating rate, {:.3f} ¢/kWh".format("  ", ave_Floating))
    print("{}For natural gas,      ${:.2f} /GJ".format("  ", ave_NG))


if __name__ == "__main__":
    make_graph(12)
    averages(6)
    averages(12)
```

<!-- reveiw -->
