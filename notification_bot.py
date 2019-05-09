import praw

reddit = praw.Reddit('notification')

# TODO: create a separate bot account for testing this bot
subreddit = reddit.subreddit("caption_meme_bot_test")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")

    submission.comments.replace_more(limit=0)
    # the list method converts ALL comments, not just TOP-level, to a list structure
    for comment in submission.comments.list():
        print(comment.body)
    
    # you can access a reply from comment.replies and iterating through it
