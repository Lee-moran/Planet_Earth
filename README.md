
# Project 4 Blog Site
Full-Stack Toolkit
Project purpose:
This site is a blog style news site, aimed to let users keep up with the fast changing world problems
In this project, ive built a Full-Stack site based on business logic used to control a centrally-owned dataset. Set up an authentication mechanism and provide role-based access to the site's data or other activities based on the dataset.

### Main Technologies
- HTML, CSS, JavaScript, Python+Django
- Relational database (recommending MySQL or Postgres)

### Site owner main objectives 
- to inform users about whats happening to the planet
- to educate users about the Planet, what can they do to help
- to increase users interests and curiosity on the affects harming the planet
- to provide a platform for users to share posts, comments and interact with each other
- to create a community with people that has common interests in saving the planet 

### Features to include:
- Posts can be up/downvoted
- Comments can be left on a post
- Time/Date of posting
- Topic groupings/categories

### Site user main objectives 
- to keep up with planet news
- to meet other like mined people 
- to interact and discuss with others on specific topics 
- to learn from each other about different problems globally
- to share posts, ideas, opinions with people who understand you 
- to show your passion to other people who dont know alot about it and want to learn.
- to post, read and comment on news stories.

## WHY THIS
This has been an ongoing problem for the planet, and since the world has reopened from covid pandemic we have put aside the real issue on saving our planet. surely if we caused these disasters we can fix them. This is why we need everyone todo there part.

Scientists say eight years left to avoid worst effects.” : “IPCC climate report gives us 10 years to save the world.” 22-jan-2022

The massive melting of glaciers as a result of global heating has caused marked shifts in the Earth's axis of rotation since the 1990s,

Global sea level rise accelerated since 2013 to a new high in 2021, with continued ocean warming and ocean acidification.

I decided to build this project, because I personally believe this is our future, and I would like more people to be aware of this, get interested and try to understand it. For those who have the same interests as me, I hope this site can be a place to share and exchange information, knowledge and opinions about the planet and how we all can make a difference.

Consumers who come to the site are greated depending on there loged in status or not. Being a member of the site gives you more accessibility being able to write, like and comment on individual blogs. 

Eg) Not logged in

<img width="1280" alt="logged out" src="https://user-images.githubusercontent.com/92300148/180831938-980289a5-3cb8-4d0a-b94c-24db8a4512ba.png">
<img width="1272" alt="not loged in" src="https://user-images.githubusercontent.com/92300148/180831920-4b45cc6c-c6b1-4e57-8960-81a244a420d0.png">

Eg) Logged in
<img width="1233" alt="logged in" src="https://user-images.githubusercontent.com/92300148/180832197-019fc69d-3822-4d11-ae49-76504723a0fd.png">
<img width="1279" alt="User already loged in " src="https://user-images.githubusercontent.com/92300148/180832206-cf327ade-81fc-423d-8e68-bbfae78abc18.png">

 

## User stories:
1) As a Site User I can view a list of posts so that I can select one to read
2) As a Site User I can click on a post so that I can read the full text
3) As a Site User / Admin I can view the number of likes on each post so that I can see which is the most popular or viral
4) As a Site User / Admin I can view comments on an individual post so that I can read the conversation
5) As a Site User I can register an account so that I can comment and like
6) As a Site User I can leave comments on a post so that I can be involved in the conversation
7) As a Site User I can like or unlike a post so that I can interact with the content
8) As a Site Admin I can create, read, update and delete posts so that I can manage my blog content
9) As a Site Admin I can create draft posts so that I can finish writing the content later
10) As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments
11) As Site User i can create a post so that others can views my opinion on relevant topics
12) As a Site User i can view a paginated list of posts so that easily select which post to view
13) As Site User i can create blogs so that i can share my views on relevant topics aswell
14) As  Site user i can maintain the quality of material being read so that the reader has fresh material


## Wirerframes 
<img width="1424" alt="Wireframe" src="https://user-images.githubusercontent.com/92300148/180831309-11ddd33c-d113-4526-b79e-7fff20c23ddc.png">

