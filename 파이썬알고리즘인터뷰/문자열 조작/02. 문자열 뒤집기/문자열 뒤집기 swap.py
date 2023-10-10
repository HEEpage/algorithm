def reverseString(word) :
    left, right = 0, len(word) - 1

    while left < right :
        word[left], word[right] = word[right], word[left]
        left += 1
        right -= 1