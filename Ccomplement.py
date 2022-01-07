"""
Define a function reversecomplement that takes a DNA string as an input. 

-First the function should check if it is a valid DNA strand (use the function defined in the 1st part). If it's not, return "error".

-If it is a valid DNA string, the function finds the reverse complement of that string. The reverse complement is found by first reversing the string, then taking the complement of each nucleotide. A and T are complements of each other, and C and G are complements of each other.

For example,
reversecomplement("AAGCT") should return "AGCTT".
"""

def reversecomplement(dna):
  for x in dna: 
    if  x != "A" and x != "C" and x != "G" and x != "T":
      return("error")
  reverse = dna[::-1] 
  revcom
  for a in reverse:
    if a == "A":
      return "T"
    if a == "C":
      return "G"
    if a == "G":
     return "C"
    if a == "T":
      return "A"
  
