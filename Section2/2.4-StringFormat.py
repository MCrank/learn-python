n = 11
f = 1.2345678
s = "computer"

print("my number is {:d}".format(n))
print("my number is {:b}".format(n))


print("{:f}".format(f))
print("{:.3f}".format(f))  # Only 3 points of precision
print("{:11.3f}".format(f))  # Padding to make 11 characters
# Padding to make 11 characters but fill with zeros
print("{:011.3f}".format(f))

print("{0} {1} {2}".format(n, f, s))
print("{name} owns(s) {amount} of {object}".format(
    name="Marco",
    amount=5,
    object="mangoes"
))
