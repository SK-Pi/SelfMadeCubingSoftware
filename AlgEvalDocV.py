def getData(fileName):
    # read file
    rawData = []
    file = open(fileName, "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        line = line.strip()
        rawData.append(line)

    res = []

    for lst in rawData:
        if len(lst.split(" ")) > 3:
            res.append(lst.split(" "))

    for i in res:
        i.pop(-1)

    return res, fileName

def checkAlg(dataAndFileName):
    data, fileName = dataAndFileName

    R = "R"
    RP = "R'"
    R2 = "R2"
    U = "U"
    UP = "U'"
    U2 = "U2"

    tempData = data

    newFile = "RES"+fileName
    resFile = open(newFile, "w+")

    for alg in tempData:
        trackR = 1
        trackU = 2
        algBad = False

        for i in alg:
            # Scans through an alg:
            if i == U:
                trackU += 1
            elif i == UP:
                trackU -= 1
            elif i == U2:
                if trackU == 0:
                    trackU += 2
                elif trackU == 2:
                    trackU -= 2
                else:
                    trackU = 3.14

            if trackU > 2:
                algBad = True
            elif trackU < 0:
                algBad = True

            if i == R:
                trackR += 1
            elif i == RP:
                trackR -= 1
            elif i == R2:
                if trackR == 0:
                    trackR += 2
                elif trackR == 2:
                    trackR -= 2
                else:
                    trackR = 3.14
            if trackR > 2:
                algBad = True
            elif trackR < 0:
                algBad = True

        if algBad != True:
            resAlg = ""
            for char in alg:
                resAlg += char + " "
            resAlg += "\n"
            resFile.write(resAlg)

    resFile.close()

textFile = str(input("What is the name of the file located in this directory which contains <RU> gen algs"
                     " created by Cube Explorer you want to evaluate?: "))

checkAlg(getData(textFile+".txt"))
