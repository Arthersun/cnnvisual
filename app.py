#encoding:utf-8
from flask import Flask,render_template,request
from section import mlrun
app = Flask(__name__)
###导入模块结束###

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mnist',methods=['POST'])
def run():
    BATCH_SIZE=request.form.get('BATCH_SIZE',type=int)
    SEED=request.form.get('SEED',type=int)
    learning_rate=request.form.get('learning_rate',type=float)
    a=mlrun(BATCH_SIZE,SEED,learning_rate)
    context1={
        'batch_size':BATCH_SIZE,
        'seed':SEED,
        'learning_rate':learning_rate,
        'l1':a[0],
        'l2': a[200],
        'l3': a[400],
        'l4': a[600],
        'l5': a[800],
        'l6':a[1000]
    }
    return render_template('index.html',**context1)

if __name__ =='__main__':
	app.run(debug=True)