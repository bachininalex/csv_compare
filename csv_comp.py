
import csv

#def report_csv():
with open('known_issues.csv', 'r') as t1, open('new_report.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

def get_update(file_1, file_2):
    global tc_list, tc_count
    tc_list = []
    with open('unknown_issues.csv', 'w') as outFile:
        for line in filetwo:
            if line not in fileone:
                tc_list.append(line)
                outFile.write(line)
    tc_count =  len(tc_list)
    #print('[%s]' % ', '.join(map(str, tc_list)))
    #print("[{0}]".format(', '.join(map(str, tc_count))))
    #print str(tc_count).translate(None, "'")

#def get_nice_string(list):
    #return "[" + ", ".join( str(x) for x in list) + "]"
    SYMBOLS = '{}()[].,:;+*/&|<>=~$\n'
    results = []
    for element in tc_list:
        temp = ''
        for ch in element:
            if ch not in SYMBOLS:
                temp += ch
        results.append(temp)
    print(' '.join(map(str, results)))



get_update(fileone, filetwo)
#get_nice_string(tc_list)

#print(get_nice_string(tc_list))
print("Number of TCs:", tc_count)
