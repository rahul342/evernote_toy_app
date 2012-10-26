<h2>evernote_toy_app</h2>

<strong>About</strong>: 
A simple app that enables browsing of images in your Evernote account (currently sandbox accounts only).
Essentially converts your evernote account to a flickr-like utility (doesn't include uploading new images for now)

<h2>Demo</h2>

Try the demo at http://evernotoy.appspot.com (Currently works with sandbox.evernote only)

<h2>Code Structure</h2>

<ul>
<li><a href="https://github.com/django-nonrel/djangoappengine">djangoappengine</a>
    <ul>
        <li>autoload</li>
        <li>dbindexer</li>
        <li>django (a slightly tailored version of the <a href="https://www.djangoproject.com/">original</a>)</li>
        <li>djangoappengine</li>
        <li>djangotoolbox</li>
    </ul>
</li>
<li><a href="https://github.com/evernote/evernote-sdk-python">Evernote Python SDK</a>
    <ul>
        <li>evernote</li>
        <li>thrift</li>
    <ul>
</li>
<li><a href="https://github.com/omab/django-social-auth">django-social-auth</a>
    <ul>
        <li>httplib2</li>
        <li>oauth2</li>
        <li>openid</li>
        <li>social_auth</li>
    <ul>
</li>
<li>evernotoy (Code for the app)</li>
</ul>


The app is structured like any other django app. I have added a wrapper over the api in <a href="https://github.com/rahul342/evernote_toy_app/blob/master/evernotoy/evernote_api.py">evernote_api.py</a> (Trimmed and appended <a href="https://github.com/akhaku/evernote-django">evernote-django</a> to suit the purpose. Thanks <a href="https://github.com/akhaku">akhaku</a>!)

<h3> Some other libraries/frameworks/sources </h3>
Also using the awesome 
<ul>
<li><a href="http://twitter.github.com/bootstrap/">Twitter Bootstrap</a></li>
<li><a href="http://www.jacklmoore.com/colorbox">ColorBox</a></li>
<li>Background image from http://subtlepatterns.com/</li>
</ul>



<h2>Usage</h2>

To deploy your own version, download the code. Add a new ```evernote_key_settings.py``` file in the root directory. Add your Evernote dev keys as -
```python
EVERNOTE_CONSUMER_KEY = ''
EVERNOTE_CONSUMER_SECRET = ''
```
For deploying on Google App Engine, you'll need to change ```app.yaml``` of course.
    