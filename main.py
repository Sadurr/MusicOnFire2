import psycopg2
from flask import Flask, redirect, session, url_for, render_template, request

app = Flask(__name__)
app.secret_key = "secret"


@app.route("/", methods=["POST", "GET"])
def home():

    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():

    if request.method == "POST":
        inputForQuery = request.form["inputText"]
        inputType = request.form["inputType"]

        my_hostname = "localhost"
        my_database = "postgres"
        my_username = "postgres"
        my_password = 'zyZiek1999XD!'
        my_port = 5432

        conn = None
        cursor = None

        band = None
        album = None
        genre = None
        description = None

        try:
            conn = psycopg2.connect(
                host=my_hostname,
                dbname=my_database,
                user=my_username,
                password=my_password,
                port=my_port)

            cursor = conn.cursor() 
            # not adding to database 
            # cursor.execute("INSERT INTO albums (id, band, album, genre, description) VALUES (7, 'Jethro Tull', 'Thick as a Brick', 'Progressive Rock', 'happy')")
            
            if inputType == 'band':
                cursor.execute("SELECT band FROM albums WHERE band = '{}'" .format(inputForQuery))
                band = cursor.fetchall()
                cursor.execute( "SELECT album FROM albums WHERE band = '{}'" .format(inputForQuery))
                album = cursor.fetchall()
                cursor.execute( "SELECT genre FROM albums WHERE band = '{}'" .format(inputForQuery))
                genre = cursor.fetchall()
                cursor.execute( "SELECT description FROM albums WHERE band = '{}'" .format(inputForQuery))
                description = cursor.fetchall()
            elif inputType == 'genre':
                cursor.execute("SELECT band FROM albums WHERE genre = '{}'" .format(inputForQuery))
                band = cursor.fetchall()
                cursor.execute("SELECT album FROM albums WHERE genre = '{}'" .format(inputForQuery))
                album = cursor.fetchall()
                cursor.execute("SELECT genre FROM albums WHERE genre = '{}'" .format(inputForQuery))
                genre = cursor.fetchall()
                cursor.execute("SELECT description FROM albums WHERE genre = '{}'" .format(inputForQuery))
                description = cursor.fetchall()
            elif inputType == 'description':
                cursor.execute("SELECT band FROM albums WHERE description = '{}'" .format(inputForQuery))
                band = cursor.fetchall()
                cursor.execute("SELECT album FROM albums WHERE description = '{}'" .format(inputForQuery))
                album = cursor.fetchall()
                cursor.execute("SELECT genre FROM albums WHERE description = '{}'" .format(inputForQuery))
                genre = cursor.fetchall()
                cursor.execute("SELECT description FROM albums WHERE description = '{}'" .format(inputForQuery))
                description = cursor.fetchall()

            resultQuery = cursor.fetchall()
            # if resultQuery == []:
            #     return '<h1> There are no results. Try again! </h1>'

            # recommended - dokonczyc
            # if inputForQuery == "calm":
            #     cursor.execute(
            #     "SELECT album FROM albums WHERE description = happy AND description = slow")
            #     recommended = cursor.fetchall()
            #     print(recommended)


            # add new music - not adding new music 
            # cursor.execute("INSERT INTO albums (id, band, album, genre, description) VALUES (7, 'Jethro Tull', 'Thick as a Brick', 'Progressive Rock', 'happy')")
            # cursor.execute("INSERT INTO albums VALUES ('7', 'Jethro Tull', 'Thick as a Brick', 'Progressive Rock', 'happy';")
            # addBand = request.form['modalBandText']
            # addAlbum = request.form['modalAlbumText']
            # addGenre = request.form['modalGenreText']
            # addDescription = request.form['modalDescriptionText']
     
            # if addBand is not None and addAlbum is not None and addDescription is not None:
            #     cursor.execute("INSERT INTO albums (band, album, genre) VALUES ('{}', '{}'', '{}'".format(
            #         addBand,  addAlbum, addDescription))
                
            session['outputQuery'] = resultQuery
            conn.commit()

        except Exception as error:
            print(error)
        finally:
            if conn is not None and cursor is not None:
                conn.close()
                cursor.close()

        # return redirect(url_for("output"))
        return render_template("result.html", band=band, album=album, genre=genre, description=description)
    else:
        return render_template("login.html")


@app.route("/output")
def output():
    if "outputQuery" in session:
        outputQuery = session['outputQuery']
        return f"<h1>{outputQuery}</h1>"


@app.route("/result")
def result():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)
