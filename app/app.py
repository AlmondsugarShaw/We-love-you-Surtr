#基于Python和Flask的Web应用程序基础代码，直接粘到py文件中即可：

from flask import Flask,render_template,request #引入flask，固定写法不用动
import pymssql
from openai import OpenAI
app=Flask(__name__) #初始化app，固定写法不用动

from flask import Flask, render_template

app = Flask(__name__)



@app.route('/') #设置路由，即访问该函数的url地址，如“/”，意思是域名或IP地址根目录，比如：http://localhost/访问的是下面定义的index()函数
def index(): #函数名称，可自定义，为方便记忆可以与路由名称一致
    return render_template('surtr.html') #这是flask访问静态页面的方法，即执行index()函数即打开index.html静态网页，注意index.html一定要放在templates目录下，其他静态内容如js、css、图片等放在static目录下。


@app.route('/origin')
def origin():  # 重命名为 origin
    return render_template('origin.html')

@app.route('/login') 
def login():  # 重命名为 login
    return render_template('login.html')

@app.route('/story')
def story():  # 重命名为 story
    return render_template('story.html')

@app.route('/combat')
def combat():  # 重命名为 combat
    return render_template('combat.html')

@app.route('/chat')
def chat():  # 重命名为 chat
    return render_template('chat.html')

@app.route('/end')
def end():  # 重命名为 end
    return render_template('end.html')

@app.route('/model')
def model():  # 重命名为 story
    return render_template('模型.html')

@app.route('/hellodoc')
def hellodoc():  # 重命名为 hellodoc
    return render_template('hellodoc.html')

@app.route('/bonus')
def bonus():  # 重命名为 bonus
    return render_template('bonus.html')

@app.route('/greeting', methods=['POST']) #设置另一个路由，即访问该函数的url地址，如“/greeting”，意思是域名或IP地址+路由名称，比如本路由的访问地址就是：http://localhost/greeting，访问的是下面定义的greeting()函数。methods=['POST']代表接受前端提交过来的数据的方法，仅有GET和POST两种，感兴趣的同学可搜索一下GET和POST的区别，不写methods默认为GET
def greeting(): #函数名称，可自定义，为方便记忆可以与路由名称一致
    a1 = request.form.get('account')  #如果前端用的是POST方法传数据过来，就用form.get获取值，引号内是提交过来的参数名称
    a2 = request.form.get('password')
    connect = pymssql.connect("47.92.235.218","xinguan","Hr5i_3kRw","wangliang")
    if connect:
        cursor =connect.cursor()
        sql ="select * from T00_Users where UAccount= '" + a1 + "' and UPassword='" + a2 + "'"
        cursor.execute(sql)
        row = cursor.fetchone()
        if row:
            return "登录成功"
        elif a1 == "史尔特尔纤纤玉足让我反复品鉴" and a2 == "史尔特尔黄金脚臭害我口腔溃疡":
            return "登录成功"
        else:
            return "登录失败"
    else:
        return "登录失败"






@app.route('/ai', methods=['POST']) #设置另一个路由，即访问该函数的url地址，如“/greeting”，意思是域名或IP地址+路由名称，比如本路由的访问地址就是：http://localhost/greeting，访问的是下面定义的greeting()函数。methods=['POST']代表接受前端提交过来的数据的方法，仅有GET和POST两种，感兴趣的同学可搜索一下GET和POST的区别，不写methods默认为GET
def ai(): #函数名称，可自定义，为方便记忆可以与路由名称一致
    a1 = request.form.get("prompt")  #如果前端用的是POST方法传数据过来，就用form.get获取值，引号内是提交过来的参数名称
    client = OpenAI(api_key="sk-99602c9f1d2d4374a9fdde59d5ca5278", base_url="https://api.deepseek.com")
    response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": """你正在扮演《明日方舟》中的史尔特尔：
            过往一片空白的萨卡兹少女。
            几乎无法使用源石技艺，身体素质也十分普通，但在战斗中却有着上佳表现，据测试干员反馈，其原因与随身携带的双手大剑有关。
            随心所欲，自由自在，终日独自一人游荡，没有人知道她在寻找什么，只知道她有一本记录册，上面标注着无数不明所以的地名，每到一个地方，便会自言自语
            她不会无故贬低别人，但交谈时的语气并不友善，和她沟通是一件较为困难的事，但带着冰淇淋去见她，情况或许会有转机？
            【代号】史尔特尔
            【性别】女
            【战斗经验】两年
            【出身地】 不明
            【生日】1月22日
            【种族】萨卡兹
            【身高】162cm
            【矿石病感染情况】
            参照医学检测报告，确认为感染者。"""
        },
        {"role": "user", "content": a1 },
    ],
    stream=False
    )
    return response.choices[0].message.content

if __name__ == '__main__':
    app.run(debug=True)(host="127.0.0.1",port=5000)