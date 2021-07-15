from flask import Flask,render_template,request,jsonify,redirect,url_for
import webbrowser
from threading import Timer
from script import *

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def interface():
    if request.method == "POST":

        data = {}
              
        accounts = request.form["accounts"]
        subject = request.form["subject"]
        task = request.form["tasks"]
        threads = request.form["threads"]
        browsers = request.form["Radio"]   
        link = request.form["link"]
        if request.form.get("box", False):
            hide = request.form["box"]
        elif request.form.get("box", True):
            hide = 'dont_hide_browser'
        try :
            reply = request.form["reply_msg"]
        except :
            reply = "NAN"
        domain = request.form['domain']
        
        data['subject'] = subject
        data['task'] = task
        data['threads'] = threads
        data['browsers'] = browsers
        data['link'] = link
        data['accounts'] = accounts
        data['hide'] = hide
        data['reply'] = reply
        data['domain'] = domain

        return launch(data)
    else:
        try:
            acc = request.args['acc']
        except:
            acc = ''
        try:
            subject = request.args['subject']
        except:
            subject = ''
        try:
            link = request.args['link']
        except:
            link = ''
        try:
            n = request.args['n']
        except:
            n = ''
        try:
            domain = request.args['domain']
        except:
            domain = ''

        return render_template("interface.html",acc=acc,subject=subject,n=n,link=link,domain=domain)


@app.route('/resume', methods=["GET"])
def resume_script():
    return resume()

@app.route('/stop', methods=["GET"])
def stop_script():
    return stop()

@app.route('/pause', methods=["GET"])
def pause_script():
    return pause()

if __name__ == '__main__': 
    webbrowser.open_new('http://127.0.0.1:5500/')
    app.run('127.0.0.1', 5500,debug=False) 
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    