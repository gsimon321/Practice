# Defining a main method
def main():
  name = input('What is your name?')
  secondary_function(name)

def secondary_function(name):
  print(name , 'what is my age LOL')
  print(f'Very nice to meet you, {name.upper()}!')

if __name__ == '__main__':
  main()

# some arithemetic operations
x = 4
y = 3

# between two 
x + y  # returns 7
x - y  # returns 1
x * y  # returns 12
x ** y # returns 64
x / y  # returns 1.333, regular division
x // y # returns 1, round floor
x % y # returns 1

# self