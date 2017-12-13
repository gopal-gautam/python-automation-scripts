# python-automation-scripts

## Upload File using pycurl 
### \[Anonymous HTTP POST\]
```py
c = pycurl.Curl()
c.setopt(c.POST, 1)
c.setopt(c.URL, "http://upload_url/")
c.setopt(c.HTTPPOST, [("file_field_name", (c.FORM_FILE, "c:\\path_to_file"))])
#c.setopt(c.VERBOSE, 1)
c.perform()
c.close()
```

### \[ftp upload\]
```py
from os.path import getsize

c = pycurl.Curl()
c.setopt(pycurl.URL, 'ftp://fpt_url:21/myfile')
c.setopt(pycurl.USERPWD, 'username:password')
c.setopt(pycurl.VERBOSE, 1)
f = open('my_file')
c.setopt(pycurl.INFILE, f)
c.setopt(pycurl.INFILESIZE, getsize('my_file'))
c.setopt(pycurl.UPLOAD, 1)
c.perform()
```
