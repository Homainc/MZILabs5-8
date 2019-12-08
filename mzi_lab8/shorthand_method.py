import textwrap
from PIL import Image, ImageFont, ImageDraw

def encode(text, start_img, enc_img_path):
    """ Encode an image """

    red_chanel = start_img.split()[0]
    green_chanel = start_img.split()[1]
    blue_chanel = start_img.split()[2]

    image_text = write_text(text, start_img.size)
    bw_encode = image_text.convert('1')

    enc_img = Image.new("RGB", (start_img.size[0], start_img.size[1]))
    pixels = enc_img.load()
    for i in range(start_img.size[0]):
        for j in range(start_img.size[1]):
            red_template_pix = bin(red_chanel.getpixel((i, j)))
            if bin(bw_encode.getpixel((i, j)))[-1] == '1':
                red_template_pix = red_template_pix[:-1] + '1'
            else:
                red_template_pix = red_template_pix[:-1] + '0'
            pixels[i, j] = (int(red_template_pix, 2), green_chanel.getpixel((i, j)), blue_chanel.getpixel((i, j)))

    enc_img.save(enc_img_path)


def decode(enc_img, img_path):
    """ Decode an image """

    red_channel = enc_img.split()[0]
    dec_img = Image.new("RGB", enc_img.size)
    pixels = dec_img.load()
    for i in range(enc_img.size[0]):
        for j in range(enc_img.size[1]):
            if bin(red_channel.getpixel((i, j)))[-1] == '0':
                pixels[i, j] = (255, 255, 255)
            else:
                pixels[i, j] = (0, 0, 0)
    dec_img.save(img_path)


def write_text(text, img_size):
    """ depict a text on an image """
    img_text = Image.new("RGB", img_size)

    drawer = ImageDraw.Draw(img_text)
    offset = 50
    for line in textwrap.wrap(text, width=60):
        drawer.text((50, offset), line, font=ImageFont.load_default().font)
        offset += 10
    return img_text

if __name__ == '__main__':
    # Initilization
    msg = 'message to ecrypt'
    encrypt_path = 'encrypted.png'
    source_img = Image.open('source.png')

    # Encoding
    encode(msg, source_img, encrypt_path)

    # Decoding
    encrypted_image = Image.open(encrypt_path)
    decode(encrypted_image, 'decrypted.png')