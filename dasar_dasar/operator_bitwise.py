# operator bitwise
a = 9
b = 5
e = 0b11111111
d = 0b00001001
# Bitwise OR ( | )
c = a | b
print("\n========OR========")
print(f"nilai: {a}, binary: {format(a, '08b')}")
print(f"nilai: {b}, binary: {format(b, '08b')}")
print("------------------( | )")
print(f"nilai: {c}, binary: {format(c, '08b')}")

# Bitwise AND ( & )
c = a & b
print("\n========AND========")
print(f"nilai: {a}, binary: {format(a, '08b')}")
print(f"nilai: {b}, binary: {format(b, '08b')}")
print("------------------( & )")
print(f"nilai: {c}, binary: {format(c, '08b')}")

# Bitwise XOR ( ^ )
c = a ^ b
print("\n========XOR========")
print(f"nilai: {a}, binary: {format(a, '08b')}")
print(f"nilai: {b}, binary: {format(b, '08b')}")
print("------------------( ^ )")
print(f"nilai: {c}, binary: {format(c, '08b')}")

# Bitwise NOT ( ~ )
c = ~ a
print("\n========XOR========")
print(f"nilai: {a}, binary: {format(a, '08b')}")
print("------------------( ^ )")
print(f"nilai: {c}, binary: {format(c, '08b')}")
print("-------------------( ^ )")
print(f"nilai: {e^d}, binary: {format(e^d, '08b')}")

# shift right ( >> )
c = a >> 1
print("\n========SR========")
print(f"nilai: {a}, binary: {format(a, '08b')}")
print("------------------( >> )")
print(f"nilai: {c}, binary: {format(c, '08b')}")

# shift left ( << )
c = a << 1
print("\n========SR========")
print(f"nilai: {a}, binary: {format(a, '08b')}")
print("------------------( << )")
print(f"nilai: {c}, binary: {format(c, '08b')}")

