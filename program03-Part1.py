#Jordan Fonseca

#2.1


DNA = input(str("Enter the DNA sequence"))   #asks user to input a string

DNA2 = []   
for i in DNA:    
    if i == "A":          #if DNA is A, replaces it with a T
        DNA2.append("T") 
    if i == 'G':         #if DNA is G, replaces it with a C
        DNA2.append("C")
    if i == "C":          #if DNA is C, replaces it with a G
        DNA2.append("G")
    if i == "T":            #if DNA is T, replaces it with a A
        DNA2.append("A")

MirrorDNA = "".join(DNA2) #brings string together        
print(MirrorDNA)         #prints list mirrored DNA sequence

#2.2

DNA = input(str("Enter the DNA sequence")) #Asks user to enter DNA string

ReverseDNA = DNA[::-1] #reverses the entered DNA string

print(ReverseDNA) #prints reverse DNA string 


#2.3

validDNA = "TGCA"  #set valid DNA

DNA = input(str("Enter DNA sequence"))

if all(i in validDNA for i in DNA) == True : #If what the user enters for DNA is true
    print("valid")  #prints valid
else:           
    print("invalid") #If not true, prints invalid

#2.4

#I was not able to figure out how to put it all together, it would not work. 


