#!/usr/bin/env python
from langtools.translator.EPUBTranslation import EPUBTranslation
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def chapters():
    chapter_list = EPUBTranslation("../resources/821ejdacrz.epub").chapters
    return render_template('show_entries.html', chapters=chapter_list)

def chapter('/')


if __name__ == '__main__':
    app.run()