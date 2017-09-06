import csv


def read_file(fobj):
    data = {}
    for line in csv.reader(fobj):
        data[line[0]] = line[1:]
    return data

with open('Issues_by_Month_Not_Customer_Reported.csv') as f1, open('Issues_by_Month_Customer_Reported.csv') as f2:
    data1 = read_file(f1)
    data2 = read_file(f2)

with open('Issues_by_Month.csv') as result:
    wtr = csv.writer(result)
    for key in data1.keys():
        try:
            wtr.writerow((key, data1[key][2], data1[key][3], data2[key][0]))
        except KeyError:
            pass




