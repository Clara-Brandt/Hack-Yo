from flask import request, redirect, Flask, render_template
app = Flask(__name__, template_folder='templates')
global userInput
userInput = ""

def calculationFunction(UI):
    sequence = UI
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
    if total < 3 :
        return "Fewer than three letters"
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
        return ("There are " + str(invalidLetterCount) + " invalid letter(s)") #placeholder: it will send a message to the website

    elif (total % 3 != 0) or (total < 3):
            return ('sequence entered does not break evenly into codons with 3 nucleotides') #Placehoder

    elif codonList[0] != ["A","U","G"]:
        return ("Translation failed: no start codon") #placeholder

    elif (finalCodon != ["U","A","A"]) and (finalCodon != ["U","A","G"]) and (finalCodon != ["U","G","A"]):
        return ("Translation failed: no stop codon") #placeholder


    else:
        # Marlena and Isabel's for loop
        aminos = []
        for codon in codonList:
            if (codon[0] == "U"):
                if (codon[1] == "U"):
                    if (codon[2] == "G" or codon[2] == "A"):
                           aminos.append("Leucine")
                    else:
                        aminos.append("Phenylalanine")
                if (codon[1] == "C"):
                       aminos.append("Serine")
                if (codon[1] == "A"):
                    if (codon[2] == "A" or codon[2] == "G"):
                        break
                    else:
                        aminos.append("Tyrosine")
                if (codon[1] == "G"):
                    if (codon[2] == "G"):
                        aminos.append("Trptophan")
                    elif (codon[2] == "A"):
                        break
                    else:
                        aminos.append("Cysteine")

            if (codon[0] == "A"):
                if (codon[1] == "U"):
                    if (codon[2] == "G"):
                        aminos.append("Methionine")
                    else:
                        aminos.append("Isoleucine")
                if (codon[1] == "C"):
                    aminos.append("Threonine")
                if (codon[1] == "A"):
                    if (codon[2] == "A" or codon[2] == "G"):
                        aminos.append("Lysine")
                    else:
                        aminos.append("Asparagine")
                if (codon[1] == "G"):
                    if (codon[2] == "A" or codon[2] == "G"):
                        aminos.append("Arginine")
                    else:
                        aminos.append("Serine")
            if (codon[0] == "G"):
                if (codon[1] == "U"):
                    aminos.append("Valine")
                    #everything that starts with GU
                    #is Val
                elif (codon[1] == "C"):
                    aminos.append("Alanine")
                    #everything that starts with GC
                    #is Ala
                elif (codon[1] == "A"):
                    if (codon[2] == "U"):
                        aminos.append("Aspartic Acid")
                    elif (codon[2] == "C"):
                        aminos.append("Aspartic Acid")
                    else:
                        aminos.append("Glutamic acid")
                else:
                    aminos.append("Glycine")
            if (codon[0] == "C"):
                if (codon[1] == "U"):
                    aminos.append("Leucine")
                elif (codon[1] == "C"):
                    aminos.append("Proline")
                elif (codon[1] == "A"):
                    if (codon[2] == "U"):
                        aminos.append("Histidine")
                    elif (codon[2] == "C"):
                        aminos.append("Histidine")
                    else:
                        aminos.append("Glutamine")
                else:
                    aminos.append("Arginine")

        finalString = "Your amino acids are: "
        for index in range(len(aminos)):
            if index == (len(aminos)-1):
                finalString = finalString + str(aminos[index])
            else:
                finalString = finalString + str(aminos[index]) + ", "
        return (finalString)
        #give result to html thingy

@app.route('/dataEntered', methods = ['POST'])
def dataEntered():
    global userInput
    userInput = request.form['input']
    displayResult()
    return redirect('/')

@app.route("/")
def displayResult():
    global userInput
    RESULT = calculationFunction(userInput)
    return render_template('index.html', result=RESULT)

if __name__ == '__main__':
    app.run(debug=True)
