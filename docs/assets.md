# Assets

`oselab` uses an asset pipeline to build CSS and JavaScript into bundles for easier consumption by the client. This is a much better experience for the user, but does add a bit more complexity for the developer.

Assets are built using [Flask-Assets](https://flask-assets.readthedocs.io/en/latest/). Bundles are defined in [`config/assets.py`](https://github.com/OpenSourceEcon/oselab/blob/master/oselab/config/assets.py). You can reference static assets and use any options provided by `Flask-Assets` there.

`oselab` does not use Babel, SASS, or other pre-processors to keep maintenance simple and make code more straightforward for future maintainers who may not have as much front-end experience.
