from flask import Flask, render_template, request
from models.game import Game

app = Flask(__name__)

# routes


def populate_list():
    game_a = Game('Tetris', 'Puzzle', 'Atari')
    game_b = Game('God of War', 'Rack n Slash', 'PS')
    game_c = Game('Valorant', 'Shooter', 'PC')
    return [game_a, game_b, game_c]

@app.route('/hello')
def hello():
    '''
    Basic Hello World for testing route
    '''
    return '<h1>Hello World!</h1>'


@app.route('/')
def index():
    '''
    Return a List of Games
    '''
    list_games = populate_list()
    return render_template('list.html', title='Games', games=list_games)


@app.route('/new')
def new():
    '''
    Render the new game page
    '''
    return render_template('new.html', title='Games')


@app.route('/create', methods=['POST'])
def create():
    '''
    Create new game
    '''

    name = request.form['name']
    category = request.form['category']
    console = request.form['console']

    list_games = populate_list()

    game = Game(name, category, console)
    list_games.append(game)

    return render_template('list.html', title='Games', games=list_games)


app.run(debug=True)