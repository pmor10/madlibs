"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Start Here</title>
      </head>
      <body>
        <a href="/hello">Take me to the start</a>
      </body>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment.""" 

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game', methods=["GET"])
def show_madlib_form():
    """Get the user respond"""

    play_game = request.args.get("play")

    if play_game == "yes":
        return render_template("game.html")
    return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():

    person = request.args.get("person")
    player_color = request.args.get("color")
    player_noun = request.args.get("noun")
    player_adj = request.args.get("adjective")

    return render_template("madlib.html", 
                            person=person, 
                            color=player_color,
                            noun=player_noun,
                            adjective=player_adj)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
