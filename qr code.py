import qrcode
input_data = "https://unsplash.com/photos/green-trees-with-sun-rays-Otl-rfJEexo" #define the input data,copy the link to thr variable
qr = qrcode.QRCode(version=1,box_size=8,border=4)  #define qrcode parameters
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill_color='black',back_color='white')
img.save('nature.png')
print("QR codegenerated and saved as 'nature'")
