from datetime import datetime
import sys
import os

domain = "example.com"
new_dns_filename = "new_dns_file"
dns_db_file = "/home/test-dns-db"
new_dns_file = os.path.join(os.path.dirname(dns_db_file),new_dns_filename)

if not os.path.exists(dns_db_file):
	print "DNS db file not found"
	exit(0)

ip = sys.argv[1]
username = sys.argv[2]

toupdate = ip.split(".")[-1]
octets = ip.split(".")
octets.reverse()
rev_ip_str = ".".join(octets)
rev_ip_ptr = username+"-"+rev_ip_str+"."+domain+"."

f = open(dns_db_file,'r')
content = f.readlines()
cur_serial = content[2].strip().split(";")[0].strip()
if cur_serial == datetime.strftime(datetime.now(),"%Y%m%d00"):
	updated_serial = str(int(cur_serial)+1)
else:
	updated_serial = datetime.strftime(datetime.now(),"%Y%m%d00")

updated_text = ""
updated_text += "".join(content[0:2])
updated_text += content[2].replace(cur_serial,updated_serial)
nummatch = False
continuechecking = True
for line in content[3:]:
	ipnum = line.split(" ")[0].strip()
	if ipnum == toupdate and continuechecking:
		nummatch = True
		continuechecking = False
		# replaceRecord(toupdate)
		updated_text += "%s\t\tIN\tPTR\t\t%s\n" %(toupdate, rev_ip_ptr)
		continue
	if (not nummatch) and continuechecking:
		try:
			intipnum = int(ipnum)
			inttoupdate = int(toupdate)
			if intipnum > inttoupdate:
				print "greater value exceeded"
				continuechecking = False
				updated_text += "%s\t\tIN\t\t%s\n" %(toupdate, rev_ip_ptr)
		except:
			pass
	updated_text += line

q = open(new_dns_file,'a')
q.write(updated_text)
q.close()

if os.path.exists(dns_db_file):
	os.path.remove(dns_db_file)
	os.path.rename(new_dns_file, dns_db_file)
