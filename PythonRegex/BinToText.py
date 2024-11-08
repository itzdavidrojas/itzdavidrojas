text1 = input()
Bin_set = bin(int.from_bytes(text1.encode(), 'big'))

print(Bin_set)