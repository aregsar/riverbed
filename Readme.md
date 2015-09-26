A-River Bed Repo Cloning to setup a new project

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
- you have the heroku pipelines pluging installed


heroku plugins:install heroku-pipelines


Create the Heroku deployment pipeline:

- cd yourapp
- heroku login
- heroku apps:create yourapp
- heroku dyno:type web=hobby -a yourapp
- heroku apps
- git push heroku master
- heroku ps:scale web=1 -a yourapp
- heroku logs --tail -a yourapp
- heroku ps
- heroku open
- heroku fork --from yourapp --to yourapp-staging
- heroku apps
- heroku info -a yourapp-staging
- git remote add yourapp-staging git@heroku.com:yourapp-staging.git
- heroku addons:destroy ssl  -a yourapp-staging
- heroku info -a yourapp-staging
- git remote -v
- git remote rm heroku
- git remote -v
- git push yourapp-staging master
- heroku ps:scale web=1 -a yourapp-staging
- heroku pipelines:create -a yourapp
- heroku pipelines:add -a yourapp yourapp-staging
- #explicit add
- #heroku pipelines:add -a yourapp -s production
- #heroku pipelines:add -a yourapp-staging -s staging
- #make a code change then push to staging and promote
- git push yourapp-staging master
- heroku pipelines:promote -a yourapp-staging
- heroku pipelines
- heroku pipelines:diff


