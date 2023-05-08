from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'location': 'San Francisco, CA',
        'salary': '$200,000 - $250,000'

    },
    {
        'id': 2,
        'title': 'Senior Data Scientist',
        'location': 'San Francisco, CA',
        'salary': '$250,000 - $275,000'
    },
    {
        'id': 3,
        'title': 'Product Manager',
        'location': 'San Francisco, CA',
        'salary': '$200,000 - $250,000'
    },
    {
        'id': 4,
        'title': 'Data Engineer',
        'location': 'Remote',
       'salary': '$175,000 - $220,000'
    }
]

@app.route('/')
def hello_world():
    return render_template('home.html', 
                           jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)   