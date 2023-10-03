# comment_service.py

from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/comment/<id>')
def comment(id):
    comments = {
        '1': {'user_id': '1', 'post_id': '2','comment':'Amazing post!'},
        '2': {'user_id': '2', 'post_id': '2','comment':'I Did not know that'}
    }
    comment_info = comments.get(id, {})
    
    # Get user,post info from User,post Service
    if comment_info:
        response1 = requests.get(f'http://localhost:5000/user/{comment_info["user_id"]}')
        response2 = requests.get(f'http://localhost:5001/post/{comment_info["post_id"]}')
        if response1.status_code == 200:
            comment_info['user'] = response1.json()
        if response2.status_code == 200:
            comment_info['post'] = response2.json()

    return jsonify(comment_info)

if __name__ == '__main__':
    app.run(port=5002)