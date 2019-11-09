def main():
    sequence = input("Please enter your DNA sequence: ")
    sequence = sequence.upper()
    total = 0
    sequenceList = []
    invalidLetter = False
    invalidLetterCount = 0

    #Makes a list of the letters and finds the total number of nucleotides.
    for letter in sequence:
        if (letter != "A") and (letter != "U") and (letter != "C") and (letter != "G"):
            invalidLetter = True
            invalidLetterCount += 1
        sequenceList += [letter]
        total += 1

    #Makes the list of all the codons
    codonCount = int(total/3)
    codonList = []
    start = 0
    for codonNum in range(codonCount):
        codon = sequenceList[start:(start+3)]
        codonList = codonList + [codon]
        start += 3

    #tests whether starting and ending codons are present
    finalCodon = codonList[codonCount-1]

    if invalidLetter == True:
        print("There are", invalidLetterCount, "invalid letter(s)") #placeholder: it will send a message to the website

    elif total % 3 != 0:
            print('sequence entered does not break evenly into codons with 3 nucleotides') #Placehoder

    elif codonList[0] != ["A","U","G"]:
        print("Translation failed: no start codon") #placeholder

    elif (finalCodon != ["U","A","A"]) and (finalCodon != ["U","A","G"]) and (finalCodon != ["U","G","A"]):
        print("Translation failed: no stop codon") #placeholder


    else:
        # Marlena and Isabel's for loop
        print(codonList)


if __name__ == '__main__':
    main()
