# 主程序页面
import os,sys
# 创建主程序目录
Base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 导入到配置文件
sys.path.append(Base_dir)
# 创建一个空的数据文件，将其放入到内存区域中，用来进行首次登陆做替换用。
user_dict={
    "is_login":False,
    "name":None,
    "account":None
}
def run(run_type):
    if run_type=="atm":
        print(run_type)
        pass
    elif run_type=="manage":
        print("manage")
        pass
