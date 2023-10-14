q = int(input())
stack_push = []
stack_pop = []
for i in range(q):
    query = input().split()
    if '+' in query:
        new_elem = int(query[1])
        if not stack_push:
            substack_min = new_elem
        else:
            substack_min = min(new_elem, stack_push[-1][1])
        stack_push.append((new_elem, substack_min))
    else:
        if not stack_pop:
            while stack_push:
                deleted_elem = stack_push.pop()[0]
                if not stack_pop:
                    substack_min = deleted_elem
                else:
                    substack_min = min(deleted_elem, stack_pop[-1][1])
                stack_pop.append((deleted_elem, substack_min))
        stack_pop.pop()
    if (not stack_push) or (not stack_pop):
        if not stack_push:
            if not stack_pop:
                print(-1)
            else:
                print(stack_pop[-1][1])
        else:
            print(stack_push[-1][1])
    elif (not stack_push) and (not stack_pop):
        print(-1)
    else:
        print(min(stack_push[-1][1], stack_pop[-1][1]))
