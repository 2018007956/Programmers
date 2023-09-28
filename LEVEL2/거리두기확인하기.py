def solution(places):
    answer = []
    for place in places:
        
        res = []
        P_idx = {}
        for i in range(5):
            for j in range(5):
                if place[i][j] =='P':
                    P_idx[(i,j)]=i+j
        # value를 기준으로 오름차순
        P_idx = sorted(P_idx.items(), key=lambda item:item[1])
        P_idx = list(dict(P_idx).keys())
        # print(P_idx) 
        
        diff_idx = []
        for a, b in zip(P_idx, P_idx[1:]): # zip으로 원본 문자열과 한칸 뒤부터 시작하는 문자열 비교
            diff_idx.append(abs(a[0]-b[0])+abs(a[1]-b[1]))
        # print(diff_idx)

        if 1 in diff_idx:
            res.append(0) # 거리두기X
        else: # 2인경우 사이에 O(빈테이블)가 존재하면 거리두기 X
            chk = 0
            for i in range(len(diff_idx)):
                if diff_idx[i] ==2:
                    # print('비교:',P_idx[i], P_idx[i+1])
                    a, b = P_idx[i], P_idx[i+1]
                    if a[0] == b[0]: # 열이 같음
                        if place[a[0]][(a[1]+b[1])//2] == "O":
                            res.append(0)
                        else:
                            res.append(1)
                    elif a[1] == b[1]: # 행이 같음
                        if place[(a[0]+b[0])//2][a[1]] == "O":
                            res.append(0)
                        else:
                            res.append(1)
                    else: # 대각선인 경우
                        if place[a[0]][b[1]] == "O" or place[b[0]][a[1]]=='O':
                            res.append(0)
                        else:
                            res.append(1)
                    chk = 1
            if chk==0: # 모든 원소가 2보다 크면 모두 거리두기 잘 지킴
                res.append(1)
        # 한명이라도 거리두기 못지키면 못지킴
        answer.append(0) if 0 in res else answer.append(1)
    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))

'''
실패
P위치를 (x,y) 형태로 다 뽑아서 x+y가 작은 순으로 나열
옆에 위치와 맨해튼거리를 계산해서, 거리가 1인 경우는 return 0 (거리두기X)
모든 수가 2이상인 경우는 return 1, 
그리고 2인 경우는 근처에 O(빈테이블)가 있는지 확인해서 하나라도 있으면 return 0 
'''