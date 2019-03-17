# Snippr

Snippr is a web-application done in Django and Vue.js. It mimics github but it forces the users to upload code as well and the users who'll comment on the issue are forced to change the code of the user. It highlights the changes in the user's code via the snipprcomparison package.
https://github.com/Zeshiba/snipprcomparison

## Requirements

- Python 3.x
- virtualenv and virtualenvwrapper
- NodeJS 8.x


## Running this app

```bash
# create and activate virtualenv
mkvirtualenv -p python3 [name of your virtualenv] -a .

# install dependencies
pip install -r requirements.txt
npm install

# django stuff
python manage.py collectstatic
python manage.py migrate

# run backend server
python manage.py runserver

# build and watch changes to frontend code
npm run build:watch
```


## Serving static files

After running `collectstatic`, all static files will be stored in the `static-root`
directory. This directory needs to be served separately using any file server,
although I would recommend using `nginx`.

Running `collecstatic` will store all static files into the `static-root` directory. This directory
needs to be served separately using any file server. In my case, I am using nginx.

```bash
sudo apt install nginx
# perform "Configure nginx" step in the next section

sudo service nginx restart
```

### Configure nginx

Create the file `/etc/nginx/sites-enabled/snippr` with the
following contents:

```
server {
    # you may use any available port that you want
    listen 9001;

    location / {
        add_header 'Access-Control-Allow-Origin' '*';
        autoindex on;

        # change the path to point to your own static-root
        root /home/emilarran/Documents/school/final-snippr/static-root;
    }
}
```

### Environment variables

By default, the app assumes that the static files are served at `localhost:9001`.

If this is not your case, e.g. you changed the nginx port to be something else,
you have to tell the app about it by setting the `STATIC_URL` environment
variable before running the server and building the static files.

```bash
export STATIC_URL=http://localhost:9000
python manage.py runserver

# and on another terminal

export STATIC_URL=http://localhost:9000
npm run build:watch
```
