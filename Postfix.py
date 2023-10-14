postfix = input().split()
operations = '+-/*'
stack = []
final_ans = 0
for s in postfix:
    if s not in operations:
        stack.append(s)
    else:
        final_ans = eval(stack.pop(-2) + s + stack.pop(-1))
        stack.append(str(final_ans))
print(final_ans)
