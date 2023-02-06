# Importing library
import qrcode

# Data to be encoded
data = 'https://t.me/school_255_bot'

# Encoding data using make() function
img = qrcode.make(data)

# Saving as an image file
img.save('MY_QR.jpg')
