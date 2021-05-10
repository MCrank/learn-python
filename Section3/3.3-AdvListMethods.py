# Sorting
# Inserting Elements
# List -> String

alpha1 = ["a","f","b","e","d"]
alpha2 = ["g","i","h"]
alpha3 = "jklmnopqrstuvwxyz"

alpha1.sort()
alpha2.sort()
print(alpha1)
print(alpha2)

alpha1.insert(2, "c")
print(alpha1)
print(alpha2)

alpha1 = ''.join(alpha1)
alpha2 = ''.join(alpha2)
print(alpha1)
print(alpha2)

alphabet = alpha1 + alpha2 + alpha3

print(alphabet)