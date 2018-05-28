from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def go_main_form():
    return render_template('layout/mainForm.html')


if __name__ == '__main__':
    app.run()


@app.route('/login')
def go_login_form():
    return render_template('layout/loginForm.html')


@app.route('/join')
def go_join_form():
    return render_template('layout/joinForm.html')


@app.route('/introduce')
def go_intro_form():
    return render_template('layout/introForm.html')


@app.route('/board')
def go_board_form():
    return render_template('layout/boardForm.html')


@app.route('/product')
def go_product_form():
    return render_template('layout/productForm.html')


