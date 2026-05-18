from pytubefix import YouTube

url="https://www.youtube.com/watch?v=YGI-J-ggz9A&list=RDYGI-J-ggz9A&start_radio=1"

YouTube(url).streams.first().download()