def fibonacci():
  """
  This function generates the Fibonacci sequence as an infinite iterator.
  """
  x, y = 0, 1
  while True:
    yield x
    x, y = y, x + y

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence using a generator
fib_generator = fibonacci()

# Print the first n terms
for i in range(num_terms):
  print(next(fib_generator))