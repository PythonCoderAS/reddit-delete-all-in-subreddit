import praw
import praw.models
import argparse

reddit = praw.Reddit("bot", user_agent="Delete All in Subreddit v1 by PythonCoderAS")

parser = argparse.ArgumentParser(description="Delete all in a subreddit")
parser.add_argument("subreddit", help="The subreddit to delete all in.")
parser.add_argument("type", choices=["posts", "comments", "all"], help="The type of content to delete.")

def main(args=None):
    args = parser.parse_args(args)
    user: praw.models.Redditor = reddit.user.me()
    sub: praw.models.Subreddit - reddit.subreddit(args.subreddit)
    if args.type in ("posts", "all"):
        for post in user.submissions.new(limit=10000):
            if post.subreddit == args.subreddit:
                post.delete()
    if args.type in ("comments", "all"):
        for comment in user.comments.new(limit=10000):
            if comment.subreddit == args.subreddit:
                comment.delete()

if __name__ == "__main__":
    main()
