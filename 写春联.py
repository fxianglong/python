import io
from PIL import Image
import numpy as np
import requests
def get_word(ch,quality):
    fp = io.BytesIO(requests.post(url='http://xufive.sdysit.com/tk',data={'ch':ch}).content)
    im = Image.open(fp)
    w,h = im.size
    if quality == 'M':
        w,h = int(w*0.75), int(0.75*h)
    elif quality == 'L':
        w,h = int(w*0.5), int(0.5*h)
    
    return im.resize((w,h))

def get_bg(quality):
    return get_word('bg',quality)

def write_couplets(text,HorV='V',quality='L',out_file=None):
    usize = {'H':(640,23), 'M':(480,18),'L':(320,12)}
    bg_im = get_bg(quality)
    text_list = [list(item) for item in text.split( )]
    rows = len(text_list)
    cols = max([len(item) for item in text_list])

    if HorV == 'V':
        ow, oh = 40+rows*usize[quality][0]+(rows-1)*10,40+cols*usize[quality][0]
    else:
        ow, oh = 40+cols*usize[quality][0],40+rows*usize[quality][0]+(rows-1)*10
    out_im = Image.new('RGBA',(ow,oh),'#f0f0f0')

    for row in range(rows):
        if HorV == 'V':
            row_im = Image.new('RGBA',(usize[quality][0],cols*usize[quality][0]),'white')
            offset = (ow-(usize[quality][0]+10)*(row+1)-10,20)
        else:
            row_im = Image.new('RGBA',(cols*usize[quality][0],usize[quality][0]),'white')
            offset = (20,20+(usize[quality][0]+10)*row)
        
        for col,ch in enumerate(text_list[row]):
            if HorV == 'V':
                pos = (0,col*usize[quality][0])
            else:
                pos = (col*usize[quality][0],0)
            
            ch_im = get_word(ch,quality)
            row_im.paste(bg_im,pos)
            row_im.paste(ch_im,(pos[0]+usize[quality][1],pos[1]+usize[quality][1]),mask=ch_im)
        out_im.paste(row_im,offset)
    
    if out_file:
        out_im.convert('RGB').save(out_file)
    out_im.show()

text = '普天同庆 欢度春节'
write_couplets(text,HorV='V',quality='M',out_file='普天同庆.jpg')
