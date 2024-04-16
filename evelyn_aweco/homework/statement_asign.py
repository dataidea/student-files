
#what is meant by break statement

# The break statement is used to exit or "break out" of the innermost enclosing loop
# (for loop, while loop, or nested loops). When the break statement is encountered within
# a loop, the loop immediately terminates, and program execution resumes at the next 
#statement after the loop.


# examples
# numbers = (1,2,3,4,5,6,7,8,9,10)
# for num in numbers:
# 	if num == 5:
		
# 	 break


DNA_sequence = "ACTGACTGACTCGTTAATTAATTAACCGT"
for TATA_BOX in DNA_sequence:
    if TATA_BOX == "T" and DNA_sequence[DNA_sequence.index(TATA_BOX):DNA_sequence.index(TATA_BOX) + 6] == "TTAATT":
         break
