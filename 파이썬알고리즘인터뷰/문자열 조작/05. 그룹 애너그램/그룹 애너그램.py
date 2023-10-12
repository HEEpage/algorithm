import collections

def groupAnagrams(strs) :
    anamgrans = collections.defaultdict(list)

    for word in strs :
        # 정렬하여 딕셔너리에 추가
        anamgrans[''.join(sorted(word))].append(word)
    
    return list(anamgrans.values())