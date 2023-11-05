

"""
given query, reddit post and comments, return input to buddy
"""
def formatter(posts, query):
    return_str = f"query: {query}\n\n"
    for post in range(len(posts)):
        return_str += f"post#{post}: {posts[post][0].title}"
        for comment in posts[post][1]:
            return_str += f"(@{comment.author}): {comment.body}\n"
    return return_str