import qrcode
from PIL import Image


class Qrcode:
    def __init__(self, data, box_size=10, fill_color="red", background_color="white"):
        self.data = data
        self.version = 1
        self.error_correction = qrcode.constants.ERROR_CORRECT_L
        self.box_size = box_size
        self.border = 4
        self.fill_color = fill_color
        self.background_color = background_color

    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=self.version,
            error_correction=self.error_correction,
            box_size=self.box_size,
            border=self.border
        )
        qr.add_data(self.data)
        qr.make(fit=True)
        image = qr.make_image(fill_color=self.fill_color, back_color=self.background_color)
        image.save(f'{self.data}.png')

#examples
qrcode1 = Qrcode(data='salut', box_size=8)
qrcode2 = Qrcode(data='cava', box_size=8, fill_color='black')


qrcode1.generate_qr_code()
qrcode2.generate_qr_code()
