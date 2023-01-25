#10250
T = int(input())
for _ in range(T):
  #H=호텔의 층 수, W=각 층의 방 수, N=몇 번째 손님 인지
  H, W, N = map(int, input().split())
  #각층의 방 번호
  n = N // H + 1
  #객실의 층
  h = N % H
  if N % H == 0:
    n = N // H
    h = H
  print(f"{h*100+n}")