# 숫자 문자열과 영단어
# https://school.programmers.co.kr/learn/courses/30/lessons/81301
def solution(s):
  words = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine"
  ]
  n = len(s)
  result = ""
  i = 0
  # s의 모든 문자를 반복
  while i < n:
    j = i
    # 숫자가 나올때까지 j증가
    while j < n and s[j].isdigit():
      j += 1
    if j > i:
      # 결과에 숫자 추가
      result += s[i:j]
      i = j
    else:
      # 숫자가 아니면, words 배열 반복
      for word in words:
        # 이 words 배열에 있는 단어와 같으면
        if s[i:i + len(word)] == word:
          # 결과에 words 배열에서의 인덱스를 추가
          result += str(words.index(word))
          i += len(word)
          break
  return int(result)
