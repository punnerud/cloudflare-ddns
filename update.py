import requests,re
response = requests.get('http://ifconfig.co/ip')
filnavn = 'last-ip.txt'
f = open(filnavn,'a+')
f = open(filnavn,'r+')
reip = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",response.text)[0]
try:
	try:
		ip = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",f.read())[0]
	except:
		print("No IP in file, updating Cloudflare")
		f.close()
		f = open(filnavn,'w+')
		f.write(reip)
		f.close()
		headers = {'Authorization': 'Bearer b-123123123','Content-Type': 'application/json'}
		data = '{"type":"A","name":"example.com","content":"'+str(reip)+'","ttl":1,"proxied":false}'
		response = requests.put('https://api.cloudflare.com/client/v4/zones/123123123/dns_records/123123123', headers=headers, data=data)
		exit()
	if reip != ip:
		print("Changed IP, updating Cloudflare")
		f.close()
		f = open(filnavn,'w+')
		f.write(reip)
		f.close()
		headers = {'Authorization': 'Bearer b-123123123','Content-Type': 'application/json'}
		data = '{"type":"A","name":"example.com","content":"'+str(reip)+'","ttl":1,"proxied":false}'
		response = requests.put('https://api.cloudflare.com/client/v4/zones/123123123/dns_records/123123123', headers=headers, data=data)
		exit()
	else:
		print("Same IP, no change")
		pass
except:
	pass
