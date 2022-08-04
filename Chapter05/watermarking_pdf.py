import argparse
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import PyPDF2
from pdf2image import convert_from_path

DEFAULT_OUTPUT = 'watermarked.pdf'
DEFAULT_BY = 'default user'
IMTERMEDIATE_ENCRYPT_FILE = 'temp.pdf'

WOTERMARK_SIZE = (200, 200)

def encrypt(out_pdf, password):
    print('Encrypting the document')
    output_pdf = PyPDF2.PdfFileWriter()
    in_file = open(out_pdf, 'rb')
    input_pdf = PyPDF2.PdfFileReader(in_file)
    output_pdf.appendPagesFromReader(input_pdf)
    output_pdf.encrypt(password)

    with open(IMTERMEDIATE_ENCRYPT_FILE, 'wb') as out_file:
        output_pdf.write(out_file)

    in_file.close()

    os.rename(IMTERMEDIATE_ENCRYPT_FILE, out_pdf)

def create_watermark(watermarked_by):
    print("Creating a watermark")
    mask = Image.new('L', WOTERMARK_SIZE, 0)
    draw = ImageDraw.Draw(mask)
    font = ImageFont.load_default()
    text = "WATERMARKED BY {}\n{}.".format(watermarked_by, datetime.now())
    draw.multiline_text((0, 100), text, 55, font=font)

    watermark = Image.new('RGB', WOTERMARK_SIZE)
    watermark.putalpha(mask)
    watermark.resize((1950,1950))
    watermark.rotate(45)

    bbox = watermark.getbbox()
    watermark = watermark.crop(bbox)

    return watermark

def apply_watermark(watermark, in_pdf, out_pdf):
    print(in_pdf)
    print('Watermarking the document')
    images = convert_from_path(in_pdf, poppler_path=r"C:\poppler-22.04.0\Library\bin")

    hi, wi = images[0].size
    hw, ww = watermark.size

    position = ((hi-hw) // 2, (wi-ww)//2)

    for image in images:
        image.paste(watermark, position, watermark)

    images[0].save(out_pdf, save_all=True, append_images=images[1:])

def main(in_pdf, out_pdf, watermarked_by, password):
    watermark = create_watermark(watermarked_by)
    apply_watermark(watermark, in_pdf, out_pdf)

    if password:
        encrypt(out_pdf, password)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='pdf', type=str,
                        help='PDF to watermark')
    parser.add_argument('-o', type=str,
                        help=f'Output PDF filename, default: {DEFAULT_OUTPUT}',
                        default=DEFAULT_OUTPUT)
    parser.add_argument('-u', type=str,
                        help=f'Watermarked by, default: {DEFAULT_BY}',
                        default=DEFAULT_BY)
    parser.add_argument('-p', type=str,
                        help='Password')
    args = parser.parse_args()
    main(args.pdf, args.o, args.u, args.p)