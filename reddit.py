import praw
import os
from dotenv import load_dotenv
load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv('id'),
    client_secret=os.getenv('secret_id'),
    user_agent="ub hacking"
)

#for submission in reddit.subreddit("test").hot(limit=10):
#    print(submission.title)
def sorter(comment):
    if not comment or not (hasattr(comment, "score") and comment.score == None):
        return 100
    return comment.score

def parse(urls, top_n):
    """
    given a list of urls, returns top n comments from each post alongside comments
    """
    ret_string = ""
    ret_post = []
    for url in urls:
        submission = reddit.submission(url=url)
        comments = submission.comments
        title = submission.title
        comments = sorted(comments, key=sorter, reverse=True)
        total = len(comments)
        if  total > top_n:
            comments = comments[0:top_n]
        ret_post.append((submission, comments))
        # for comment in comments:
        #     if comment.author is None:
        #         print(comments)
        #     else:
        #         ret_string += comment.author.name + " : " + comment.body + "\n\n"
        #         ret_comments.append(comment)
    return ret_post