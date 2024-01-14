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


@app.route('/init')
def init():
    '''
    '''
    list_games = ['Tetris', 'God of War', 'Valorant']
    return render_template('list.html', title='Games', games=list_games)


app.run()
