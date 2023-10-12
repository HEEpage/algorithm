def longestPalindrom(strs) :
    # 팰린드롬 판별 및 투 포인터 확장
    def expand(left, right) :
        while left >= 0 and right < len(strs) and strs[left] == strs[right] :
            left -= 1
            right += 1
        
        return strs[left + 1 : right]
    
    # 해당 사항이 없을 때 빠르게 리턴
    if len(strs) < 2 or strs == strs[::-1] :
        return strs
    
    # 슬라이딩 윈도우 우측으로 이동
    result = ''
    for i in range(len(strs) - 1) :
        result = max(result, expand(i, i + 1), expand(i, i + 2), key = len)
    
    return result