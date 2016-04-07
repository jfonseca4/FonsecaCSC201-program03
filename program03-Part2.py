#Jordan Fonseca

#3.1

DNA = input(str("Enter the first DNA sequence")) #Asks user to input 2 DNA strings
DNA2 = input(str("Enter the second DNA sequence"))

NumMatches = sum(a==b for a, b in zip(DNA, DNA2))
#sum of the number of times DNA and DNA2 match

print(NumMatches)  #prints the number of matches

#I was not able to figure out 3.2 or 3.4
