# Importing library
import qrcode

# Data to be encoded
data = 'https://www.youtube.com/watch?v=RsN0aXfPR1E'

# Encoding data using make() function
img = qrcode.make(data)

# Saving as an image file
img.save('image.png')
