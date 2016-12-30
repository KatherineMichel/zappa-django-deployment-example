# Zappa Django Deployment Example

Files from initial deployment of [Zappa](https://github.com/Miserlou/Zappa) using Django

## Instructions

* Set up AWS account and properly install AWS credentials file
* Create GitHub repo, clone it, and cd into root folder
* Ensure you are using Python 2.7 version (I'm using 2.7.12 via pyenv)
* Create your working environment (zappa-django-deployment-example-env)
* Install Django (`$ pip install django`)
* cd out of project root folder

### Create Project

    $ django-admin.py startproject core zappa-django-deployment-example

### Zappa

cd into project root folder, configure project settings to your liking

    $ pip install zappa
    $ pyenv local zappa-django-deployment-example-env
    $ zappa init (you will need to have S3 bucket name ready)
    $ zappa deploy production
    $ zappa update production (as needed)
    
### Live

Application will now be live. Note, AWS URL + environment name will be root and will prepend non-index template names. Example index: https://mb7zkt4j7l.execute-api.us-east-1.amazonaws.com/production

If your template content renders, you're golden :)

### Push to GitHub

    $ git init (not needed if repo was cloned)
    $ git add .
    $ git commit -m "Message"
    $ git push origin master
