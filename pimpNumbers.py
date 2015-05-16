f = open("HaltestellenVVS_simplified_utf8.csv", "r")
r = open("HaltestellenVVS_simplified_utf8_stationID.csv", "w")

r.write(f.readline())
lines = f.readlines()

for line in lines:
	stationID = line.split(",")[0]
	
	newStationID = int(stationID)+5000000
	outLine = str(newStationID) + line[len(stationID):]
	r.write(outLine)

r.close()
f.close()
