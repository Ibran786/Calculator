from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def a():
    return render_template("calculator.html")
@app.route('/calculator',methods=['POST'])
def b():
    if request.method=="POST":
        x=float(request.form['f'])
        y=float(request.form['s'])
        z=request.form['o']
        if z=="+":
            result=x+y
        elif z=="-":
            result=x-y
        elif z=="*":
            result=x*y
        elif z=="/":
            result=x/y
        else:
            result="Incorrect Operator"
    return render_template("calculator.html",result=result)

if __name__=="__main__":
    app.run()



