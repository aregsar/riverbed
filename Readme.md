A-Riverbed Repo Cloning to setup a new project

Prerequisites:

- setup a completely empty repo on github named yourapp
- install git
- install python
- install virtualenv
- install npm


Create a new app by cloning and modifying riverbed:

- git clone git@github.com:aregsar/riverbed.git yourapp
- cd yourapp
- rm -rf .git
- cp .env.example .env
- virtualenv -p $(which python) venv
- source venv/bin/activate
- pip install -r requirements.txt
- pip freeze > requirements.txt
- npm install
- bower install
- python manage.py runserver
- deactivate
- git init
- git add -A
- git commit -m "first commit"
- git remote add origin git@github.com:yourname/yourapp.git
- git remote -v
- git push -u origin master

--------------------------------------------------------------------

B-Setup a deployment pipeline on heroku

Prerequisites:

- You have a flask appplication committed to a local git repository(Part A)
- You have the heroku cli installed

https://devcenter.heroku.com/articles/heroku-command#installing-the-heroku-cli

-- heroku update
-- heroku --version
-- which heroku

- you have the heroku pipelines pluging installed

heroku plugins:install heroku-pipelines


Create the Heroku deployment pipeline:

- cd yourapp
- heroku login
- heroku create yourapp --buildpack git://github.com/heroku/heroku-buildpack-python.git
- #heroku buildpacks:set -a yourapp git://github.com/heroku/heroku-buildpack-python.git
- heroku apps
- git push heroku master
- heroku ps:scale web=1:hobby -a yourapp
- heroku logs --tail -a yourapp
- heroku ps
- heroku open
- heroku fork --from yourapp --to yourapp-staging
- heroku apps
- heroku apps:info -a yourapp-staging
- git remote add yourapp-staging git@heroku.com:yourapp-staging.git
- heroku addons:destroy ssl -a yourapp-staging
- heroku apps:info -a yourapp-staging
- git remote -v
- git remote rm heroku
- git remote -v
- git push yourapp-staging master
- heroku ps:scale web=1:hobby -a yourapp-staging


- heroku pipelines:create -a yourapp
- #heroku pipelines:create yourapp -a yourapp -s production
- heroku pipelines:add yourapp -a yourapp-staging -s staging
- heroku pipelines:list
- heroku pipelines:info yourapp


- #make a code change then push to staging and promote
- git push yourapp-staging master
- heroku pipelines:promote -a yourapp-staging
- heroku pipelines
- heroku pipelines:diff


