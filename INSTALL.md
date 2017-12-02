INSTALLATION INSTRUCTIONS FOR CROMLECH DEMO APP
==========================

For python3.4+
--------------

```bash
$> pyvenv . && source bin/activate
$> python bootstrap.py
$> ./bin/buildout
$> pip install uwsgi
$> uwsgi --http :8080 --wsgi-file app.py
