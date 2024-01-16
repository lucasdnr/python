from flask import Flask, render_template, request, redirect, session, flash
from models.game import Game

app = Flask(__name__)
app.secret_key = "lucasdnr"

def populate_list():
    game_a = Game('Tetris', 'Puzzle', 'Atari')
    game_b = Game('God of War', 'Rack n Slash', 'PS')
    game_c = Game('Valorant', 'Shooter', 'PC')
    return [game_a, game_b, game_c]


list_games = populate_list()
# routes


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
    return render_template('list.html', title='Games', games=list_games)


@app.route('/new')
def new():
    '''
    Render the new game page
    '''
    return render_template('new.html', title='Games')


@app.route('/signin')
def signin():
    '''
    Render the login/sign in page
    '''
    return render_template('login.html')


@app.route('/create', methods=['POST'])
def create():
    '''
    Create new game
    '''

    name = request.form['name']
    category = request.form['category']
    console = request.form['console']
    game = Game(name, category, console)
    list_games.append(game)

    return redirect('/')


@app.route('/auth', methods=['POST'])
def auth():
    '''
    Authentication route
    '''
    if 'alohomora' == request.form['password']:
        session['user_logged'] = request.form['user']
        flash(f'{session['user_logged']} Login successful', 'success')
        return redirect('/')
    else:
        flash('User or password is incorrect!', 'danger')
        return redirect('/signin')


app.run(debug=True)
