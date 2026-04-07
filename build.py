#!/usr/bin/env python3
"""
Build the oselab.org static site from Jinja2 templates.

Usage:
    pip install jinja2 markdown
    python build.py

Outputs rendered HTML to site/ and copies static assets to site/assets/.
"""
import os
import re
import shutil
import textwrap
from datetime import datetime

import jinja2
import markdown as md_lib

ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(ROOT, "templates")
STATIC_DIR = os.path.join(ROOT, "static")
SITE_DIR = os.path.join(ROOT, "site")

# ---------------------------------------------------------------------------
# Route → URL mapping (mirrors Flask views.py)
# ---------------------------------------------------------------------------
ENDPOINT_MAP = {
    "homepage": "/",
    "about": "/about/",
    "gallery": "/gallery/",
    "tutorials": "/tutorials/",
    "bootcamp_current": "/bootcamp/current/",
    "bootcamp_comments": "/bootcamp/comments/",
    "bootcamp_2019": "/bootcamp/2019/",
    "bootcamp_application_form": "/bootcamp/application_form/",
    "faq": "/faq/",
    "fedfundsplot": "/gallery/fedfundsplot/",
    "tseries_pubdebt_gdp_frcsts": "/gallery/tseries_pubdebt_gdp_frcsts/",
    "usgdp_npp": "/gallery/usgdp_npp/",
    "usempl_npp": "/gallery/usempl_npp/",
    "djia_npp": "/gallery/djia_npp/",
    "marginal_effective_corporate_taxes": "/gallery/marginal_effective_corporate_taxes/",
    "overlapping_generations": "/gallery/overlapping_generations/",
    "increase_decrease": "/gallery/tax_increase_decrease/",
}


def url_for(endpoint, **kwargs):
    """Replaces Flask's url_for(). Static files map to /assets/..."""
    if endpoint == "static":
        return "/assets/" + kwargs["filename"]
    return ENDPOINT_MAP.get(endpoint, "/" + endpoint + "/")


# ---------------------------------------------------------------------------
# Template filters
# ---------------------------------------------------------------------------
def dedent_filter(s):
    return textwrap.dedent(s)


NOT_HANDLE_SAFE = re.compile(r"[^A-Za-z0-9\-]+")


def handleize_filter(s):
    handle = "-".join(s.lower().strip().split())
    return NOT_HANDLE_SAFE.sub("", handle)


def markdown_filter(s):
    return md_lib.markdown(
        s,
        extensions=[
            "tables",
            "attr_list",
            "smarty",
            "nl2br",
            "codehilite",
            "fenced_code",
        ],
    )


def build_page_title(page_title=""):
    if not page_title:
        return "Open Source Economics Laboratory"
    return f"Open Source Economics Laboratory | {page_title}"


# ---------------------------------------------------------------------------
# Page list: template path → (site output path, extra context)
# ---------------------------------------------------------------------------
PAGES = [
    (
        "home/index.html",
        "index.html",
        {"title": build_page_title()},
    ),
    (
        "home/about.html",
        "about/index.html",
        {"title": build_page_title("About")},
    ),
    (
        "faq/faq.html",
        "faq/index.html",
        {"title": build_page_title("FAQ")},
    ),
    (
        "bootcamp/current.html",
        "bootcamp/current/index.html",
        {"title": build_page_title("Current OSE Lab Boot Camp status")},
    ),
    (
        "bootcamp/2019.html",
        "bootcamp/2019/index.html",
        {"title": build_page_title("2019 Boot Camp")},
    ),
    (
        "bootcamp/application_form.html",
        "bootcamp/application_form/index.html",
        {"title": build_page_title("Boot Camp Application Form")},
    ),
    (
        "bootcamp/comments.html",
        "bootcamp/comments/index.html",
        {"title": build_page_title("Boot Camp Comments")},
    ),
    (
        "gallery/index.html",
        "gallery/index.html",
        {"title": build_page_title("Gallery")},
    ),
    (
        "gallery/fedfundsplot.html",
        "gallery/fedfundsplot/index.html",
        {"title": build_page_title("U.S. Federal Funds Effective Rate and Target Plot")},
    ),
    (
        "gallery/tseries_pubdebt_gdp_frcsts.html",
        "gallery/tseries_pubdebt_gdp_frcsts/index.html",
        {"title": build_page_title("Comparison of CBO U.S. Debt-to-GDP Forecasts")},
    ),
    (
        "gallery/usgdp_npp.html",
        "gallery/usgdp_npp/index.html",
        {"title": build_page_title("U.S. Real GDP Normalized Peak Plot")},
    ),
    (
        "gallery/usempl_npp.html",
        "gallery/usempl_npp/index.html",
        {
            "title": build_page_title(
                "U.S. Total Nonfarm Employment Normalized Peak Plot"
            )
        },
    ),
    (
        "gallery/djia_npp.html",
        "gallery/djia_npp/index.html",
        {"title": build_page_title("DJIA Normalized Peak Plot")},
    ),
    (
        "gallery/marginal_effective_corporate_taxes.html",
        "gallery/marginal_effective_corporate_taxes/index.html",
        {
            "title": build_page_title(
                "Marginal Effective Tax Rates on Corporate Investments"
            )
        },
    ),
    (
        "gallery/overlapping_generations.html",
        "gallery/overlapping_generations/index.html",
        {"title": build_page_title("Overlapping Generations")},
    ),
    (
        "gallery/tax_increase_decrease.html",
        "gallery/tax_increase_decrease/index.html",
        {"title": build_page_title("Tax Increase vs. Tax Decrease")},
    ),
    (
        "tutorials/index.html",
        "tutorials/index.html",
        {"title": build_page_title("Tutorials")},
    ),
]


def build():
    # Set up Jinja2 environment
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATES_DIR),
        autoescape=False,
        keep_trailing_newline=True,
    )
    env.filters["dedent"] = dedent_filter
    env.filters["handleize"] = handleize_filter
    env.filters["markdown"] = markdown_filter
    env.globals["url_for"] = url_for
    env.globals["now"] = datetime.utcnow()

    # Render each page
    for template_name, output_rel, context in PAGES:
        template = env.get_template(template_name)
        rendered = template.render(**context)

        output_path = os.path.join(SITE_DIR, output_rel)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(rendered)
        print(f"  Built: {template_name} → site/{output_rel}")

    # Copy static assets: oselab/static/ → site/assets/
    assets_dst = os.path.join(SITE_DIR, "assets")
    if os.path.exists(assets_dst):
        shutil.rmtree(assets_dst)
    shutil.copytree(STATIC_DIR, assets_dst)
    print(f"  Copied: oselab/static/ → site/assets/")

    # Ensure GitHub Pages config files exist
    nojekyll = os.path.join(SITE_DIR, ".nojekyll")
    if not os.path.exists(nojekyll):
        open(nojekyll, "w").close()

    cname = os.path.join(SITE_DIR, "CNAME")
    if os.path.isdir(cname):
        # Mistakenly created as a directory — remove and recreate as a file
        shutil.rmtree(cname)
    if not os.path.exists(cname):
        with open(cname, "w") as f:
            f.write("www.oselab.org\n")
    print(f"  GitHub Pages config: .nojekyll, CNAME")


if __name__ == "__main__":
    print("Building site...")
    build()
    print("Done.")
