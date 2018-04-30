#认证页面
import os,sys,json
# 创建主程序目录
Base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 导入到配置文件
sys.path.append(Base_dir)

from conf import settings #导入配置页面
user_data_file=settings.data_path["acc"]
# 创建用户验证装饰器
def login_requird(func):
    def wrapper(args):
        if args["is_login"]is True:
            func(args)
        else:
            print("对不起，当前用户尚未登录.")
    return wrapper

def is_login(acc_data):
    if acc_data["is_login"]==False:
        count=0
        while count<3:
            input_name = input("\33[34;0m请输入用户名:\33[0m")
            input_pwd = input("\33[34;0m请输入密码:\33[0m")
            with open(user_data_file, "r+", encoding="utf-8") as f:
                user_data = json.dumps(f.read())
                user_info = json.loads(user_data)
                if input_name == user_info["name"] and input_pwd == user_info["password"]:
                    acc_data = user_info
                    acc_data["is_login"] == True
                    return acc_data
                else:
                    print("用户名或密码错误，请重新输入。")
                    count+=1
        else:
            print("非法操作，密码错误超过三次，请三个小时后再登录。")
    else:
        print("\33[34;0m欢迎%s登录本系统\33[0m"%acc_data["name"])
        return acc_data



        
