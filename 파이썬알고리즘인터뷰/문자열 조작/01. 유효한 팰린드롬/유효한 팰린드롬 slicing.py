import re

def isPalindrome(sentence) :
    sentence = sentence.lower()

    # 정규식으로 불필요한 문자 필터링
    sentence = re.sub('[^a-z0-9]', '', sentence)

    return sentence == sentence[::-1] # 슬라이싱