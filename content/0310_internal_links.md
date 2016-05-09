title: Pelican Internal Links

```
yourproject/
    ├── content/
    │   ├── article1.rst
    │   ├── cat/
    │   │   └── article2.md
    │   ├── images
    │   │   └── han.jpg
    │   └── pages/
    │   │   ├── about.md
    │   │   └── (other articles)
    │   └── (other articles)
    ├── output
    ├── develop_server.sh
    ├── fabfile.py
    ├── Makefile
    ├── pelicanconf.py       # Main settings file
    └── publishconf.py       # Settings to use when ready to publish
```

It is now possible to specify intra-site links to files in the *source content* hierarchy instead of files in the *generated* hierarchy.

### article2.md

```markdown
Title: The second article
Date: 2012-12-01 10:02

See below intra-site link examples in Markdown format.

[a link relative to the current file]({filename}../article1.rst)
[a link relative to the content root]({filename}/article1.rst)

![Alt Text]({filename}/images/han.jpg)
```

- [Article 1]({filename}article1.rst)
- [Article 2]({filename}cat/article2.md)

