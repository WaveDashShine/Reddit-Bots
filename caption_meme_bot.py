import praw
import numpy as np 
from PIL import Image
import json
import requests
from io import BytesIO
import re

def main():
    global regex_image_extension
    regex_image_extension = re.compile(".*\.(jpg|png|jpeg)")

    global json_data
    with open("replied_comments.json", "r") as f:
        json_data = json.load(f)

    reddit = praw.Reddit("caption")
    subreddit = reddit.subreddit("caption_meme_bot_test")
    match_keyword = "!caption"

    for submission in subreddit.hot(limit=5):
        print_submission(submission)
        submission.comments.replace_more(limit=0)
        # the list method converts ALL comments, not just TOP-level, to a list structure
        for comment in submission.comments.list():
            if match_keyword in str(comment.body) and comment.id not in json_data["replied_comments"]:
                reply_to(comment)
                store_comment_id(comment.id)

def reply_to(comment):
    parent_comment = comment.parent()
    print(parent_comment.body)
    #comment.reply("I have replied to this comment")

def store_comment_id(id):
    json_data["replied_comments"].append(id)
    with open("replied_comments.json", "w") as f:
       json.dump(json_data, f, ensure_ascii=False)

def print_submission(submission):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("URL: ", submission.url)
    print("---------------------------------\n")

def generate_image_macro(url_image):
    if regex_image_extension.match(url_image, re.IGNORECASE):
        response = requests.get(url_image)
        img = Image.open(BytesIO(response.content))

# TODO: submit the image on the private subreddit, 
# grab the url of the submitted image,
# then link to it in the comments,
# remember to append the comment reply with some bot disclaimer 
# https://praw.readthedocs.io/en/latest/code_overview/models/subreddit.html#praw.models.Subreddit.submit_image

# TODO: use submission stream instead of scanning through submission comment
# https://praw.readthedocs.io/en/latest/code_overview/models/subreddit.html#praw.models.Subreddit.stream

if __name__ == "__main__":
    main()