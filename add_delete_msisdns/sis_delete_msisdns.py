import datetime
from MSISDN import Msisdn

file_in='Recycled_numbers_01.txt'
shift_time=30

# Read the MSISDN list from file
try:
    with open(file_in) as fin:
        msisdns=[]
        for line in fin:
            n=Msisdn(line[:-1])
            msisdns.append(n)
except FileNotFoundError as e:
    msisdns=""

#current time stamp
ts = (datetime.datetime.now()+datetime.timedelta(minutes=shift_time)).strftime("%Y%m%d%H%M%S")

# Generate the output file name
out_file="userinfo" + str(ts) + "10001.txt"

# Initailze the output file header 
nu= str(len(msisdns))
head="0001|00000|{0}|001|000|{1}{2}| |0{3}".format(ts,("0" * (10-len(nu) ) ), nu,"\n")
with open(out_file, "a") as f:
    print("{0}".format(head),file=f)
    #print("{0}".format("\n"),file=f)

# Write the MSISDNs del records to output file
with open(out_file, "a") as f:
    for i,n in enumerate(msisdns):
        idx=i+1
        #rec=
        record= "{0}{1}".format(idx,n.get_del_record())
        print(record, file=f)