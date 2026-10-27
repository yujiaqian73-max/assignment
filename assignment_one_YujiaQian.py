import random
import turtle as t


def draw_python():
    """选项 1：绘制 Python 蛇"""
    t.clearscreen()
    t.setup(800, 300)
    t.penup()
    t.fd(-150)
    t.pendown()
    t.seth(-40)
    t.pensize(25)
    t.pencolor("purple")

    for _ in range(4):
        t.circle(40, 80)
        t.circle(-40, 80)
    t.circle(40, 80 / 2)
    t.fd(40)
    t.circle(16, 180)
    t.fd(40 * 2 / 3)
    t.done()


def draw_spiral():
    """选项 2：绘制彩色螺旋线"""
    t.clearscreen()
    t.setup(600, 600)
    t.bgcolor("black")
    x = 1
    t.speed(0)
    t.colormode(255)

    while x < 400:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        t.pencolor(r, g, b)
        t.fd(50 + x)
        t.rt(90.991)
        x = x + 1

    t.exitonclick()


def draw_star():
    """选项 3：绘制五角星"""
    t.clearscreen()
    t.setup(600, 600)
    t.speed(5)
    t.bgcolor("black")
    t.colormode(255)

    t.pencolor(
        random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)
    )
    t.fillcolor("gold")
    t.pensize(5)

    t.begin_fill()
    for _ in range(5):
        t.forward(150)
        t.right(144)
    t.end_fill()
    t.exitonclick()


def run_qa_bot():
    """选项 4：QA 问答机器人"""
    print("\n--- QA Bot Started ---")
    print("输入 'quit' 可以退出机器人返回主菜单。")
    print("支持的关键词：hku, robot, jetson, ai, human")

    while True:
        question = input("\nYour question: ").strip().lower()

        if question == "quit":
            print("退出 QA Bot...")
            break

        if "hku" in question:
            print("Bot: HKU (The University of Hong Kong) is a top-tier global university.")
        elif "robot" in question:
            print("Bot: Robots are programmable machines capable of automated actions.")
        elif "jetson" in question:
            print(
                "Bot: NVIDIA Jetson is an embedded computing board for edge AI and robotics."
            )
        elif "ai" in question:
            print("Bot: AI enables machines to mimic human intelligence.")
        elif "human" in question:
            print("Bot: Humans are biological beings known for creativity and emotion.")
        else:
            print(
                "Bot: 没听懂哦，试试问关于 hku, robot, jetson, ai 或 human 的问题吧！"
            )


def run_calculator():
    """选项 5：简易计算器"""
    print("\n--- Simple Calculator Started ---")
    try:
        num1 = float(input("请输入第一个数字: "))
        operator = input("选择运算符 (+, -, *, /): ").strip()
        num2 = float(input("请输入第二个数字: "))

        if operator == "+":
            print(f"计算结果: {num1} + {num2} = {num1 + num2}")
        elif operator == "-":
            print(f"计算结果: {num1} - {num2} = {num1 - num2}")
        elif operator == "*":
            print(f"计算结果: {num1} * {num2} = {num1 * num2}")
        elif operator == "/":
            if num2 == 0:
                print("错误：除数不能为 0！")
            else:
                print(f"计算结果: {num1} / {num2} = {num1 / num2}")
        else:
            print("错误：无效的运算符！")

    except ValueError:
        print("错误：请输入有效的数字。")


def main():
    """主菜单循环"""
    while True:
        print("\n========================================")
        print("         主菜单 - 选择要运行的程序          ")
        print("========================================")
        print(" 1. 画 Python 蛇")
        print(" 2. 画彩色螺旋线")
        print(" 3. 画五角星")
        print(" 4. 运行 QA 问答机器人")
        print(" 5. 运行简易计算器")
        print(" 0. 退出程序")

        choice = input("\n请输入数字选择对应的程序 (0-5): ").strip()

        if choice == "1":
            draw_python()
        elif choice == "2":
            draw_spiral()
        elif choice == "3":
            draw_star()
        elif choice == "4":
            run_qa_bot()
        elif choice == "5":
            run_calculator()
        elif choice == "0":
            print("程序已退出，再见！")
            break
        else:
            print("[错误] 请输入 0 到 5 之间的有效数字！")


if __name__ == "__main__":
    main()
