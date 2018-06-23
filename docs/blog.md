# Blog Posts

All blog posts should exist in the `posts` directory and will be automatically available at a route matching their filename. For example, a blog post written in `posts/my_example_post.html` would be available at the url `/blog/my_example_post`.

## Basic structure

Each blog post file is simply a Jinja template, so it can style itself as it pleases. Most blog posts, however, will want to use the following pattern:

```jinja
{% extends "blog/post.html" %}

{% block title %}
  {{
    page_heading(
      title="Your post's title"
      body="An optional sub-heading"
    )
  }}
{% endblock %}

{% block post %}
{% filter markdown %}

Write your post here! You can use _markdown_ as you please.

{% endfilter %}
{% endblock %}
```

To break this down further:

* Extend the blog post layout (which, in turn, extends the application layout for consistency)
* Add a title using the `page_heading` macro
* Populate the `post` block with your post's content. Filter the content with the `markdown` filter so you can use markdown. The markdown filter will also accept plain HTML for when markdown is not quite enough.
