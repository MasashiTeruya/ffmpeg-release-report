import unittest
from url_parser import UrlParser

class   UrlParserTest(unittest.TestCase):
    def test_parse(self):
        f = open('sample.html')
        text = f.read()
        parser = UrlParser()
        result = parser.parse(text)
        self.assertIsNotNone(result)
        self.assertEqual('ffmpeg-0.10.1.tar.gz', result[0])
        self.assertEqual('ffmpeg-0.10.10.tar.gz', result[1])
        