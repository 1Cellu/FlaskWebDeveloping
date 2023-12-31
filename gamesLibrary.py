from flask import Flask, render_template, request, redirect, session, flash, url_for

class Game:
    def __init__(self, name, category, console):
        self.name = name
        self.category=category
        self.console=console

games_list2000 = Game('Tetris', 'Puzzle', 'Atari')
games_list2023 = Game('f123', 'Racing', 'PS4')
games_list20001 = Game('Tetris', 'Puzzle', 'Atari')
games_list20231 = Game('f123', 'Racing', 'PS4')
games_list20002 = Game('Tetris', 'Puzzle', 'Atari')
games_list20232 = Game('f123', 'Racing', 'PS4')
games_list20003 = Game('Tetris', 'Puzzle', 'Atari')
games_list20233 = Game('f123', 'Racing', 'PS4')
games_list20004 = Game('Tetris', 'Puzzle', 'Atari')
games_list20234 = Game('f123', 'Racing', 'PS4')
games_list20005 = Game('Tetris', 'Puzzle', 'Atari')
games_list20235 = Game('f123', 'Racing', 'PS4')
games_list20006 = Game('Tetris', 'Puzzle', 'Atari')
games_list20236 = Game('f123', 'Racing', 'PS4')
games_list20007 = Game('Tetris', 'Puzzle', 'Atari')
games_list20237 = Game('f123', 'Racing', 'PS4')
games_list = [games_list2000, games_list2023, games_list20001, games_list20231, games_list20002, games_list20232, games_list20003, games_list20233, games_list20004, games_list20234,
              games_list20005, games_list20235, games_list20006, games_list20236, games_list20007, games_list20237, games_list2000, games_list2023, games_list2000, games_list2023]

class User:
    def __init__(self, name, nickname, password):
        self.name = name
        self.nickname = nickname
        self.password = password

user1 = User("Daniel", "dan", "admin")
user2 = User("Lys", "Gio", "tester")
user3 = User("Mari", "Mar", "123")
user4 = User("Daniel1", "dan", "admin")
user5 = User("Lys1", "Gio", "tester")
user6 = User("Mari1", "Mar", "123")
user7 = User("Daniel2", "dan", "admin")
user8 = User("Lys2", "Gio", "tester")
user9 = User("Mari2", "Mar", "123")
user10 = User("Daniel3", "dan", "admin")
user11 = User("Lys3", "Gio", "tester")
user12 = User("Mari3", "Mar", "123")
user13 = User("Danie4l", "dan", "admin")
user14 = User("Lys4", "Gio", "tester")
user15 = User("Mari4", "Mar", "123")
user16 = User("Daniel5", "dan", "admin")
user17 = User("Lys5", "Gio", "tester")
user18 = User("Mari5", "Mar", "123")

users = { user1.nickname : user1,
          user2.nickname : user2,
          user3.nickname : user3,
          user4.nickname: user4,
          user5.nickname: user5,
          user6.nickname: user6,
          user7.nickname: user7,
          user8.nickname: user8,
          user9.nickname: user9,
          user10.nickname: user10,
          user11.nickname: user11,
          user12.nickname: user12,
          user13.nickname: user13,
          user14.nickname: user14,
          user15.nickname: user15,
          user16.nickname: user16,
          user17.nickname: user17,
          user18.nickname: user18
          }

app = Flask(__name__)
app.secret_key = 'DanielC'

@app.route('/')
def index():
    return render_template('list.html', title='Dinamic Name', games_list = games_list)

@app.route('/newGame')
def newGame():
    if 'user_on' not in session or session['user_on'] == None:
        return redirect(url_for('login', next=url_for('newGame')))
    return render_template('new_game.html', title='New Game')

@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']

    game = Game(name, category, console)
    games_list.append(game)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    next = request.args.get('next')
    if(next == None):
        next = url_for('index')
    return render_template('login.html', next = next)

@app.route('/autenticate', methods=['POST'])
def autenticate():
    if request.form['user'] in users:
        user = users[request.form['user']]
        if request.form['password'] == user.password:
            session['user_on'] = user.nickname
            flash(user.nickname + ' entered')
            nextPage = request.form['next']
            return redirect(nextPage)
        else:
            flash('Wrong User or Password')
            return redirect(url_for('login'))
    else:
        flash('Wrong User or Password')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['user_on'] = None
    flash('Logout')
    return redirect('/')

app.run(debug=True)