import httpx

with open("proxy.txt", 'w') as file:
	file.write(httpx.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all").text)
