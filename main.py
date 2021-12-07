from flask import Flask, render_template, request, redirect, jsonify
from game_of_life import GameOfLife

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        GameOfLife(width=int(request.form['width']), height=int(request.form['height']))
        return redirect('/live')
    return render_template('index.html')

@app.route('/live')
def live():
    gol = GameOfLife()
    gol.form_new_generation()
    return render_template('live.html', gol=gol)

@app.route('/api', methods=['GET'])
def api():
    gol = GameOfLife()
    gol.form_new_generation()
    return jsonify({'world': gol.world, 'old_world': gol.old_world, 'counter': gol.counter})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

