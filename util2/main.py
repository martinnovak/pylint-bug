from collections import namedtuple

UrlComponents = namedtuple(
    typename='UrlComponents',
    field_names=['scheme', 'netloc', 'url', 'path', 'query', 'fragment']
)
