from flask import render_template
from osmlab import app
from datetime import datetime

@app.context_processor
def inject_view_helpers():
    return {'now': datetime.utcnow()}

@app.route('/')
def homepage():
    """
    Shows the user the homepage
    """
    return render_template('home/index.html')


@app.route('/gallery')
def gallery():
    """
    Serve up the gallery page
    """
    return render_template('gallery/gallery.html')


@app.route('/gallery/bubble-plot')
def bubbleplot():
    """
    Serve up the bubble plot
    """
    return render_template('gallery/bubbleplot/bubbleplot.html')


@app.route('/gallery/surf3Dtime')
def surf3Dtime():
    """
    Serve up the surf3Dtime viz
    """
    return render_template('gallery/surf3Dtime/surf3Dtime.html')


@app.route('/gallery/increase-decrease')
def increase_decrease():
    """
    Serve up the increase-decrease viz
    """
    return render_template('gallery/increase-decrease/increase-decrease.html')
