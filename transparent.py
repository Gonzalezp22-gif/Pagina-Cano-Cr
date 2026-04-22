import sys
import subprocess

try:
    from PIL import Image
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Pillow'])
    from PIL import Image

def make_transparent(img_path, out_path):
    img = Image.open(img_path).convert('RGBA')
    datas = img.getdata()
    
    new_data = []
    # threshold for white
    threshold = 230
    for item in datas:
        # if RGB is close to white, make transparent
        if item[0] > threshold and item[1] > threshold and item[2] > threshold:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(out_path, 'PNG')
    print('Done making background transparent!')

make_transparent('logo_cano.png', 'logo_cano.png')
