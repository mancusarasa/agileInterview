# How to create the environment and start the app
 $ virtualenv -p python3 venv/
 $ pip install -r requirements.txt
 $ . ./venv/bin/activate
 $ ./api.py

# Known issues

- The search in the cache is quite inefficient (linear in the amount of cached records + the database access time).
- The initial caching of images (and the periodic renewal of the cached values) is not implemented, because I went way past two hours to implement this partial solution.
