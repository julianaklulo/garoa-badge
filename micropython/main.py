from framebuf import FrameBuffer, MONO_HLSB
from machine import Pin, I2C
from time import sleep

import sh1106


btn_up = Pin(12, Pin.IN, Pin.PULL_UP)
btn_down = Pin(13, Pin.IN, Pin.PULL_UP)
btn_prog = Pin(0, Pin.IN, Pin.PULL_UP)

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
display = sh1106.SH1106_I2C(128, 64, i2c, Pin(16), 0x3c)
display.flip()


def read_pbm_image(filename, invert=False):
    from framebuf import FrameBuffer, MONO_HLSB

    with open(filename, "rb") as f:
        if f.readline().strip() != b"P4":
            raise ValueError("Not a binary PBM (P4) file")
        while True:
            line = f.readline().strip()
            if not line.startswith(b"#"):
                width, height = map(int, line.split())
                break
        data = bytearray(f.read())

    if not invert:
        for i in range(len(data)):
         data[i] ^= 0xFF

    return FrameBuffer(data, width, height, MONO_HLSB)
    return fb


def show_image(display, fb, x_offset=0, y_offset=0):
    display.fill(0)
    display.blit(fb, x_offset, y_offset)
    display.show()


def show_word(display, handle, x_offset=0, y_offset=0):
    display.fill(0)
    display.text(handle, x_offset, y_offset)
    display.show()


def show_phrase(display, phrase, x_offset=0, y_offset=0):
    display.fill(0)
    words = phrase.split()

    for word in words:
        display.text(word, x_offset, y_offset)
        y_offset += 10

    display.show()

def qrcode():
    image = read_pbm_image("qr-code.pbm")
    show_image(display, image, x_offset=32)


def handle():
    handle = "@julianaklulo"
    show_word(display, handle, x_offset=10, y_offset=28)


def name():
    name = "Juliana Karoline de Sousa"
    show_phrase(display, name, y_offset=16)


name()
while True:
    if not btn_up.value():
        handle()
    if not btn_down.value():
        qrcode()
    if not btn_prog.value():
        name()

    sleep(0.5)
