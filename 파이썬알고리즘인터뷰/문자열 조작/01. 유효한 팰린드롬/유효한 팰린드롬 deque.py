import collections

def isPalindrome(sentence) :
    # 자료형 deque로 선언
    strs = collections.deque()

    for char in sentence :
        if char.isalnum() :
            strs.append(char.lower())
    
    while len(strs) > 1 :
        if strs.popleft() != strs.pop() :
            return False
    
    return True