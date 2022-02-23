import psycopg2
from flask import Flask, redirect, session, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
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
            resultQuery = cursor.execute("SELECT * FROM albums WHERE band = '{0}'" .format(inputForQuery)) 
         
            print(cursor.fetchall()) 
            conn.commit()

            
        except Exception as error:
            print(error)
        finally:
            if conn is not None and cursor is not None:
                conn.close()
                cursor.close()
                
        session['outputQuery'] = resultQuery
        return redirect(url_for("user", output=inputForQuery)) #"user"-> nazwa funkcji
    else:
       return render_template("login.html")

@app.route("/<output>")
def user(output):
    outputQuery = session.get('outputQuery') #none
    return f"<h1>{outputQuery}</h1>"

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True)