#reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#performs on first two elements and repeats 
# reduce(function,iterables)
import functools #built in tools that gives u tools to work with function

letters = ["H","E","L","L","O"]

word = functools.reduce(lambda x,y: x+y, letters)
print(word)

#basically H+E add to become HE, then HE+L add to become HEL and so on

factorial = [24,3,2,1]
result = functools.reduce(lambda x,y, : x* y, factorial)
print(result)




