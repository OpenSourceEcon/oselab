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

@app.route('/bootcamp/2019')
def bootcamp_2019():
    """
    Show the 2019 bootcamp page
    """
    return render_template('/bootcamp/2019.html', title=build_page_title('2019 Boot Camp'))

@app.route('/bootcamp/current')
def bootcamp_current():
    """
    Show the current bootcamp status page
    """
    return render_template('/bootcamp/current.html', title=build_page_title('Current OSE Lab Boot Camp status'))

@app.route('/bootcamp/application_form')
def bootcamp_application_form():
  """
  The bootcamp application form
  """
  return render_template('/bootcamp/application_form.html', title=build_page_title('Boot Camp Application Form'))

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

@app.route('/gallery/fedfundsplot')
def fedfundsplot():
    """
    Serve up the U.S. federal funds effective rate and target plot
    """
    return render_template('gallery/fedfundsplot.html',
                           title=build_page_title('U.S. Federal Funds Effective Rate and Target Plot'))

@app.route('/gallery/tseries_pubdebt_gdp_frcsts')
def tseries_pubdebt_gdp_frcsts():
    """
    Serve up the comparison of CBO debt-to-GDP forecasts plot viz
    """
    return render_template('gallery/tseries_pubdebt_gdp_frcsts.html',
                           title=build_page_title('Comparison of CBO U.S. Debt-to-GDP Forecasts'))

@app.route('/gallery/usgdp_npp')
def usgdp_npp():
    """
    Serve up the U.S. real GDP normalized peak plot viz
    """
    return render_template('gallery/usgdp_npp.html',
                           title=build_page_title('U.S. Real GDP Normalized Peak Plot'))

@app.route('/gallery/usempl_npp')
def usempl_npp():
    """
    Serve up the US total nonfarm employment normalized peak plot viz
    """
    return render_template('gallery/usempl_npp.html',
                           title=build_page_title('U.S. Total Nonfarm Employment Normalized Peak Plot'))

@app.route('/gallery/djia_npp')
def djia_npp():
    """
    Serve up the DJIA normalized peak plot viz
    """
    return render_template('gallery/djia_npp.html',
                           title=build_page_title('DJIA Normalized Peak Plot'))

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

@app.route('/tutorials')
def tutorials():
    """
    Serve up the tutorials page
    """
    return render_template('tutorials/index.html',
                           title=build_page_title('Tutorials'))

@app.route('/blog/<post>')
def blog_post(post):
    """
    Serve up the given blog post
    """
    return render_template(f"blog/posts/{post}.html", title=build_page_title('Blog'))
