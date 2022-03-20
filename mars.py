from flask import Flask, url_for, render_template, request

app = Flask(__name__)


@app.route('/answer', methods=['POST', 'GET'])
@app.route('/auto_answer', methods=['POST', 'GET'])
def answer():
    profs = {'opt1': 'инженер-исследователь',
             'opt2': 'инженер',
             'opt3': 'исследователь'}
    if request.method == 'GET':
        return render_template('form.html', profs=profs)
    elif request.method == 'POST':
        params = dict(request.form)
        return render_template('answer.html', params=params, profs=
        ','.join([profs[i] for i in profs if params.get(i)]))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
