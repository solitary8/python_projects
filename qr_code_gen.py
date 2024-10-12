import qrcode 

data = 'hello'

img = qrcode.make(data)

img.save('/home/codespace/test.png')