
"inane comment to get rid of grayscale"

tyr = 1490
trp = 5500
cys = 125

aa = "MPPYTVVYFPVRGRCAALRMLLADQGQSWKEEVVTVETWQEGSLKASCLYGQLPKFQDGDLTLYQSNTILRHLGRTLGLYGKDQQEAALVDMVNDGVEDLRCKYISLIYTNYEAGKDDYVKALPGQLKPFETLLSQNQGGKTFIVGDQISFADYNLLDLLLIHEVLAPGCLDAFPLLSAYVGRLSARPKLKAFLASPEYVNLPINGNGKQ"

def CalcNoOfCys(aaseq):
    nCys = 0
    for char in aaseq:
        if char == "C":
            nCys += 1
    return nCys

def CalcTheoExtCoeff(aaseq):
    extcoeff = 0
    for char in aaseq:
        if char == "W":
            extcoeff += trp
        elif char == "Y":
            extcoeff += tyr
    return extcoeff

if(CalcNoOfCys(aa) % 2 == 0):
    excdoeff_Cis = str(CalcTheoExtCoeff(aa) + CalcNoOfCys(aa)/2 * cys)
elif(CalcNoOfCys(aa) % 2 == 1):
    excdoeff_Cis = str(CalcTheoExtCoeff(aa) + ((CalcNoOfCys(aa)-1)/2) * cys)

print("With Cystines: " + excdoeff_Cis +" M^-1.cm^-1")
print("Without Cystines: " + str(CalcTheoExtCoeff(aa)) + " M^-1.cm^-1")



class Car:

    def __init__(self,manufacturer, model, eng_disp, colour):
        self._manufacturer = manufacturer
        self._model = model
        self._engineDisp = eng_disp
        self._colour = colour

GavinsRealisticCar = Car("Mazda","2",1498,"Blue")
GavinsUnrealisticDreamCar = Car("Lamborghini","Aventador", 6498,"Green")

print(GavinsRealisticCar._manufacturer)

number = 1
print(number.__add__(1))



























