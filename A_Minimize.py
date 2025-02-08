n = int(input())


for i in range(n):
  r, l = map(int, input().split())
  minn = 100
  for num in range(r, l + 1):
    minn = min(minn, (num - r) + (l - num))
    
  print(minn)