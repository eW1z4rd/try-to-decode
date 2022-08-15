import random
import string

from lib.convert import Convert


def test(s):
    # url
    assert s == Convert(s).url_encode().url_decode().get()
    assert s == Convert(s.encode()).url_encode().url_decode().get()
    # html
    assert s == Convert(s).html_encode().html_decode().get()
    assert s == Convert(s.encode()).html_encode().html_decode().get()
    # base64
    assert s == Convert(s).str_to_base64().base64_to_str().get()
    assert s == Convert(s.encode()).str_to_base64().base64_to_str().get()
    # unicode
    assert s == Convert(s).str_to_unicode().unicode_to_str().get()
    assert s == Convert(s.encode()).str_to_unicode().unicode_to_str().get()
    # bin
    assert s == Convert(s).str_to_bin().bin_to_str().get()
    assert s == Convert(s.encode()).str_to_bin().bin_to_str().get()
    # ord
    assert s == Convert(s).str_to_oct().oct_to_str().get()
    assert s == Convert(s.encode()).str_to_oct().oct_to_str().get()
    # dec
    assert s == Convert(s).str_to_dec().dec_to_str().get()
    assert s == Convert(s.encode()).str_to_dec().dec_to_str().get()
    # hex
    assert s == Convert(s).str_to_hex().hex_to_str().get()
    assert s == Convert(s.encode()).str_to_hex().hex_to_str().get()


if __name__ == '__main__':
    char_range = f'{string.printable}中文字符'
    for i in range(10000):
        test(''.join(random.sample(char_range, random.randint(1, len(char_range)))))
