from PIL import Image
import qrcode


def generate_qrcode(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
        border=1,
    )
    qr.add_data(url)
    qr.make(fit=True)

    return qr


def generate_pbm_from_qr(qr, filename, x, y):
    img = qr.make_image(fill_color="black", back_color="white").convert("1")
    img = img.resize((x, y), Image.NEAREST)
    img.save(filename)


url = "https://www.julianaklulo.dev"
filename = "qr-code.pbm"

qr = generate_qrcode(url)
generate_pbm_from_qr(qr, filename, 64, 64)

