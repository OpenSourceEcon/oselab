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

@app.route('/about')
def about():
    """
    Shows the about page
    """
    return render_template('home/about.html')

@app.route('/gallery')
def gallery():
    """
    Serve up the gallery page
    """
    return render_template('gallery/index.html')


@app.route('/gallery/marginal_effective_corporate_taxes')
def marginal_effective_corporate_taxes():
    """
    Serve up the Marginal Effective Tax Rates on Corporate Investments viz
    """
    return render_template('gallery/marginal_effective_corporate_taxes.html')


@app.route('/gallery/overlapping_generations')
def overlapping_generations():
    """
    Serve up the overlapping generations viz
    """
    return render_template('gallery/overlapping_generations.html')


@app.route('/gallery/tax_increase_decrease')
def increase_decrease():
    """
    Serve up the tax_increase_decrease viz
    """
    return render_template('gallery/tax_increase_decrease.html')
