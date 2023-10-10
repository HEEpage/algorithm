def isPalindrome(sentence) :
    strs = []
    for char in sentence :
        if char.isalnum() : # 해당 문자가 영문자 또는 숫자인지 판별
            strs.append(char.lower())
    
    # 팰린드롬 여부 판별
    while len(strs) > 1 :
        if strs.pop(0) != strs.pop() :
            return False
    
    return True