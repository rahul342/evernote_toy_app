# Create your views here.
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, \
    HttpResponseForbidden
from django.shortcuts import render_to_response
from django.template import Context
from django.template.loader import get_template
from evernote_api import EvernoteAPI
import logging
from django.utils import simplejson

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/');
    else:
        return render_to_response('login.html', {},)

@login_required
def home(request):
    extra_data = request.user.social_auth.all()[0].extra_data
    evernote_api = EvernoteAPI(extra_data['oauth_token'], extra_data['store_url'])
    shard_url = '/'.join(extra_data['store_url'].split('/')[:-1])
    
    INIT_LOAD_SIZE = 18
    note_offset, resource_offset, image_guids = evernote_api.get_image_resource_guids(0, 0, INIT_LOAD_SIZE)
    
    no_more_images = False
    if len(image_guids) != INIT_LOAD_SIZE:
        no_more_images = True
        
    return render_to_response('home.html', dict(note_offset=note_offset, resource_offset=resource_offset,
                                                image_guids=image_guids, shard_url=shard_url,
                                                token=extra_data['oauth_token'], no_more_images=no_more_images))

def load_more(request, note_offset, resource_offset):
    if not request.user.is_authenticated():
        return HttpResponseForbidden('')
    
    note_offset, resource_offset = map(int, [note_offset, resource_offset])
    extra_data = request.user.social_auth.all()[0].extra_data
    evernote_api = EvernoteAPI(extra_data['oauth_token'], extra_data['store_url'])
    shard_url = '/'.join(extra_data['store_url'].split('/')[:-1])
    
    LOAD_SIZE = 12
    note_offset, resource_offset, image_guids = evernote_api.get_image_resource_guids(note_offset, resource_offset, LOAD_SIZE)
    if len(image_guids) == 0:
        return HttpResponse('', content_type="text/plain")
    
    no_more_images = False
    if len(image_guids) < LOAD_SIZE:
        no_more_images = True
    
    rows = get_template('rows.html').render(Context(dict(token=extra_data['oauth_token'], shard_url=shard_url, image_guids=image_guids)))
    json = simplejson.dumps(dict(note_offset=note_offset, resource_offset=resource_offset, rows=rows, no_more_images=no_more_images))
    return HttpResponse(json, mimetype='application/json')
        
        
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/login')