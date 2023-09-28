from collections import deque

def solution(order):
    stack = deque()
    order = deque(order)
    num = 1
    cnt = 0
    while order:
        if order[0] in stack: # -> O(n) 이라서 지양
            if order[0] == stack[-1]:
                cnt += 1
                order.popleft()
                stack.pop()
            else:
                break
        else:
            if order[0] != num:
                stack.append(num)
            else:
                cnt += 1
                order.popleft() 
            num += 1
    return cnt

print(solution(list(map(int, input().split()))))

'''
시간초과
'''