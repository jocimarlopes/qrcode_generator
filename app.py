import qrcode
from datetime import datetime


def generate_qrcode_by_link(link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=0,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="grey", back_color="black")
    type(img)  # qrcode.image.pil.PilImage
    filename = 'qrcode_' + str(datetime.now().timestamp()) + '.png'
    img.save(filename)
    print('QR Code Salvo com Sucesso')

generate_qrcode_by_link('https://wa.me/5551980641036')