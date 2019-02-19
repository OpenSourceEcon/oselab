# Deploying `oselab`

The `oselab` website runs on [Heroku](www.heroku.com). If you do not have access to the OSE Lab organization, ask someone to add your account. This project is deployed to the `oselab` app.

To get set up to trigger deploys, [download the Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line) and run `heroku git:remote -a oselab`.

Finally, to start a new deploy, run `git push heroku master`. Heroku will receive the event and deploy the new `oselab.org` website.
