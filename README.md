evernote_toy_app
================

A simple app that enables browsing of images in your Evernote account (currently sandbox only).
Essentially converts your evernote account to flickr (doesn't include uploading new images for now)

<h2>Demo</h2>

Try the demo at http://evernotoy.appspot.com (Currently only works with sandbox.evernote)

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


The app is structured like any other django app. I have added a wrapper over the api in evernotoy/evernote_api.py (Trimmed and appended https://github.com/akhaku/evernote-django to suit the purpose. Thanks https://github.com/akhaku!)

<h3> Some other libraries/frameworks/sources </h3>
Also using the awesome 
<ul>
<li>http://twitter.github.com/bootstrap/</li>
<li>https://github.com/jackmoore/colorbox</li>
<li>Background image from http://subtlepatterns.com/</li>



<h2>
    