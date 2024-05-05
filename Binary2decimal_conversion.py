def binary_2_dec(bin_num):
  bin_num = str(bin_num)
  dec_num = 0
  pos = len(bin_num)
  for digit in bin_num:
    pos -= 1
    dec_num += 2 ** pos * int(digit)
    print(pos)
  return dec_num

binary = 100110
decimal_conversion1 = binary_2_dec(binary)
print("\n" + str(decimal_conversion1))
