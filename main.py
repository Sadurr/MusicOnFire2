import psycopg2
from flask import Flask, redirect, session, url_for, render_template, request

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        inputType = request.form["band"]
        session["inputType"] = inputType

    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if "inputType" in session:
        inputType = session['inputType'] #not working

    if request.method == "POST":
        inputForQuery = request.form["nm"]
        
        my_hostname = "localhost"
        my_database = "postgres"
        my_username = "postgres"
        my_password = 'zyZiek1999XD!'
        my_port = 5432

        conn = None
        cursor = None

        try:
            conn = psycopg2.connect(
                host = my_hostname,
                dbname = my_database,
                user = my_username,
                password = my_password, 
                port = my_port)

            cursor = conn.cursor()
            cursor.execute("SELECT * FROM albums WHERE band = '{}'" .format( inputForQuery)) 
            
            resultQuery = cursor.fetchall()
            print( resultQuery) 
           
            session['outputQuery'] = resultQuery
            
            conn.commit()
            
        except Exception as error:
            print(error)
        finally:
            if conn is not None and cursor is not None:
                conn.close()
                cursor.close()
                
        return redirect(url_for("user")) 
    else:
       return render_template("login.html")

@app.route("/output")
def user():
    if "outputQuery" in session:
        outputQuery = session['outputQuery'] 
        return f"<h1>{outputQuery}</h1>"

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True)