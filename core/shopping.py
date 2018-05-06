#购物模块，实现信用卡购物，将物品加载到购物车，和自动生成购物记录以及购物日志文件。
import os,sys,json,logging

# 创建主程序目录
Base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 导入到配置文件
sys.path.append(Base_dir)
from conf import settings
#打开商品列表文件。
product_list=settings.data_path["acc"] + r"product_list.txt"


#展示商品列表，并且将其放入购物车。
def shopping_list(acc_date):
    pro_list=[]
    shopping_car=[]
    if acc_date["is_login"]==True:
        with open(product_list,"r+",encoding="utf-8") as f_product_list:
            for item in f_product_list:
                pro_list.append(item.strip("\n").split())#剔除换行符和以此为分割。
        def pro_info():
            print("\33[34;0m编号:\t商品:\t\t价格:\33[0m")
            for index, item in enumerate(pro_list):
                print("%s\t\t%s\t\t%s" % (index, item[0], item[1]))

        while True:
            print("\33[30;0m以下是商品信息：\33[0m")
            pro_info()
            choice_id = input("\33[31;0m购买商品，请输入相应序号，结束，请输入b\33[0m").strip()
            if choice_id.isdigit():
                choice_id=int(choice_id)
                if choice_id<len(pro_list) and choice_id>=0:
                    shopping_car.append(pro_list[choice_id])
                    print("商品%s已经加入购物车,价格为%s"%(pro_list[choice_id][0],pro_list[choice_id][1]))
                else:
                    print("对不起，商城中没有您要选择的商品。")
            elif choice_id=="b":
                sum=0
                for item in shopping_car:
                    sum+=int(item[1])
                f_user_shopping={"username":acc_date["name"],
                    "shopping_car":shopping_car,
                    "price":float(sum)
                    }
                shopping_car_record = settings.data_path["acc"] + r"%s_shopping_car_record.txt"%acc_date["name"]

                with open(shopping_car_record,"w+") as f:
                    # shopping_record=json.loads(f.read())
                    shopping_record=json.dumps(f_user_shopping)
                    f.write(shopping_record)
                print("当前购物车的商品有%s,总价为:%s"%(shopping_car,sum))
                break
    else:
        exit("当前用户未登录")




# 定义购物商城模块。
def shopping_mall(acc_data):
    shopping_list(acc_data)
    print("选购商品")


# 定义购物车模块,并且询问其是否结账。
def shopping_car(acc_data):
    f_shopping_car=settings.data_path["acc"]+r"%s_shopping_car_record.txt"%acc_data["name"]
    with open(f_shopping_car,"r+",encoding="utf-8") as f:
        shopping_car_record=json.loads(f.read())
        print("\33[34;0m%s当前购物车中的物品有\33[0m".center(30,"-")%acc_data["name"])
        print(shopping_car_record["shopping_car"])

def null_shopping_car(acc_data):
    f_shopping_car = settings.data_path["acc"] + r"%s_shopping_car_record.txt" % acc_data["name"]
    with open(f_shopping_car,"r+") as f:
        shopping_car_record=json.loads(f.read())
        shopping_car_record["shopping_car"]=[]
        new_record=json.dumps(shopping_car_record)
        with open(f_shopping_car,"w") as f:
            f.write(new_record)




# 定义结账模块,调用信用卡模块，实现结账功能和修改余额功能。
def payment(acc_data):
    user_file=settings.data_path["acc"]+r"%s_shopping_car_record.txt"%acc_data["name"]#打开用户对应的购物车记录。
    with open(user_file,"r+") as f:
        user_data=json.loads(f.read())
        if user_data["shopping_car"]:
            acc_data["balance"] = float(acc_data["balance"] - user_data["price"])  # 计算新的余额,blance.
            print("恭喜用户%s结账成功。当前用户余额为%s" % (acc_data["name"], acc_data["balance"]))
            null_shopping_car(acc_data)
        else:
            print("对不起，用户尚未购买商品。")


    user_info_file=settings.data_path["acc"]+r"%s.txt"%acc_data["name"]#将accdata中的数据重新写入到文件中。
    with open(user_info_file,"w") as f:
        new_acc_data=json.dumps(acc_data)
        f.write(new_acc_data)


def shopping_center(acc_data):
    print("\33[32;0m欢迎%s进入购物中心，祝您购物愉快\33[0m".center(30,"-")%acc_data["name"])
    print_menu=u"""\33[31;0m
    1>>购物商城
    2>>查看购物车
    3>>结账
    q>>退出\33[0m    
    """
    choice_menu={
                "1":shopping_mall,
                "2":shopping_car,
                "3":payment,
    }
    while True:
        print(print_menu)
        choice_id=input("\33[31;0m请输入序号，选择你想进入的程序，退出请按【q】>>:\33[0m")
        if choice_id.isdigit():
            choice_menu[choice_id](acc_data)
        elif choice_id=="q":
            break
            
