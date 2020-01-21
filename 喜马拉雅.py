import requests
import parsel
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
}
def download_media(media_url,media_name):
    response = requests.get(media_url,headers = headers)


    with open(f'{media_name}.mp4',mode = 'wb') as f:
        f.write(response.content)


media_url = "https://fdfs.xmcdn.com/group31/M0B/6C/F8/wKgJX1mG0xDCFUfeAPYI4CGwxyI618.m4a"
#download_media(media_url,media_name)

def media_api(track_id):
    api_url = f'https://www.ximalaya.com/revision/play/v1/audio?id={track_id}&ptype=1'
    response = requests.get(api_url,headers = headers)
    data = response.json()
    src = data['data']['src']
    return src

def get_total_page(page_url):
    response = requests.get(page_url,headers=headers)
    sel = parsel.Selector(response.text)
    sound_list = sel.css('.sound-list ul li a')
    for sound in sound_list[:2]:
        media_url = sound.css('a::attr(href)').extract_first()
        media_url = media_url.split('/')[-1]
        media_name = sound.css('a::attr(title)').extract_first()
        yield media_url,media_name

if __name__  == '__main__':
    for page in range(1,5):
        medias = get_total_page("https://www.ximalaya.com/xiangsheng/9742789/p{page}/")
        for media_id,media_name in medias:
            media_url = media_api(media_id)
            download_media(media_url,media_name)
