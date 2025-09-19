square_size = int(input("Enter the size of the pattern:"))
row = 0

while row < square:
  for i in range(square_size):
    print("*", end="")
  print()
  row += 1