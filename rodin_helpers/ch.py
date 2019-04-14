from simplech import ClickHouse, bytes_decoder, json_decoder
from io import StringIO

import pandas as pd


ch = ClickHouse()


def pd_wide(columns=250, rows=100, col_width=1000):
    pd.options.display.max_columns = columns
    pd.options.display.max_rows = rows
    pd.options.display.max_colwidth = col_width


def df_from_query(query, index=None):
    query += ' FORMAT CSVWithNames'
    result = ch.select(query)
    df = pd.read_csv(StringIO(result))
    if index: df.set_index(index, inplace=True)
    return df


def select_unpack(query, separator='.'):
    accum = []
    for obj in ch.objects_stream(query):
        obj['data'] = dict(zip(obj.pop('data.key', []), obj.pop('data.value', [])))
        obj['extra'] = dict(zip(obj.pop('extra.key', []), obj.pop('extra.value', [])))
        obj['data_extra'] = dict(zip(obj.pop('data_extra.key', []), obj.pop('data_extra.value', [])))
        accum.append(obj)
    return pd.io.json.json_normalize(accum, sep=separator) 
