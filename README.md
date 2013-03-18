blog
====

My little web2py blog engine, modeled after my experience with wordpress...

Config
====
All your sensitive config shit must be defined in models/config.py
Since files are loaded in alphabetical order in the models dir this is loaded
before db.py and anything after that...

Here is a sample config:

# ---CUT-----------------------------------------------
# config = dictdot(
# 	 backend    = 'sqlite'
# 	,dalstring  = '%s://storage.db'
# 	,mailserver = 'smtp.3rr0rsp4c3.com:25'
# 	,mailsender = 'mailer-daemon@3rr0rsp4c3.com'
# 	,maillogin  = 'mailer-daemon:annih.ilate'
# )
# # Laaaaaaazyy
# config.dalstring = config.dalstring % config.backend
# -----------------------------------------------CUT---

Just a note... dictdot is a dictionary in which you can access attributes that
are valid python identifiers as properties... so exactly like javascript. I did
this because I was working with some really gnarly dict's in the shotgun libray
and i was fucking tired of typing the [''] like 3 or four times >:| so yeah.
