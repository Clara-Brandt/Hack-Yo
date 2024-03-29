from flask import request, redirect, Flask, render_template
app = Flask(__name__, template_folder='templates')

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
        aminos = []
        for codon in c3:
            if (codon[0:1] == "U"):
                if (codon[1:2] == "U"):
                    if (codon[2:3] == "G" or codon[2:3] == "A"):
                           aminos.append("Leu")
                    else:
                        aminos.append("Phe")
                if (codon[1:2] == "C"):
                       aminos.append("Ser")
                if (codon[1:2] == "A"):
                    if (codon[2:3] == "A" or codon[2:3] == "G"):
                        break
                    else:
                        aminos.append("Tyr")
                if (codon[1:2] == "G"):
                    if (codon[2:3] == "G"):
                        aminos.append("Trp")
                    elif (codon[2:3] == "A"):
                        break
                    else:
                        aminos.append("Cys")

            if (codon[0:1] == "A"):
                if (codon[1:2] == "U"):
                    if (codon[2:3] == "G"):
                        aminos.append("Met")
                    else:
                        aminos.append("Ile")
                if (codon[1:2] == "C"):
                    aminos.append("Thr")
                if (codon[1:2] == "A"):
                    if (codon[2:3] == "A" or codon[2:3] == "G"):
                        aminos.append("Lys")
                    else:
                        aminos.append("Asn")
                if (codon[1:2] == "G"):
                    if (codon[2:3] == "A" or codon[2:3] == "G"):
                        aminos.append("Arg")
                    else:
                        aminos.append("Ser")
            if (codon[0:1] == "G"):
                if (codon[1:2] == "U"):
                    aminos.append("Val")
                    #everything that starts with GU
                    #is Val
                elif (codon[1:2] == "C"):
                    aminos.append("Ala")
                    #everything that starts with GC
                    #is Ala
                elif (codon[1:2] == "A"):
                    if (codon[2:3] == "U"):
                        aminos.append("Asp")
                    elif (codon[2:3] == "C"):
                        aminos.append("Asp")
                    else:
                        aminos.append("Glu")
                else:
                    aminos.append("Gly")
            if (codon[0:1] == "C"):
                if (codon[1:2] == "U"):
                    aminos.append("Leu")
                elif (codon[1:2] == "C"):
                    aminos.append("Pro")
                elif (codon[1:2] == "A"):
                    if (codon[2:3] == "U"):
                        aminos.append("His")
                    elif (codon[2:3] == "C"):
                        aminos.append("His")
                    else:
                        aminos.append("Gln")
                else:
                    aminos.append("Arg")

        result = amino

@app.route('/dataEntered', methods = ['POST'])
def dataEntered():
    userInput = request.form['input']
    # Probably call a function to do the calculations here
    displayResult()
    return redirect('/')

@app.route("/")
def displayResult():
    RESULT = "hi"
    # Replace RESULT with the actual result
    return render_template('index.html', result=RESULT)

if __name__ == '__main__':
    app.run(debug=True)
    main()
