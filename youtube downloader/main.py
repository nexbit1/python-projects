from pytube import YouTube
#first run the certificate command stored in python application folder on MAC

#ask for the link from user
link = input("Enter the link of YouTube video you want to download:  ")
try:
    yt = YouTube(link)
except:
    print('link not found')
    exit()

#Showing details
print("Title: ",yt.title)
#Getting the highest resolution possible
highest_res = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...😇")
highest_res.download('/Users/omkarnagvekar/Downloads')
print("Download completed!!🥳")
