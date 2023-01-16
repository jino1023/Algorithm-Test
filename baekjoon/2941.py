#2941번 크로아티아 알파벳 갯수 세기
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
x = input()
for i in cro:
  #cro문자열이 x에 있으면 @으로 변환
  x = x.replace(i, '@')
print(len(x))