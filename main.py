def show_menu():
    print("\n====== 学生信息管理系统 ======")
    print("1. 添加学生")
    print("2. 查看所有学生")
    print("3. 按学号查询学生")
    print("4. 修改学生信息")
    print("5. 删除学生")
    print("6. 退出")


def main():
    while True:
        show_menu()
        choice = input("请输入你的选择: ").strip()

        if choice == "1":
            print("你选择了：添加学生")
        elif choice == "2":
            print("你选择了：查看所有学生")
        elif choice == "3":
            print("你选择了：按学号查询学生")
        elif choice == "4":
            print("你选择了：修改学生信息")
        elif choice == "5":
            print("你选择了：删除学生")
        elif choice == "6":
            print("程序退出，再见！")
            break
        else:
            print("输入无效，请输入 1~6。")


if __name__ == "__main__":
    main()