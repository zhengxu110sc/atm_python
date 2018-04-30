import os,sys,json
# 创建主程序目录
Base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 导入到配置文件
sys.path.append(Base_dir)

# 创建用户列表数据库

acc_dict={"name":"lisi","is_login":False,"age":18,"phone":15884630951,"occupation":"it","enroll_date":2018-4-30,"expire_date":2023-4-30,"account":1234567,"password":1314520,"credit":15000.0,"balance":15000.0,"status":0,"pay_day":22,}


def add_user():
    name=input("name>>>:")
    acc_dict["name"]=name
    file_name="%s.txt"%name
    with open(file_name,"w+")as f:
        f_user=json.dumps(acc_dict)
        f.write(f_user)


add_user()