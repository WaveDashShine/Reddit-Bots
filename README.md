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

Generate your client id and secret from your Reddit account here:  
https://www.reddit.com/prefs/apps/
