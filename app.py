int fizz = 3
int buzz = 5
for n in range(1,100):
  if n % fizz == 0:
    if n % buzz == 0:
      print("FizzBuzz")
    else:
      print("Fizz")
  elif n % buzz == 0:
    print("Buzz")
  else:
    print(n)
