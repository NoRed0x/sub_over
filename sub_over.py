#!/usr/bin/env python
import os
import dns.resolver
import optparse
import subprocess
from termcolor import colored 


print("""
		#######################################################
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
		#              SubDomain TakeOver                     #
		#              Coder: karim habeeb                    #
		#              twitter.com/Nored0x                    #
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
		#######################################################  
	""")  


print(colored("\n-----------------------------------", 'green', attrs=['bold']))
print(colored("[+] Start collecting Resolved CNAME", 'red', attrs=['bold']))
print(colored("-----------------------------------", 'green', attrs=['bold']))

def get_arguments():
	parser=optparse.OptionParser()
	parser.add_option("-d","--sub",dest="subdomain_list",help="list of subdomain")
	(options,arguments)=parser.parse_args()
	if not options.subdomain_list:
		print("[-] Subdomain list not found")
		exit()
	return options

options=get_arguments()
subdomains=options.subdomain_list


wordlist=open(subdomains,'r')
cname_url='cname_url'
cname_list='cname_list'

list_of_cname=[]
for subdomain in wordlist:

	subdomain=subdomain.strip()
	try:		
		result=dns.resolver.query(subdomain,'CNAME') #if not found dns recored >not error
		if result.rrset is not None : #DNS Record Set  is a group of records with the same record type, for example all DNS A records are one RRset
			#print(result.rrset)
			list_of_cname.append(result.rrset)
						

	except :
		print("[-] "+subdomain +" has no cname ")
		pass		

for cname in list_of_cname:
	print("[+] cname :"+str(cname))
	cnames=open('cname_list','a')
	cnames.write(str(cname))
	cnames.write("\n")
	cnames.close()

subprocess.call("cat "+cname_list +'| cut -d " " -f 1 | httpx -follow-redirects -silent >'+cname_url,shell=True)
subprocess.call("rm "+cname_list,shell=True)
subprocess.call("eyewitness -f "+cname_url+" --no-prompt ",shell=True)
