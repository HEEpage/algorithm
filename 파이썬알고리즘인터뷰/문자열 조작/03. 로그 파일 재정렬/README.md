# 03. 로그 파일 재정렬

[문제 링크] https://leetcode.com/problems/reorder-data-in-log-files/

### 문제
<p>로그를 재정렬하라. 기준은 다음과 같다.</p>

1. 로그의 가장 앞 부분은 식별자다.
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.

---

#### 예제 1
* 입력
```python
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
```
* 출력
```
["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
```

---

#### 예제 2
* 입력
```python
logs = ["a1 9 2 3 1"," g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
```
* 출력
```
["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]
```