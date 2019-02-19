from flask import render_template
from oselab import app
from oselab.utils import build_page_title
from datetime import datetime

@app.context_processor
def inject_view_helpers():
    return dict(now=datetime.utcnow(), title=build_page_title())

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
    return render_template('home/about.html', title=build_page_title('About'))

@app.route('/faq')
def faq():
    """
    Show the FAQ page
    """
    return render_template('faq/faq.html', title=build_page_title('FAQ'))

@app.route('/bootcamp/comments')
def bootcamp_comments():
    """
    Show the boot camp comments page
    """
    return render_template('bootcamp/comments.html', title=build_page_title('Boot Camp Comments'))

@app.route('/gallery')
def gallery():
    """
    Serve up the gallery page
    """
    return render_template('gallery/index.html', title=build_page_title('Gallery'))


@app.route('/gallery/marginal_effective_corporate_taxes')
def marginal_effective_corporate_taxes():
    """
    Serve up the Marginal Effective Tax Rates on Corporate Investments viz
    """
    return render_template('gallery/marginal_effective_corporate_taxes.html', title=build_page_title('Marginal Effective Tax Rates on Corporate Investments'))


@app.route('/gallery/overlapping_generations')
def overlapping_generations():
    """
    Serve up the overlapping generations viz
    """
    return render_template('gallery/overlapping_generations.html', title=build_page_title('Overlapping Generations'))


@app.route('/gallery/tax_increase_decrease')
def increase_decrease():
    """
    Serve up the tax_increase_decrease viz
    """
    return render_template('gallery/tax_increase_decrease.html')

@app.route('/blog/<post>')
def blog_post(post):
    """
    Serve up the given blog post
    """
    return render_template(f"blog/posts/{post}.html", title=build_page_title('Blog'))
