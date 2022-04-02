import datetime as dt

class InvalidInput(Exception):
    pass

def inputValidation(line):
    argsArr = line.split()
    if len(argsArr) == 5:
        try:
            if argsArr[0][0].isupper() and argsArr[0][1].isupper() and argsArr[0][2:6].isnumeric() and argsArr[1] in ['S','C'] and argsArr[2].isnumeric() and len(argsArr[3]) == 5 and len(argsArr[4]) == 5 :
                startTimeArr = argsArr[3].split(":")
                endTimeArr = argsArr[4].split(":")

                for nb in startTimeArr + endTimeArr:
                    if len(nb) != 2: raise InvalidInput

                if int(startTimeArr[0]) >= 0 and int(startTimeArr[0]) <= 23 and int(startTimeArr[1]) >= 0 and int(startTimeArr[1]) <= 59 and int(endTimeArr[0]) >= 0 and int(endTimeArr[0]) <= 23 and int(endTimeArr[1]) >= 0 and int(endTimeArr[1]) <= 59:
                    return argsArr
        except:
            raise InvalidInput

    raise InvalidInput

def calculateVelocity(startTime, endTime, distance):
    startTimeArr = startTime.split(":")
    endTimeArr = endTime.split(":")
    sTime = dt.datetime(2022,12,1,int(startTimeArr[0]), int(startTimeArr[1]),00)
    eTime = dt.datetime(2022, 12,1 if endTimeArr[0] >= startTimeArr[0] else 2, int(endTimeArr[0]), int(endTimeArr[1]), 00)
    velocity = (int(distance)/(eTime-sTime).total_seconds())*3600/1000
    return round(velocity,2)

def main():
    try:
        while True:
            line = input()
            try:
                argsArr = inputValidation(line)
                if argsArr:
                    data = dict()
                    data["regNumber"] = argsArr[0]
                    data["vehicleType"] = argsArr[1]
                    data["distance"] = argsArr[2]
                    data["startTime"] = argsArr[3]
                    data["endTime"] = argsArr[4]

                    maxVel = 120 if data["vehicleType"] == "S" else 80
                    finalVel = calculateVelocity(data["startTime"], data["endTime"], data["distance"])

                    ticketString = "M" if finalVel > maxVel else "."

                    print(f'{data["regNumber"]} {ticketString} { "%.2f"%finalVel }')

                else:
                    raise InvalidInput

            except InvalidInput:
                print("BLAD")

    except EOFError:
        pass

if __name__ == '__main__':
    main()

