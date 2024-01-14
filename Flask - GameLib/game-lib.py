from flask import Flask, render_template
from models.game import Game

app = Flask(__name__)

# routes


@app.route('/hello')
def hello():
    '''
    Basic Hello World for testing route
    '''
    return '<h1>Hello World!</h1>'


@app.route('/list')
def list():
    '''
    Return a List of Games
    '''
    game_a = Game('Tetris', 'Puzzle', 'Atari')
    game_b = Game('God of War', 'Rack n Slash', 'PS')
    game_c = Game('Valorant', 'Shooter', 'PC')
    list_games = [game_a, game_b, game_c]
    return render_template('list.html', title='Games', games=list_games)


@app.route('/new')
def new():
    '''
    Add new game
    '''

    return render_template('new-game.html', title='Games')


app.run()
