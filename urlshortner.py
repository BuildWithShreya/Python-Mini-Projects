import pyshorteners

url=input('Enter URL  :\n')
print("URL After shortening : ",pyshorteners.Shortener().tinyurl.short(url))