- [live wireframe](https://lucid.app/lucidspark/eb631a3a-3a1f-4c98-a978-4a3a5971fb43/edit?viewport_loc=808%2C-849%2C5132%2C2368%2C0_0&invitationId=inv_1c43a584-275a-4ed4-b9ae-7b6584675b5e#)


## DataBase structure 
<img width="664" alt="DB structure" src="https://user-images.githubusercontent.com/92300148/180831042-74bc7de4-bb85-4652-a441-8922c6603096.png">

- [a link to live wireframe](https://lucid.app/lucidchart/4431c8b1-f218-41b9-858e-24ef8ad521df/edit?viewport_loc=-371%2C168%2C2501%2C921%2C0_0&invitationId=inv_fa6de680-4a18-4d50-ad65-f42fc915c1cb#)


## Fonts and Color scheme 
Exo & Ubuntu are the primary fonts I wanted to use because there soft and complamentarty. Giving of a sense of peace. the stroke in these font work well together. 
- [Exo](https://fonts.google.com/?query=exo&preview.text=Planet%20Earth%20&preview.layout=row&preview.text_type=custom)
- [Ubuntu](https://fonts.google.com/specimen/Ubuntu?query=ub&preview.text=Planet%20Earth%20&preview.layout=row&preview.text_type=custom)

As a fall back I used ***Roboto and lato***  which is a front i used before and lato as well as the standard sans serif. Good idea to have a fall back so your content is viewable.

In terms of the color scheme I went with something slightly different. I used the planet as inspiration. I think these colors bring warmth and a real feel for the earth with the browns blues and greens.
- [colors](https://icolorpalette.com/imagepalette/color-palette-ideas-from-sphere-wood-macro-photography-image)

<img width="367" alt="color palette " src="https://user-images.githubusercontent.com/92300148/180831474-2ae6c06c-a3bc-4aec-b569-12d745786cf3.png">

## Testing 
Jigsaw CSS validator
Nu Html checker 
Pep8 

## Installations
Below are the installations we need before writing any code

Install the server to use when deploy on Heroku
```bash
pip3 install django gunicorn
```

Supporting libraries:
``` bash
Postgresql and psycopg2
pip3 install dj_database_url psycopg2
```

Run Cloudinary
``` bash
pip3 install dj3-cloudinary-storage
```

Create file list:
Create requirement.txt
``` bash
pip3 freeze --local > requirements.txt
```

Create new django project:
```bash
django-admin startproject Filename:
```

Create blog app
```bash
python3 manage.py startapp blog
```

## Issues resolved
Your Blogs page has an edit and delete button. Delete btn wouldnt work due to its properties.
I had 2 properties instead of 3 for Bootstrap 5.

## Deployment

This project was developed using a [GitPod](https://gitpod.io/ "Link to GitPod") workspace. The code was commited to [Git](https://git-scm.com/ "Link to Git") and pushed to [GitHub](https://github.com/ "Link to GitHub") using the terminal.

### Deploying on Heroku
To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. Create the Heroku App:
    - Select "Create new app" in Heroku.
    - Choose a name for your app and select the location.

2. Attach the Postgres database:
    - In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.

3. Prepare the environment and settings.py file:
    - In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
    - In your GitPod workspace, create an env.py file in the main directory. 
    - Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
    - Add the SECRET_KEY value to the Config Vars in Heroku.
    - Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
    - Update the Config Vars with the Cloudinary url, adding into the settings.py file also.
    - In settings.py add the following sections:
        - Cloudinary to the INSTALLED_APPS list
        - STATICFILE_STORAGE
        - STATICFILES_DIRS
        - STATIC_ROOT
        - MEDIA_URL
        - DEFAULT_FILE_STORAGE
        - TEMPLATES_DIR
        - Update DIRS in TEMPLATES with TEMPLATES_DIR
        - Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']

4. Store Static and Media files in Cloudinary and Deploy to Heroku:
    - Create three directories in the main directory; media, storage and templates.
    - Create a file named "Procfile" in the main directory and add the following:
        - web: gunicorn project-name.wsgi
    - Log in to Heroku using the terminal heroku login -i.
    - Then run the following command: **heroku git:remote -a your_app_name_here** and replace your_app_name_here with the name of your Heroku app. This will link the app to your Gitpod terminal.
    - After linking your app to your workspace, you can then deploy new versions of the app by running the command **git push heroku main** and your app will be deployed to Heroku.

## Reference:
- [lucid](https://lucid.app/) - "database structure and wirerframes"
- [pexel](https://www.pexels.com/) "images"
- [bootstrap](https://getbootstrap.com/)
- [stackoverflow](https://stackoverflow.com/)
- [Django Docs](https://docs.djangoproject.com/en/3.2/)
- [Summernote GitHub Docs](https://github.com/summernote/summernote,)
- [Cripsy Forms Docs](https://django-crispy-forms.readthedocs.io/en/latest/)
- CodeInstitute - "I Think Therefore I Blog"



I have to give a shout out the the tutuor suppport also for there help.