#1316 그룹 단어
result = 0
for _ in range(int(input())):
  word = input()
  if list(word) == sorted(word, key=word.find):
    result += 1
print(result)