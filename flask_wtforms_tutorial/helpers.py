from datetime import datetime

DF_DEFAULT = '%Y-%m-%d'
DF_INTRADAY = '%Y-%m-%d %H:%M:%S'


def str_to_date(v, f=DF_DEFAULT):
    return datetime.strptime(v, f)


def date_to_str(dt, f=DF_DEFAULT):
    return dt.strftime(f)
