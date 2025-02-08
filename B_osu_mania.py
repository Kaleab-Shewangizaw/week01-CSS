n = int(input())

for _ in range(n):
  m = int(input())
  res = []
  for _ in range(m):
    beat = input()
    for dd in range(4):
      if beat[dd] == "#":
        res.append(dd+1)
  res = " ".join(map(str, res[::-1]))
  print(res)