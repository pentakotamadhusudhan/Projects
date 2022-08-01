import barcode
from barcode_generator.models import barmodel


def logic(name,b):
    ean = barcode.get('code128', name)
    filename = ean.save(f'{b}.png', options={"write_text": False})
    return filename
