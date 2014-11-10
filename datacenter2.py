# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/python

#Starts here
datacenter_num = raw_input()
datacenter_num = int(datacenter_num)
datacenter_set = dict()
datacenter_list = []

#Check if first line input is valid
if 0 <= datacenter_num <= 999999:
    for i in xrange(datacenter_num):
        user_input = raw_input()
        if len(user_input) > 999:
            exit()
        else:
            datacenter_set[i] = user_input
else:
    exit()
    
#Check if Data set ids is valid
for i in xrange(datacenter_num):
    datacenter_set[i] = datacenter_set[i].split(" ")
    for j in xrange(len(datacenter_set[i])):
        if 0 <= int(datacenter_set[i][j]) <= 299:
            pass
        else:
            exit()

for i in xrange(datacenter_num):
    datacenter_set[i].pop(0)
    
new_datacenter_set = []

for i in xrange(datacenter_num):
    for j in xrange(len(datacenter_set[i])):
        new_datacenter_set.append(datacenter_set[i][j])

new_datacenter_set = list(set(new_datacenter_set))
new_datacenter_set.sort()
complete_data_set = {}

for i in xrange(len(new_datacenter_set)):
    for j in xrange(datacenter_num):
        if (new_datacenter_set[i] in datacenter_set[j]) and (new_datacenter_set[i] not in complete_data_set):
            complete_data_set[new_datacenter_set[i]] = j

for i in xrange(datacenter_num):
    for j in xrange(len(new_datacenter_set)):
        if new_datacenter_set[j] not in datacenter_set[i]:
            print new_datacenter_set[j], complete_data_set[new_datacenter_set[j]]+1, i+1
            
print "done"