from flask import Flask, render_template, request, redirect, session, flash, url_for
from models.game import Game
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "lucasdnr"

app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{driver}://{user}:{password}@{server}/{database}'.format(
        driver='mysql+mysqlconnector',
        user='root',
        password='',
        server='localhost',
        database='gamelib'
)


db = SQLAlchemy(app)


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
    # we can create a middleware to implement this validation
    if 'user_logged' not in session or session['user_logged'] == None:
        return redirect(url_for('signin', page=url_for('index')))

    return render_template('list.html', title='Games', games=list_games)


@app.route('/new')
def new():
    '''
    Render the new game page
    '''
    # we can create a middleware to implement this validation
    if 'user_logged' not in session or session['user_logged'] == None:
        return redirect(url_for('signin', page=url_for('new')))

    return render_template('new.html', title='Games')


@app.route('/signin')
def signin():
    '''
    Render the login/sign in page
    '''
    next_page = request.args.get('page')
    return render_template('login.html', page=next_page)


@app.route('/signout')
def signout():
    '''
    Signout of user
    '''
    session['user_logged'] = None
    flash('Bye bye!', 'success')
    return redirect(url_for('signin'))


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

    return redirect(url_for('index'))


@app.route('/auth', methods=['POST'])
def auth():
    '''
    Authentication route
    '''
    # This authentication is only symbolic for our example to have a login screen
    if '123456' == request.form['password']:
        session['user_logged'] = request.form['user']
        next_page = request.form['page']
        flash(f'{session['user_logged']} Login successful', 'success')
        if next_page == 'None':
            return redirect(url_for('index'))
        else:
            return redirect(next_page)
    else:
        flash('User or password is incorrect!', 'danger')
        return redirect(url_for('signin'))


if __name__ == '__main__':
    app.run(debug=True)
