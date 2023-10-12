# 04. 가장 흔한 단어

[문제 링크] https://leetcode.com/problems/most-common-word/

### 문제
<p>금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.</p>

---

#### 예제 1
* 입력
```python
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit." 
banned = ["hit"]
```
* 출력
```
"ball"
```

---

#### 예제 2
* 입력
```python
paragraph = "a."
banned = []
```
* 출력
```
"a"
```