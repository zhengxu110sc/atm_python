# 主程序页面
import os,sys
# 创建主程序目录
Base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 导入到配置文件
sys.path.append(Base_dir)
# 导入验证页面
from core import auth
from core.auth import is_login
# 创建一个空的
# 数据文件，将其放入到内存区域中，用来进行首次登陆做替换用。
user_dict={
    "is_login":False,
    "name":None,
    "account":None
}
@is_login
def interactive(acc_data):
    print(acc_data)
def run(run_type):
    if run_type=="atm":
        acc_data=auth.select_user(user_dict)
        interactive(acc_data)


    elif run_type=="manage":
        print("manage")
        pass
