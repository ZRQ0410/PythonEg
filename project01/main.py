"""
    游戏入口
"""
"""
    没有加入判断是否可以移动的功能：如：
            2 0 0 0 
            2 0 0 0
            2 0 0 0
            2 0 0 0  不能向左移动，但实际运行中无提醒且会产生新的数字
"""
from project01.usl import GameConsoleView

if __name__ == '__main__':
    view = GameConsoleView()
    view.main()
