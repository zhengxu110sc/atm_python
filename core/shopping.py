#购物模块，实现信用卡购物，将物品加载到购物车，和自动生成购物记录以及购物日志文件。
import os,sys,json,logging

# 创建主程序目录
Base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 导入到配置文件
sys.path.append(Base_dir)
# 定义购物商城模块。
def shopping_mall(acc_data):
    print("选购商品")


# 定义购物车模块
def shopping_car(acc_data):
    print("购物车")


# 定义结账模块
def payment(acc_data):
    print("结账")




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
            
