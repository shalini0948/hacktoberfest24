from flask import Flask, render_template, request, redirect, url_for, flash, session
import markdown
import json
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Add this line with a unique secret key

def load_posts():
    posts = []
    post_files = os.listdir("blog/posts")
    for i, filename in enumerate(post_files):
        with open(f"blog/posts/{filename}", "r") as f:
            content = f.read()
            posts.append({"id": i + 1, "title": filename.replace('.md', ''), "content": markdown.markdown(content)})  # Added id attribute
    return posts

def load_comments(post_id):
    try:
        with open(f"blog/comments/{post_id}.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_comments(post_id, comments):
    with open(f"blog/comments/{post_id}.json", "w") as f:
        json.dump(comments, f)

@app.route('/')
def index():
    posts = load_posts()
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def view_post(post_id):
    posts = load_posts()
    post = next((p for p in posts if p['id'] == post_id), None)  # Find the post by id
    if post is None:
        return "Post not found", 404
    comments = load_comments(post_id)
    return render_template('post.html', post=post, comments=comments)

@app.route('/new_post', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        filename = f"blog/posts/{title.replace(' ', '_').lower()}.md"
        with open(filename, "w") as f:
            f.write(content)
        flash('Post created successfully.', 'success')
        return redirect(url_for('index'))
    return render_template('new_post.html')

@app.route('/comment/<int:post_id>', methods=['POST'])
def add_comment(post_id):
    comment = request.form['comment']
    comments = load_comments(post_id)
    comments.append(comment)
    save_comments(post_id, comments)
    flash('Comment added successfully.', 'success')
    return redirect(url_for('view_post', post_id=post_id))

if __name__ == '__main__':
    app.run(debug=True)