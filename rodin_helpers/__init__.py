from IPython.core.display import display, HTML, Markdown
from IPython.display import YouTubeVideo
from typing import Generator

def show_link(url, title='Authorize'):
    display(HTML(f'Click <a href="{url}" target="_blank">{title}</a> or open {url} in your browser'))

def video(id):
    return YouTubeVideo(id, width=700, height=400)

def walk(item, level=0, path=[], limit_list=None):
    path_str = " > ".join(map(str, path))
    if isinstance(item, dict):
        print(f"[dict  {path_str}")
        for key, val in item.items():
            walk(val, level+1, [*path, key], limit_list=limit_list)
    elif isinstance(item, list):
        print(f"[list  {path_str}")
        for i, val in enumerate(item):
            walk(val, level+1, [*path, i], limit_list=limit_list)
            if limit_list and i == limit_list:
                break
    else:
        print(f'|      {path_str}={str(item)}')


def print_rows(recods, limit=None):
    """
    print_rows(['a', 'b'], [{'a':1, 'b':2}])
    """
    if isinstance(recods, Generator):
        recods = [*recods]
    cols = sorted({c for record in recods for c in record.keys()})
    txt = '|'.join(cols)+'\n'
    txt += '|'.join(['---' for i in range(len(cols))])+'\n'
    for i, row in enumerate(recods):
        txt += '|'.join([str(row.get(f) or '-').replace('|', '&#124;') for f in cols])+'\n'
        if limit and limit <= i:
            break
    display(Markdown(txt))


def flatten_dict(dd, separator='.', prefix=''):
    return {
        prefix + separator + k if prefix else k: v
        for kk, vv in dd.items()
        for k, v in flatten_dict(vv, separator, kk).items()
    } if isinstance(dd, dict) else {
        prefix: dd
    }