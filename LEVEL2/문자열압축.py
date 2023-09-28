def compress(text, tok_len):
    # print(range(0, len(text), tok_len))
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)] # tok_len 길이로 문자열 나누기
    res = []
    cur_word = words[0]
    cur_cnt = 1
    # print('words:',words)
    # print(words, words[1:] + [''])
    for a, b in zip(words, words[1:] + ['']): # zip으로 원본 문자열과 한칸 뒤부터 시작하는 문자열 비교
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
        # print('res:',res)
    
    # print(list(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res))
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    # tok_len: 문자열 반절까지와 전체 길이
    # print(list(range(1, int(len(text)/2) + 1)) + [len(text)])
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])


print(solution(input()))

'''
def solution(s):
    answer = len(s)
    for x in range(1, int(len(s)/2)+1):
        d = 0
        comp = ''
        c = 1
        for i in range(0, len(s), x):
            temp = s[i:i+x]
            if comp == temp:
                c += 1
            elif comp != temp:
                d += len(temp)
                if c > 1:
                    d += 1 #len("{}".format(c))
                c = 1
                comp = temp
        if c > 1:
            d += 1 # len("{}".format(c))
        answer = min(answer, d)
    return answer
'''

'''
내풀이)
def solution(s):
    answer = []
    for n in range(1, len(s)+1):
        split_data = list(map(''.join, zip(*[iter(s)]*n))) # 문자열 n 단위로 자르기
        remainder = []
        if len(split_data)*n != len(s):
            remainder = s[len(split_data)*n:]
        cnt = 1
        result = ""
        split_data.append('-1') # 마지막 문자열들 result에 추가하기 위해서 
        tmp = split_data[0]
        for i in range(1,len(split_data)):
            if tmp == split_data[i]:
                cnt += 1
            else:
                if cnt >1:
                    result += str(cnt) + split_data[i-1]
                else:
                    result += split_data[i-1]
                cnt = 1
                tmp = split_data[i]
        answer.append(len(result) + len(remainder))
    return min(answer)

print(solution(input()))

문자열을 n 단위로 나눔, 나머지 부분은 따로 받아놓음

for문을 한번 더 돌면서 같은 문자열 개수 카운트하고 
개수와 알파벳을 붙여서 string 만든다

결과 string 길이 계산 후 가장 작은 경우 출력
'''