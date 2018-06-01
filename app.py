fizz = 3
buzz = 5
upto = 100
for n in range(1,(upto + 1)):
  if n % fizz == 0:
    if n % buzz == 0:
      print("FizzBuzz")
    else:
      print("Fizz")
  elif n % buzz == 0:
    print("Buzz")
  else:
    print(n)
