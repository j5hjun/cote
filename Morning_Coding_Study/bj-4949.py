from collections import deque

while True:
    text = input()

    True if text else False

    L = deque()
    for i in text:
        if i == '(' or i == ')' or i == '[' or i == ']':
            L.append(i)
    while L:
        t = L.popleft()
        tc = L.popleft()
        print(t, tc)
        # 연속된 것을 찾아서 없애 > 마지막에 남는게 있으면 no
        if t == '(':
            if tc == ')':
                pass
            else:
                L.append(t)
                L.append(tc)
        elif t == '[':
            if tc == ']':
                pass
            else:
                L.append(t)
                L.append(tc)
    print('no' if L else 'yes')