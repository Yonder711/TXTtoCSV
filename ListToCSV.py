# ListToCSV.py
# name of your file to open and process, it is assumed to be in the same folder as the script
filename = ".\StatusResults.txt"

# Create the list to hold the new row
rows = []

# Open the file in read mode, the encoding removed teh first line with UTF encoding characters
with open(filename, "r", encoding='utf-8-sig') as f:
    # The for loop will step through each line in the file
    for line in f.readlines():
        if "Running IP" in line: # 
            #print("Line:")
            #print(line)
            values = line.strip("\n").strip()  # Strip the line feed and remove extra spaces
            #print("Values:")
            #print(values)
            # If It is the first line add a carrier return
            rows.append("\n")
            rows.append(values)
        else:
            #print("Line:")
            #print(line)
            values = line.strip("\n").strip()  # Strip the line feed and remove extra spaces
            #print("Values:")
            #print(values)
            rows.append(",")
            rows.append(values)

print(rows)   

with open("StatusResults-Out.csv", "w") as f:
    for row in rows:
        f.write(row)
        if rows != len(rows)-1:
            #f.write(",")
            pass
        else:
            f.write("\n")
