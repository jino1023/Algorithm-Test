def solution(input_string):
    loners = [] # 외톨이 알파벳들을 저장할 리스트
    
    # 각 알파벳별로 등장한 부분을 기록할 딕셔너리를 초기화합니다.
    positions = {}
    for char in input_string:
        positions[char] = []
    
    # 문자열을 순서대로 탐색하면서, 각 알파벳이 등장한 위치를 기록합니다.
    for i in range(len(input_string)):
        char = input_string[i]
        positions[char].append(i)
        
    # 등장한 부분이 1개인 알파벳들은 외톨이 알파벳이 될 수 없습니다. 제외합니다.
    for char, pos in positions.items():
        if len(pos) == 1:
            continue
            
        # 등장한 부분이 2개 이상인 알파벳들을 처리합니다.
        prev_pos = pos[0] # 이전 등장 위치를 저장할 변수
        for p in pos[1:]: # 현재 등장 위치부터 시작해서 이전 등장 위치와 비교합니다.
            if p - prev_pos > 1: # 두 등장 위치 사이에 다른 알파벳이 있는 경우
                loners.append(input_string[prev_pos]) # 이전 등장 위치의 알파벳은 외톨이 알파벳입니다.
                break # 더 이상 비교하지 않습니다.
            prev_pos = p # 현재 등장 위치를 이전 등장 위치로 설정합니다.
        else: # for문이 break 없이 끝났다면, 외톨이 알파벳이 아닙니다.
            continue
             
    # 외톨이 알파벳들을 알파벳순으로 이어붙인 문자열을 반환합니다.
    if len(loners) == 0:
        return "N"
    else:
        loners.sort() # 외톨이 알파벳들을 알파벳순으로 정렬합니다.
        return "".join(loners)

print(solution("edeaaabbccd")) # "de"
print(solution("eeddee")) # "e"
print(solution("string")) # "N"
print(solution("zbzbz")) # "bz"
