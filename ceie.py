import csv
#"2016data.csv"

#1/1/2016 10:00

#1/1/2016 9:00

#1/12/2016 

#12/1/2016

#12/12/2016

#[9:]
#[10:]
#[11:]

data2016 = open("2016data.csv",'r').read().splitlines()
data2016 = [i.split(",") for i in data2016]

peakhours = []

for j in data2016:
	if j[3][3:] == "/2016 7:00":
		peakhours.append(j)
	if j[3][3:] == "/2016 8:00":
		peakhours.append(j)
	if j[3][3:] == "/2016 9:00":
		peakhours.append(j)
	if j[3][3:] == "/2016 10:00":
		peakhours.append(j)
		

	if j[3][4:] == "/2016 7:00":
		peakhours.append(j)
	if j[3][4:] == "/2016 8:00":
		peakhours.append(j)
	if j[3][4:] == "/2016 9:00":
		peakhours.append(j)
	if j[3][4:] == "/2016 10:00":
		peakhours.append(j)
		

	if j[3][5:] == "/2016 7:00":
		peakhours.append(j)
	if j[3][5:] == "/2016 8:00":
		peakhours.append(j)
	if j[3][5:] == "/2016 9:00":
		peakhours.append(j)
	if j[3][5:] == "/2016 10:00":
		peakhours.append(j)
		
with open("peakhours2016.csv","w+") as f:
	writer = csv.writer(f,delimiter=",")
	writer.writerows(peakhours)

