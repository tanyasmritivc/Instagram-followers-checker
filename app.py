from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_unfollowers():
    followers_file = request.files['followers']
    following_file = request.files['following']

    try:
        followers = json.load(followers_file)
        following_data = json.load(following_file)
        following = following_data['relationships_following']

        followers_list = [entry['string_list_data'][0]['value'] for entry in followers]
        following_list = [entry['string_list_data'][0]['value'] for entry in following]

        not_following_back = [user for user in following_list if user not in followers_list]

        return jsonify(not_following_back=not_following_back)

    except Exception as e:
        return jsonify(error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
