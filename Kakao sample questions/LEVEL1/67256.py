# 2020 카카오 인턴십 > 키패드 누르기
def solution(numbers, hand):
    answer = ''
    '''
    1,4,7 -> L
    3,6,9 -> R
    2,5,8,0 -> 현재 손 위치(앞 번호) 파악
    
    2차원 배열로 위치를 나타내지 않아도 좌우숫자의 뺄셈으로 거리 계산 가능 
    -> *,0,# 문제 & 5와 8은 거리 1인데 뺄셈 하면 안됨
    -> 거리로 변환 해야 할듯
    
    012
    345
    678
    -> -1씩 하고 나누기 3했을때 몫=행, 나머지=열
    -> 0은 예외
    이거 생각해내니깐 금방 해결됨
    '''
    # 거리 변환
    last_L, last_R = [3,0], [3,2]
    pos = []
    for i in numbers:
        if i==0:
            pos.append([3,1])
            continue
        num=i-1
        pos.append([num//3, num%3])
    
    for idx, p in enumerate(pos):
        if p[1]==0: #1,4,7
            answer += 'L'
            last_L = p 
        elif p[1]==2: #3,6,9
            answer += 'R'
            last_R = p
        else: #2,5,8,0
            dist_L = abs(p[0]-last_L[0]) + abs(p[1]-last_L[1])
            dist_R = abs(p[0]-last_R[0]) + abs(p[1]-last_R[1])
            if dist_L == dist_R:
                if hand =='left':
                    answer += 'L'
                    last_L = p
                else:
                    answer += 'R'
                    last_R = p
            elif dist_L < dist_R:
                answer += 'L'
                last_L = p
            else:
                answer += 'R'
                last_R = p                        
    return answer

'''
[다른 사람 풀이]
position을 미리 key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)} 로 만들어 놓고 진행
나머지 last_R,L기억해놓고 거리 구하는것 등은 똑같음

'''