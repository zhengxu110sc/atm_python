# 主程序页面
import os,sys
# 创建主程序目录
Base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 导入到配置文件
sys.path.append(Base_dir)
# 导入验证页面
from core import auth
from core.auth import is_login
from core.credit import credit_center
from core.shopping import shopping_center
from core.personal import personal_center

# 创建一个空的
# 数据文件，将其放入到内存区域中，用来进行首次登陆做替换用。
user_dict={
    "is_login":False,
    "name":None,
    "account":None
}
#定交互程序。
@is_login
def interactive(acc_data):
    print_menu=u"""
    \33[34;0m请输入序号，进入相应的程序。
    1>>购物中心
    2>>个人中心
    3>>信用卡中心
    q>>退出当前程序。
    \33[0m    
    """

    interactive_menu={
        "1":shopping_center,
        "2":personal_center,
        "3":credit_center,
    }
    while True:
        print(print_menu)
        choice_id=input("\33[34;0m请输入您的选择,退出请按【q】>>:\33[0m").strip()
        if choice_id.isdigit() and int(choice_id)<len(interactive_menu):
            interactive_menu[choice_id](acc_data)
        elif choice_id=="q":
            exit("感谢您使用本系统。")
        else:
            print("对不起，非法操作，请重新输入。")

        


def run(run_type):
    if run_type=="atm":
        acc_data=auth.select_user(user_dict)
        interactive(acc_data)


    elif run_type=="manage":
        print("manage")
        pass
