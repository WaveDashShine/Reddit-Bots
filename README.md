# Reddit-Caption-Bot

Python 3.6 

pip used to install praw (required for reddit bots) 

praw.ini is required for the bot to run, template can be found here:  
https://praw.readthedocs.io/en/v4.0.0/getting_started/configuration/prawini.html

Requires the following in the PRAW.ini:  
```
client_id=
client_secret=
password=
username=
user_agent=
```

I recomment you use section declarations [...] to load directly by calling praw.Reddit([...])  

Keep in mind that your bot account will have its password stored in plaintext. 

Generate your client id and secret from your Reddit account here:  
https://www.reddit.com/prefs/apps/

JSON file will be used to store comments that have already been replied to. The above command is useful for untracking JSON changes while still keeping a copy of its template in the repo.   
`git update-index --assume-unchanged FILE_NAME`  