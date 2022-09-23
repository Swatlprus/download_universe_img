import os
from urllib.parse import urlparse
from urllib.parse import unquote

def get_type_img(url):
    unquote_url = unquote(url)
    urlparse_url = urlparse(unquote_url)
    file_extension = os.path.splitext(
        f'{urlparse_url.netloc}{urlparse_url.path}')[-1]
    return file_extension