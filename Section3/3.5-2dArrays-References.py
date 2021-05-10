from pprint import pprint as pretty_print
from copy import copy, deepcopy

nums_2d = [
  [1,2,3,4,5,6,7],
  [8,9,10,11,12,13,14,15],
  [16,17,18,19,20,21,22]
]

# Grab number 11
print(nums_2d[1][3])

print(nums_2d)
pretty_print(nums_2d)

nums_2d[2][1] = -5
pretty_print(nums_2d)

letters = ["A","B","C","D","E"]
letters_2d = [letters, letters, letters]
pretty_print(letters_2d)
letters_2d[0][0] = 'F' # All As are converted to F because line 20 is a reference
pretty_print(letters_2d)

letters2 = ["A","B","C","D","E"]
letters_2d_copy = [copy(letters2), copy(letters2), copy(letters2)]
letters_2d_copy[0][0] = 'Z'
pretty_print(letters_2d_copy)
