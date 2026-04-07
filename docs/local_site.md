# Rendering the site locally

When you have updated the code for the site in the repository on your local machine, you will want to test the site to make sure it has the functionality you want. The simplest way to do this is to use Python's built-in HTTP server.

- Run `python build.py` first from the root directory if you have made template changes
- Navigate to the `site/` directory in your terminal: `cd site`
- Initiate a Python built-in server: `python -m http.server 8000`
- In your browser, open http://localhost:8000
- Run `python build.py` from the root directory if you have made template changes
- Refresh browser window after any changes

Once you are done using the site on the local server, close the browser window and terminate the browser in your terminal using `CMD-c`.
