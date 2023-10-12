# 05. 그룹 애너그램

[문제 링크] https://leetcode.com/problems/group-anagrams/

### 문제
<p>문자열 배열을 받아 애너그램 단위로 그룹핑하라.</p>

---

#### 예제 1
* 입력
```python
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
```
* 출력
```
[
  ["ate", "eat", "tea"],
  ["nat", "tan"],
  ["bat"]
]
```

---

#### 예제 2
* 입력
```python
strs = [""]
```
* 출력
```
[[""]]
```

---

#### 예제 3
* 입력
```python
strs = ["a"]
```
* 출력
```
[["a"]]
```

---

<details>
<summary> <u>애너그램</u>이란? 🤔 </summary>
문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것
</details>