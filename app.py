from flask import Flask,render_template,jsonify
app=Flask(__name__)

jobs=[
  {
    'id': 1,
    'title' : 'THE GUIDE',
    'author' : 'R.K.NARAYAN',
    'publication_year': 2001,
    'publisher': 'R.K.NARAYAN',
    'language':'English'
  },
  {
    'id': 2,
    'title' : 'THE PRIVATE LIFE OF AN INDIAN PRINCE',
    'author' : 'MULK RAJ ANAND',
    'publication_year': 2001,
    'publisher': 'R.K.NARAYAN',
    'language':'English'
  },
  {
    'id': 3,
    'title' : 'GODAN',
    'author' : 'MUNSHI PREMCHAND',
    'publication_year': 2001,
    'publisher': 'R.K.NARAYAN',
    'language':'English'
  },
]

@app.route("/")
def hello():
  return render_template('home.html',books=jobs,origin='Indian')

@app.route("/books")
def list_books():
  return jsonify(jobs)
  
if __name__=="__main__" :
  app.run(host='0.0.0.0',debug=True)