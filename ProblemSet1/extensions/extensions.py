# Get user input
filename = input("File name: ")
# Remove spaces and make it all lower case
new_filename = filename.lower().strip()
# If gif or jpg or jpeg or png print "image/type"
if '.gif' in new_filename:
    print("image/gif")
elif '.jpg' in new_filename or '.jpeg' in new_filename:
    print ("image/jpeg")
elif '.png' in new_filename:
    print ("image/png")
# If pdf or zip, print "application/type"
elif '.pdf' in new_filename:
    print("application/pdf")
elif '.zip' in new_filename:
    print("application/zip")
# if txt, print "text/plain"
elif '.txt' in new_filename:
    print("text/plain")
# Otherwise, print "application/octet-stream"
else:
    print("application/octet-stream")


