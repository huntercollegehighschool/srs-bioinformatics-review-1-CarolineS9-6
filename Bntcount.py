"""
Define a function ntcount that takes a string representing a DNA string. 

-First the function should check if it is a valid DNA strand (use the function defined in the 1st part). If it's not, return "error".

-If it is a valid DNA strand, the function returns a dictionary with the counts of each nucleotide.

For example: 
ntcount("AACTGTA") 
returns {"A": 3, "C": 1, "G": 1, "T": 2}
"""

def ntcount(dna):
  for x in dna: 
    if  x != "A" and x != "C" and x != "G" and x != "T":
      return("error")
    dicit = {}
    dna = dna.lower()
    for a in dna: 
      dicit.setdefault(a,0)
      dicit[a] = dicit[a] + 1 
    return dicit
  
