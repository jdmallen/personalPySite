from flask import Flask, render_template, request, redirect, url_for, abort, session
from personalPySite import app

@app.route('/')
def home():
    return render_template('layout.html')