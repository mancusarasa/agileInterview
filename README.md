# How to create the environment and start the app

```
mkdir venv
virtualenv -p python3 venv/
. ./venv/bin/activate
pip install -r requirements.txt
./api.py
```
# Known issues

- The search in the cache is quite inefficient (linear in the amount of cached records + the database access time).
- The initial caching of images (and the periodic renewal of the cached values) is not implemented, because I went way past two hours to implement this partial solution.
