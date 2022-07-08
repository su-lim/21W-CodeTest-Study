def solution(number, k):

    answer = ''
    N = len(number) # input 값 길이
    length = N-k # 구할 답 길이
    index = -1 # 현재 index

    while length > 0:
        
        if length == N-index-1: # 남아있는 배열이 남은 답의 길이와 같을 때
            answer += number[index+1:]
            break
            
        maximum = "0"
        for num_idx, num in enumerate(number[index+1: N-length+1]):
            if num == "9": # 9이면 비교 안하고 바로 answer에 넣음
                temp = 1 + index + num_idx # 현재 index에 max index 더함
                maximum = "9"
                break
            if num > maximum: # max 값 찾는 알고리즘
                maximum = num
                temp = 1 + index + num_idx # 현재 index에 max index 더함
        answer += maximum
        index = temp
        length -= 1
    return answer