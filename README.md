This repo should illustrate a problem with pylint wrongly recognizing global module when a file of that name exists in a different folder.

Try to run:

```
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pylint .
```

Pylint returns an error:

`util2/main.py:1:0: E0611: No name 'namedtuple' in module 'collections' (no-name-in-module)`
