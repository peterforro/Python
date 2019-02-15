from flask import Flask, render_template, request, redirect, url_for
from data_manager import *

app = Flask(__name__)



@app.route('/',methods=['GET'])
def index():
    return render_template('index.html', **request.args)



@app.route('/hash',methods=['POST'])
def hash():
    return redirect(url_for('index',
                            hash_pswd = request.form['hash_pswd'],
                            hash_hash = hash_password(request.form['hash_pswd'])))



@app.route('/verify',methods=['POST'])
def verify():
    verify_hash = request.form['verify_hash'].strip().replace('\n','')
    verify_pswd = request.form['verify_pswd']
    return redirect(url_for('index',
                            verify_hash = verify_hash,
                            verify_pswd = verify_pswd,
                            match = 'yes' if verify_password(verify_pswd, verify_hash) else 'no' ))



if __name__ == '__main__':
    app.run()
