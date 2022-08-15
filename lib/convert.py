import base64
from typing import Union
from urllib.parse import quote, unquote


class Convert(object):
    entity_maps = {
        '&': '&amp;',
        ' ': '&nbsp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        '\'': '&apos;'
    }

    def __init__(self, s: Union[str, bytes]):
        if isinstance(s, str):
            self._str = s
            self._bytes = s.encode()
        elif isinstance(s, bytes):
            self._str = s.decode()
            self._bytes = s
        else:
            raise TypeError

    def get(self) -> str:
        return self._str

    def get_bytes(self) -> bytes:
        return self._bytes

    def url_encode(self, encoding='utf-8'):
        """url encode"""
        return Convert(quote(self._str, safe='', encoding=encoding))

    def url_decode(self, encoding='utf-8'):
        """url decode"""
        return Convert(unquote(self._str, encoding=encoding))

    def html_encode(self):
        """html encode"""
        for k, v in self.entity_maps.items():
            if k in self._str:
                self._str = self._str.replace(k, v)
        return Convert(self._str)

    def html_decode(self):
        """html decode"""
        for k, v in self.entity_maps.items():
            if v in self._str:
                self._str = self._str.replace(v, k)
        return Convert(self._str)

    def str_to_base64(self):
        """base64 encode"""
        return Convert(base64.b64encode(self._bytes))

    def base64_to_str(self):
        """base64 decode"""
        return Convert(base64.b64decode(self._str).decode())

    def str_to_unicode(self):
        """unicode encode"""
        return Convert(''.join([f' {ord(c):04x}'.replace(' ', '\\u') for c in self._str]))

    def unicode_to_str(self):
        """unicode decode"""
        return Convert(self._bytes.decode('unicode_escape'))

    def str_to_bin(self, seq=' '):
        """bin encode"""
        return Convert(self._bin_oct_dec_hex('b', seq, False))

    def bin_to_str(self, seq=' '):
        """bin decode"""
        return Convert(self._bin_oct_dec_hex(2, seq, True))

    def str_to_oct(self, seq='\\0'):
        """oct encode"""
        return Convert(self._bin_oct_dec_hex('o', seq, False))

    def oct_to_str(self, seq='\\0'):
        """oct decode"""
        return Convert(self._bin_oct_dec_hex(8, seq, True))

    def str_to_dec(self, seq='\\'):
        """dec encode"""
        return Convert(self._bin_oct_dec_hex('d', seq, False))

    def dec_to_str(self, seq='\\'):
        """dec decode"""
        return Convert(self._bin_oct_dec_hex(10, seq, True))

    def str_to_hex(self, seq='\\0x'):
        """hex encode"""
        return Convert(self._bin_oct_dec_hex('x', seq, False))

    def hex_to_str(self, seq='\\0x'):
        """hex decode"""
        return Convert(self._bin_oct_dec_hex(16, seq, True))

    def _bin_oct_dec_hex(self, method, sep='', reverse=False):
        if not reverse:
            return ''.join([f' {ord(c):02{method}}'.replace(' ', sep) for c in self._str]).strip()
        else:
            return ''.join([chr(i) for i in [int(c, method) for c in self._str.lstrip(sep).split(sep)]])
