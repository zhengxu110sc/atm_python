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
            print("\33[34;0m欢迎%s登录本系统\33[0m".center(40,"-")%acc_data["name"])
            return func(acc_data)
        else:
            print("\33[34;0m对不起，当前用户尚未登录\33[0m")
    return wrapper

# 打开对应文件，并且对用户名和密码进行对比:
def open_file(acc_date):
    #这里通过路径映射出user_data数据文件。
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
            return acc_date
    else:
        print("用户不存在。")

#查询用户并登录
def select_user(acc_data):
    login_count=0
    if acc_data["is_login"]==False:
        while login_count<3:
            acc_data["name"] = input("请输入您的用户名进行登录>>").strip()
            acc_data["password"] = int(input("请输入密码>>:").strip())
            acc_data=open_file(acc_data)
            if acc_data["is_login"]==True:
                return acc_data
            else:
                login_count+=1
        else:
            exit("密码输错三次，系统强制退出")

    else:
        acc_data=open_file(acc_data)
        return acc_data



# def select_info(args):
#     lg_count=0
#     acc_data={}
#     if args["is_login"]==False:
#         while lg_count < 3:
#             acc_id=input("\33[34;0m请输入您的用户名:\33[0m")
#             acc_pwd=input("\33[34;0m请输入您的密码:\33[0m")
#             if acc_id in user_dict:
#                 acc_data=user_dict[acc_id]
#                 if acc_id == acc_data["username"] and acc_pwd==acc_data["password"]:
#
#                     acc_data["is_login"]=True
#                     return acc_data
#                 else:
#                     print("\33[34;0m密码输入错误，请检查后重新输入。\33[0m")
#                     lg_count+=1
#             else:
#                 print("\33[34;0m当前用户不存在。\33[0m")
#                 lg_count+=1
#         else:
#             print("\33[34;0m密码输错三次，当前账户将被锁定\33[0m")
#     else:
#         acc_data=args
#         return acc_data