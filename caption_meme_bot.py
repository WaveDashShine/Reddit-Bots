import praw
import numpy as np 
from PIL import Image
import json

def main():
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
    print("---------------------------------\n")

if __name__ == "__main__":
    main()