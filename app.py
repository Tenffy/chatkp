from flask import Flask, render_template, request
from markupsafe import escape
from flask import render_template
from gpt35turbo import GPT35Chat
from flask_socketio import SocketIO, emit     
import time
import asyncio

app= Flask(__name__)
app.config["JSON_AS_ASCII"]= False
'''
app.config['SECRET_KEY'] = 'secret!'  
socketio = SocketIO() 

socketio.init_app(app, cors_allowed_origins='*')
 
name_space = '/dcenter'
 

thread = None  
def background_thread():                                                        
    while True:                                                                 
        socketio.emit('message', {'goodbye': "Goodbye"})                        
        time.sleep(1)

@socketio.on('connect')
def connect():                                                                  
    global thread                                                               
    if thread is None:                                                          
        thread = socketio.start_background_task(target=background_thread)
    
@app.route('/test') 
def index():                                                                    
    return render_template('hello.html')  
'''    
'''
@app.route('/push')
def push_once():
    event_name = 'dcenter'
    broadcasted_data = {'data': "test message!"}
    socketio.emit(event_name, broadcasted_data, broadcast=False, namespace=name_space)
    return 'done!'

@socketio.on('connect', namespace=name_space)
def connected_msg():
    print('client connected.')

@socketio.on('disconnect', namespace=name_space)
def disconnect_msg():
    print('client disconnected.')

@socketio.on('my_event', namespace=name_space)
def mtest_message(message):
    print(message)
    emit('my_response',
         {'data': message['data'], 'count': 1})
 
@app.route("/")
def hello_world():
    return "<p>Hello,欢迎光临GPT测试网页!,请在浏览器地址中输入/GPT/你想对gpt说的话</p>"
'''
'''

# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"#escape转义

# @app.route("/user/<username>")
# def show_user_profile(username):
#     return f'User {escape(username)}'

# @app.route("/post/<int:post_id>")
# def show_post(post_id):
#     return f'Post {post_id}'

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html',name=name)
# # app.run(host='0.0.0.0',debug=True)
'''
allMsg=''
chatCount=0
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/get_response',methods=['POST'])
def processIndex():
    global allMsg
    user_input = request.form['user_input']
    allMsg+=user_input
    print("输入："+user_input)
    output=generateGPT(allMsg) 
    allMsg+=output
    return "GPT：<br>"+output

@app.route('/back',methods=['POST'])
def backhome():
    return render_template('index.html')
# @app.route('/GPT/')
# @app.route('/GPT/<strname>')
# def generateGPT(strname):
#     gptOuput=GPT35Chat()
#     output=gptOuput.generator(escape(strname))
#     return render_template('GPT.html',strname=output)

@app.route('/chat')
def chatindex():
    return render_template('chat.html')
@app.route('/chat/get_response', methods=['POST'])
def process():
    if request.method == "POST":
        global allMsg
        input_msg = request.form['user_input']
        allMsg =allMsg+'\n\n'+input_msg
        global chatCount
        if chatCount==0:
            allMsg=""
        chatCount+=1
        if chatCount==1:
            output=generateF(input_msg)
            msgFilter = "第%s轮:"%chatCount+output
            is_finish=False
            response=[msgFilter,is_finish]
            return response
        elif chatCount<5:
            output=generateM(allMsg)
            msgFilter = "第%s轮:"%chatCount+output
            is_finish=False
            response=[msgFilter,is_finish]
            return response
        else :
            output=generateD(allMsg)
            msgFilter = "第%s轮:"%chatCount+output
            is_finish=True
            chatCount=0
            response=[msgFilter,is_finish]
            return response
@app.route('/reset')
def reset():
    global chatCount
    chatCount =0
    global msgFilter
    global allMsg
    msgFilter = []
    allMsg =''
    return render_template('index.html', output=msgFilter)
@app.route('/chat/reset')
def reset_chat():
    global chatCount
    chatCount =0
    global msgFilter
    global allMsg
    msgFilter = []
    allMsg =''
    return render_template('chat.html', output=msgFilter)
def generateF(msg):
    gptOuput=GPT35Chat()
    output=gptOuput.generatorChatF(escape(msg))
    global allMsg
    print('print测试1：'+allMsg)
    allMsg = allMsg+'\n\n'+output
    return output
def generateM(msg):
    gptOuput=GPT35Chat()
    output=gptOuput.generatorChatM(escape(msg))
    global allMsg
    allMsg = allMsg+'\n\n'+output  
    print('print测试2：'+allMsg) 
    return output

def generateD(msg):
    gptOuput=GPT35Chat()
    output=gptOuput.generatorChatD(escape(msg))
    global allMsg
    allMsg = allMsg+'\n\n'+output
    print('print测试3：'+allMsg)    
    return output
 
def generateGPT(msg):
    gptOuput=GPT35Chat()
    output=gptOuput.generator(escape(msg))
    print('print测试4：'+'')
    return output
if __name__ == '__main__':                                                      
    app.run(debug=True) 


