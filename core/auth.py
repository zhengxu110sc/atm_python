#认证页面
import os,sys,json
# 创建主程序目录
Base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 导入到配置文件
sys.path.append(Base_dir)

# 导入设置模块
from conf import settings

# 装饰器函数，用来判断用户是否登录
def is_login(func):
    def wrapper(acc_data):
        if acc_data["is_login"]:
            print("\33[34;0m欢迎%s登录本系统\33[0m"%acc_data["name"])
            return acc_data
        else:
            print("\33[34;0m对不起，当前用户尚未登录\33[0m")
    return wrapper

# 打开对应文件，并且对用户名和密码进行对比:
def open_file(acc_date):
    user_data = settings.data_path["acc"] + r"%s.txt"%acc_date["name"]
    if user_data:
        with open(user_data,"r+")as f:
            user_datas=json.loads(f.read())
        if acc_date["name"]==user_datas["name"] and acc_date["password"]==user_datas["password"]:
            user_datas["is_login"]=True
            acc_date=user_datas
            return acc_date
        else:
            print("用户名或密码错误。")
    else:
        print("用户不存在。")

#查询用户并登录
def select_user(acc_data):
    if acc_data["name"]==None:
        acc_data["name"]=input("请输入您的用户名进行登录>>").strip()
        acc_data["password"]=int(input("请输入密码>>:").strip())
        acc_data=open_file(acc_data)
        return acc_data
    else:
        acc_data=open_file(acc_data)
        return acc_data



