DEBUG = 0 

print(" ------------ GBA Binary rom decoder ------------ ")
print("           -  developed by viCppDev -  ")
print("+ https://github.com/viCppDev/GBA-binary-decoder +\n")

fileName = input("File GBA rom name: ")
f=open(fileName, 'rb')
fileContents = f.read()

f = open(fileName[:-4]+".txt", "a")

bytes = 0
outString = " "*8+"| "

for bytes in range (0,16):
    outString += "0x{0:0{1}X}".format(bytes,2)+"|"

if DEBUG == 1:
    print(outString)
    print("_"*89)

f.write(outString + "\n")
f.write("_"*89 + "\n")

bytes = 0
outString = "0x{0:0{1}X}".format(bytes,6) + "| "

for b in fileContents:
    bytes = bytes + 1


    if bytes % 2 == 0:
        endchar = " "
    else:
        endchar = ""

    
    outString += ("{0:0{1}X}".format(b,2) + endchar)

    if bytes % 32 == 0:

        if DEBUG == 1:
            print(outString)
        f.write(outString)
        f.write("\n")

        outString = ""
        outString += "0x{0:0{1}X}".format((bytes>>1),6) + "| "



f.close()
print("Decode! (output file: "+fileName[:-4]+".txt"+")")