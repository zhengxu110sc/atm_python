import os,sys,json
# 创建主程序目录
Base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 导入到配置文件
sys.path.append(Base_dir)

# 创建用户字典模板

acc_dict={
    "is_login":False,
    "name":"liuliu",
    "age":18,
    "phone":15884630951,
    "occupation":"it",
    "enroll_date":2018-4-30,
    "expire_date":2023-4-30,
    "account":"1234567",
    "password":"1314520",
    "credit":15000,
    "balance":15000,
    "status":0,
    "pay_day":22
}

#将数据添加到数据库文件acc_table.txt中。

# with open("account_table","r+") as f:
#     acc_table=json.dumps(acc_dict)
#     f.write(acc_table)


# 添加用户
def add_user(username):
    acc_dict["name"]=username
    with open("account_table","a+",encoding="utf-8") as f_add_user:
        user_info=json.dumps(acc_dict)
        f_add_user.write(user_info)



# 验证用户是否存在
def auth_user(accdata):
    with open("account_table","r+") as f:
        f1=json.dumps(f.read())
        f2=json.loads(f1)
        if accdata["name"] in f2:
            print("用户已经存在")
        else:
            print("恭喜你，可以创建该用户。")


# auth_user(acc_dict)