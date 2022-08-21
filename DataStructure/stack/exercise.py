"""
    逆波兰表达式

    Eg.
    1 3 + 4 * 5 - p
    为 1+3 的值 *4 再 -5，p表示结束
"""

from sstack import *


st = SStack()

while True:
    exp = input()
    tmp = exp.split(' ')
    for i in tmp:
        if i not in ['+', '-', '*', '/', 'p']:
            st.push(float(i))
        elif i == '+':
            y = st.pop()
            x = st.pop()
            st.push(x+y)
        elif i == '-':
            y = st.pop()
            x = st.pop()
            st.push(x-y)
        elif i == '*':
            y = st.pop()
            x = st.pop()
            st.push(x*y)
        elif i == '/':
            y = st.pop()
            x = st.pop()
            st.push(x/y)
        elif i == 'p':
            print(st.top())
