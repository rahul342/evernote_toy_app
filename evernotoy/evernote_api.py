from django.conf import settings
from evernote.edam.notestore import NoteStore
from evernote.edam.notestore.ttypes import NoteFilter
from thrift.transport import THttpClient
import thrift.protocol.TBinaryProtocol as TBinaryProtocol

class EvernoteAPI:
    if getattr(settings, 'EVERNOTE_DEBUG', True):
        evernoteHost = 'sandbox.evernote.com'
    else:
        evernoteHost = 'www.evernote.com'
    tempCredentialRequestUri = "https://" + evernoteHost + "/oauth"
    resOwnerAuthUri = "https://" + evernoteHost + "/OAuth.action"
    resFormat = "microclip"
    tokRequestUri = tempCredentialRequestUri
    consumerKey = settings.EVERNOTE_CONSUMER_KEY
    consumerSecret = settings.EVERNOTE_CONSUMER_SECRET
    userStoreUri = "https://" + evernoteHost + "/edam/user"

    def __init__(self, oauth_token=None, shard=None, uid=None, exp=None):
        self.oauth_token = oauth_token
        self.shard = shard
        self.uid = uid
        self.exp = exp
        self.notestore = None

    def _get_note_store(self):
        if self.notestore == None:
            noteStoreHttpClient = THttpClient.THttpClient(self.shard)
            noteStoreProtocol = TBinaryProtocol.TBinaryProtocol(noteStoreHttpClient)
            self.noteStore = NoteStore.Client(noteStoreProtocol)
        return self.noteStore

    def get_notes_with_tag(self, tag):
        """ Gets all the notes with the tag "tag"
        """
        notestore = self._get_note_store()
        allTags = notestore.listTags(self.oauth_token)
        tag = [x for x in allTags if x.name == tag][0]
        nFilter = NoteFilter(tagGuids=[tag.guid])
        notes = notestore.findNotes(self.oauth_token, nFilter, 0, 10)
        return notes.notes

    def get_image_resource_guids(self, note_offset=0, resource_offset=0, max_images=10):
        """Gets images (total = max_images) starting from resource_offset in note_offset. Each image is above 256x256.
           Returns a tuple (note_offset, resource_offset, image_guid list). (note_offset, resourcse_offset) points to the next unprocessed resource
        """
        if max_images == 0:
            return note_offset, resource_offset, []
        notestore = self._get_note_store()
        note_filter = NoteFilter(words="resource:image/*")
        image_guids = []
        
        note = notes = None
        break_flag = False
        while not(notes and note_offset >= notes.totalNotes):
            notes = notestore.findNotes(self.oauth_token, note_filter, note_offset, max_images)
            for note in notes.notes:
                while resource_offset < len(note.resources):
                    cur_resource = note.resources[resource_offset]
                    if (cur_resource.mime.startswith('image') and 
                        cur_resource.width >= 256 and
                        cur_resource.height >= 256):
                        image_guids.append(cur_resource.guid)
                        if len(image_guids) == max_images:
                            break_flag = True
                            break
                    resource_offset = resource_offset + 1
                if break_flag:
                    break
                note_offset = note_offset + 1
                resource_offset = 0
            if break_flag:
                    break
            
        if break_flag and note:
            if (resource_offset + 1) < len(note.resources):
                resource_offset = resource_offset + 1
            else:
                note_offset = note_offset + 1
                resource_offset = 0
            
        return note_offset, resource_offset, image_guids
        
        