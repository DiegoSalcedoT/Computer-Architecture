from nand import NAND_gate
from not_gate import NOT_gate
from and_gate import AND_gate
from or_gate import OR_gate
from xor_gate import XOR_gate

def half_adder(a, b):
  return XOR_gate(a, b), AND_gate(a, b)

def full_adder(a, b, c):
  s1, c1 = half_adder(a, b)
  s2, c2 = half_adder(s1, c)
  c_out = OR_gate(c1, c2) # c_out = (a AND b) OR ((a XOR b) AND c)
  return(s2, c_out)

for f in (0,1):
  for s in (0,1):
    for t in (0,1):
      print(f, s, t, full_adder(f, s, t))

def ALU(a, b, c, opcode):
  if opcode == "00":
    return half_adder(a, b)
  elif opcode == "01":
    return full_adder(a, b, c)
  elif opcode == "10":
    return full_adder(a, b, 1)

for opc in ("00", "01", "10"):
  print("")
  for f in (0,1): 
    for s in (0,1):
      for t in (0,1):
        print(opc, f, s, t, ALU(f, s, t, opc))



