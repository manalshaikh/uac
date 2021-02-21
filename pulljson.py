import urllib.request

with urllib.request.urlopen("https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true") as url:
    s = url.read()
    fileopen = open("data.json", 'wb')
    fileopen.write(s)
    fileopen.close()
    print("Successfully downloaded")