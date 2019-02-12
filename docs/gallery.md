# Gallery

## How to add a new visualization

### Add a new route for your visualization

in `views.py`, add a new route for your visualization. It will look something like this:

```python
@app.route('/gallery/my_viz')
def my_viz():
    """
    Serve up my_viz
    """
    return render_template('gallery/my_viz.html', title=build_page_title('My viz'))
```

Once you have told Flask how to render the route, create a new file for the associated template (`gallery/my_viz.html` in the above example) and move onto the next step.

### Create the visualization and export it as static markup

Your visualization should be as static as possible. To avoid slowing down the website at all, try to export your visualization as an independent html file.

> Your visualization should also manage its own dependencies and it should not add a dependency for every page of the rest of the site. For example, if your visualization depends on Bokeh 10.6, add the source of Bokeh 0.10.6 to `static/vendor/javascript` and reference it in _just_ the template for your new visualization

Here is a sample of what your visualization template might look like:

```jinja2
{% extends "layout.html" %}
{% block body %}

<!-- Uses bokeh 0.12.7–replace these with your visualization's dependencies -->
<link rel="stylesheet" href="{{ url_for('static', filename='vendor/css/bokeh-0.12.7.min.css') }}" type="text/css">
<script type="text/javascript" src="{{ url_for('static', filename='vendor/javascript/bokeh-0.12.7.min.js') }}"></script>

{{
  page_heading(
    title="My visualization",
    body="A brief description of the visualization",
  )
}}

<div class="container py-5">
  <div id="viz-root"></div>
</div>

<script type="text/javascript">
// your visualization should have static javascript that powers it.
</script>

{% endblock %}
```

### Add your visualization to the Gallery index

Finally, you will want to add a link to your visualization from the gallery index. This is made easy with the [`gallery_item`](https://github.com/OpenSourceEcon/oselab/blob/master/oselab/templates/components/gallery_item.html) macro:

```jiinja
{{
  gallery_item(
    title="My viz",
    body="""
      Some kind of description
      """,
    url="/gallery/my_viz",
    image=url_for('static', filename="images/my_viz.png"),
  )
}}
```

The `url` property is the url you put in the call to `@app/route` in step 1. Add an image of your visualization to reference it in the `image` prop (750x750px is best).
