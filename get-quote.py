import random
def orig():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 47
  rnd = random.randint(0, last)
  print(quotes[rnd])
  print(quotes[rnd+1],end='n')

if __name__== "__main__":
  orig()
