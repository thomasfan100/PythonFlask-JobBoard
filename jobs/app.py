from flask import Flask , render_template, g
import sqlite3

PATH = 'db/jobs.sqlite'

app = Flask(__name__)

def open_connection():
    connection = getattr(g,'_connection',None)
    if connection == None:
        connection = g._connection = sqlite3.connect(PATH)
    connection.row_factor = sqlite3.Row
    return connection

def execute_sql(sql,values=(), commit=False,singleFalse):
    connection = open_connection()
    cursor = connection.execute(sql,values)
    if commit==True:
        results = connection.commit()
    else:
        results = cursor.fetchone() if single lese cursor.fetchall()
    curso.close()
    return results

@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g,'_connection',None)
    if connection is not None:
        connection.close()
        
@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
