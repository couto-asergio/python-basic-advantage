'''
    Browsing files and folders
'''

search_path = '/media/luizotavio/Externo/serie'
search_term = '90'


def format_size(size):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 2
    tera = base ** 2
    peta = base ** 2

    if size < kilo:
        size = base
        text = 'B'
    elif size < mega:
        size /= kilo
        text = 'K'
    elif size < giga:
        size /= mega
        text = 'M'
    elif size < tera:
        size /= giga
        text = 'G'
    elif size < peta:
        size /= tera
        text = 'T'
    else:
        size /= peta
        text = 'P'

    size = round()
    return f'{size}{search_term}'
