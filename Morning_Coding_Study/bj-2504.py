# 열면 시작 닫히면 종료 1 > 괄호는 곱 2 대괄은 곱 3
# (()[[]])([])
# 2*(2*(1)+3*3*(1))+2*(3*(1))

# 답안

s = input()
stack = []

for i in s:
    if i == '(' or i == '[':
        stack.append(i)
    else:
        temp = 0
        while stack:
            top = stack.pop()
            if i == ')' and top == '(':
                stack.append(2 if temp == 0 else 2 * temp)
                break
            elif i == ']' and top == '[':
                stack.append(3 if temp == 0 else 3 * temp)
                break
            elif isinstance(top, int):
                temp += top
            else:
                print(0)
                exit(0)

        else:
            print(0)
            exit(0)

result = 0
for i in stack:
    if isinstance(i, int):
        result += i
    else:
        print(0)
        exit(0)

print(result)


# (()[[]])([])
# (2[3])(3)
# (2+9)6
# (11)6
# 22+6
# 28

# (()[[]])
# (2[3])
# (2+9)
# 22

# 오답
"""
import re

G = input()
while True:
    value = G
    G = G.replace('()', '2')
    G = G.replace('[]', '3')
    if G == value:
        G = re.sub(r'(\d+)\((\d+)\)', lambda m: str(int(m.group(1))+ (2 * int(m.group(2)))), G)
        G = re.sub(r'(\d+)\[(\d+)\]', lambda m: str(int(m.group(1))+ (3 * int(m.group(2)))), G)
        G = re.sub(r'\((\d+)\)(\d+)', lambda m: str((2 * int(m.group(1))) + int(m.group(2))), G)
        G = re.sub(r'\[(\d+)\](\d+)', lambda m: str((3 * int(m.group(1))) + int(m.group(2))), G)
        G = re.sub(r'\((\d+)\)\((\d+)\)', lambda m: str((2*int(m.group(1)))+ (2 * int(m.group(2)))), G)
        G = re.sub(r'\((\d+)\)\[(\d+)\]', lambda m: str((2*int(m.group(1)))+ (3 * int(m.group(2)))), G)
        G = re.sub(r'\((\d+)\)\[(\d+)\]', lambda m: str((2 * int(m.group(1))) + (3 * int(m.group(2)))), G)
        G = re.sub(r'\[(\d+)\]\[(\d+)\]', lambda m: str((3 * int(m.group(1))) + (3 * int(m.group(2)))), G)
        G = re.sub(r'\((\d+)\)', lambda m: str(2 * int(m.group(1))), G)
        G = re.sub(r'\[(\d+)\]', lambda m: str(3 * int(m.group(1))), G)
    # print(G)
    if G == value:
        break

result = int(G) if G.isdigit() else 0
print(result)
"""