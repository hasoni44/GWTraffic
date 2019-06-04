currentID = 0
idRows = []

for i in ID_FILE:
	currentID = i[0]
	idRows = []
	
	#2011 file1
	for a1 in y2011_1FILE:
		if a1[0] == currentID:
			idRows.append(a1)
	
	#2011 file2
	for a2 in y2011_2FILE:
		if a2[0] == currentID:
			idRows.append(a2)
			
	#2011 file3
	for a3 in y2011_3FILE:
		if a3[0] == currentID:
			idRows.append(a3)
	
	#2011 file4
	for a4 in y2011_4FILE:
		if a4[0] == currentID:
			idRows.append(a4)
			
	#2011 file5
	for a5 in y2011_5FILE:
		if a5[0] == currentID:
			idRows.append(a5)
			
	#2011 file6
	for a6 in y2011_6FILE:
		if a6[0] == currentID:
			idRows.append(a6)
			
	#2011 file7
	for a7 in y2011_7FILE:
		if a7[0] == currentID:
			idRows.append(a7)
			
	#2011 file8
	for a8 in y2011_8FILE:
		if a8[0] == currentID:
			idRows.append(a8)
			
	#2011 file9
	for a9 in y2011_9FILE:
		if a9[0] == currentID:
			idRows.append(a9)
			
	#2011 file10
	for a10 in y2011_10FILE:
		if a10[0] == currentID:
			idRows.append(a10)
			
	#2011 file11
	for a11 in y2011_11FILE:
		if a11[0] == currentID:
			idRows.append(a11)
			
	#2011 file12
	for a12 in y2011_12FILE:
		if a12[0] == currentID:
			idRows.append(a12)
			
	