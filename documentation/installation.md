# Installation

### Linux environment

*For now the installation instruction is only for Linux* 

##### Cloning from git to local machine

You should have git in use. Clone the project from github by using the command in terminal:

```
git clone https://github.com/mrasola/keskustelufoorumi.git destinationdir
```

Once cloned you can modify the code as you please. Before that, however, install 
requirements using:

```
pip intall -r requirements.txt
```

Requirements are found in requirements.txt. The requirements.txt contains
versions used in developing the application. The app might work on other versions
but there are no guarantees.


##### Pushing to Heroku for usage

For this you require [PostgreSQL database system](https://www.postgresql.org/) and 
[Heroku client](https://devcenter.heroku.com/articles/heroku-cli). After installing 
these you can move the application to heroku. The steps are as follows, and 
assume you have a Heroku account. First create a spot for the app in Heroku:

````
heroku create individualNameForApp
```` 
After this add the knowledge of Heroku to your local version control:

````
git remote add heroku https://git.heroku.com/individualNameForApp.git
````
Now Heroku needs a database to use with the application. Add the environment 
variable for the app to know it operates in Heroku as:

````
heroku config:set HEROKU=1
````

Crate a database in Heroku with:

````
heroku addons:add heroku-postgresql:hobby-dev
````
And use:

````
git add .
git commit -m "Heroku commit"
git push heroku master
````

to push to Heroku. 