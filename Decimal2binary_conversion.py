def dec_2_bin(decimal_num):
  binary_num = ''
  while decimal_num > 0:
    binary_num = str(decimal_num % 2) + binary_num
    decimal_num = decimal_num // 2
  return int(binary_num)

final_binary_number = dec_2_bin(number_to_convert)
print(final_binary_number)
