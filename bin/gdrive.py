#! /usr/bin/python
# Written by Peter Nichols to copy files to Google Drive. http://www.itdiscovery.info
# Sample file from http://planzero.org/blog/2012/04/13/uploading_any_file_to_google_docs_with_python
# Desired feature to grab all the kml/jpg files on the directory and dump them at once
# License: GPL 2.0

import sys, time, os.path, argparse
import atom.data, gdata.client, gdata.docs.client, gdata.docs.data


parser = argparse.ArgumentParser(description='Python script that KML files and uploads them to Google Drive.')
parser.add_argument('-u','--username', help='-u --username. Google Drive Username to Login as. Required!',required=True)
parser.add_argument('-p','--password', help='-p --password. Google Drive Password to Login as. Required!',required=True)
parser.add_argument('-l','--location', default='images', help='-l --location. [My Tracks] Google Drive Directory to store the KML files.',required=False)
parser.add_argument('-f','--filename', help='-f --filename The file name/directory for the KML file.',required=True)
parser.add_argument('-s', '--single', default=0, type=int, help= '-s --single [1] A single file [0] or all files [1] of that type in the directory', required=False)
parser.add_argument('-m','--mimetype', default='jpg', choices=['kml','jpg','txt','csv','mpg','mp4'],help='-m --mimetype [jpg] The file type of the files: kml, jpg, txt, csv, mpg, mp4',required=False )
args = parser.parse_args()

username = args.username
password = args.password
collection = args.location
targetdir = args.filename 
single = args.single
ftype = args.mimetype

if ftype == 'jpg':
    file_type = 'image/jpeg'
elif ftype == 'kml':
    file_type = 'application/vnd.google-earth.kml+xml'
elif ftype == 'txt':
    file_type = 'text/plain'
elif ftype == 'csv':
    file_type = 'text/csv'
elif ftype == 'mpg':
    file_type = 'audio/mpeg'
elif ftype == 'mp4':
    file_type = 'video/mp4'


#Start the Google Drive Login
docsclient = gdata.docs.client.DocsClient(source='RPi Python-GData 2.0.17')

# Get a list of all available resources (GetAllResources() requires >= gdata-2.0.15)
print 'Logging in...',
try:
    docsclient.ClientLogin(username, password, docsclient.source);
except (gdata.client.BadAuthentication, gdata.client.Error), e:
    sys.exit('Unknown Error: ' + str(e))
except:
    sys.exit('Login Error, perhaps incorrect username/password')
print 'success!'

# The default root collection URI
uri = 'https://docs.google.com/feeds/upload/create-session/default/private/full'
# Get a list of all available resources (GetAllResources() requires >= gdata-2.0.15)
print 'Fetching Collection/Directory ID...',
try:
   resources = docsclient.GetAllResources(uri='https://docs.google.com/feeds/default/private/full/-/folder?title=' + collection + '&title-exact=true')
except:
   sys.exit('ERROR: Unable to retrieve resources')
# If no matching resources were found
if not resources:
   sys.exit('Error: The collection "' + collection + '" was not found.')
# Set the collection URI
uri = resources[0].get_resumable_create_media_link().href
print 'success!'
# Make sure Google doesn't try to do any conversion on the upload (e.g. convert images to documents)
uri += '?convert=false'

if single==1:
   #Loop through directory name in arguments for all the file types
   for filer in os.listdir(targetdir):
    if filer.endswith(ftype):
         print 'Uploading ', filer,'.....',
         fhandle = open(filer)
         file_size = os.path.getsize(fhandle.name)
         # Create an uploader and upload the file
         uploader = gdata.client.ResumableUploader(docsclient, fhandle, file_type, file_size, chunk_size=1048576, desired_class=gdata.data.GDEntry)
         new_entry = uploader.UploadFile(uri, entry=gdata.data.GDEntry(title=atom.data.Title(text=os.path.basename(fhandle.name))))
         print 'success!'
         continue
    else:
         print 'Skipping',filer,'.'
         continue
else:
    fhandle = open(targetdir)
    file_size = os.path.getsize(fhandle.name)
    print 'Uploading ', targetdir,'....' 
    # Create an uploader and upload the file
    uploader = gdata.client.ResumableUploader(docsclient, fhandle, file_type, file_size, chunk_size=1048576, desired_class=gdata.data.GDEntry)
    new_entry = uploader.UploadFile(uri, entry=gdata.data.GDEntry(title=atom.data.Title(text=os.path.basename(fhandle.name))))
    print 'success!',
print 'Done!'