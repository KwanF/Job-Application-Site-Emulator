from flask import Flask, render_template, jsonify
from database import load_jobs_from_db
from sqlalchemy import text

app = Flask(__name__)

# JOBS = [
#     {
#         'id': 1,
#         'title': 'Software Engineer',
#         'location': 'San Francisco, CA',
#         'salary': '$200,000 - $250,000'

#     },
#     {
#         'id': 2,
#         'title': 'Senior Data Scientist',
#         'location': 'San Francisco, CA',
#         'salary': '$250,000 - $275,000'
#     },
#     {
#         'id': 3,
#         'title': 'Product Manager',
#         'location': 'San Francisco, CA',
#         'salary': '$200,000 - $250,000'
#     },
#     {
#         'id': 4,
#         'title': 'Data Engineer',
#         'location': 'Remote',
#        'salary': '$175,000 - $220,000'
#     }
# ]


@app.route('/')
def hello_world():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)   