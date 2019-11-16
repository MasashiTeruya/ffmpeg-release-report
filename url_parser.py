from bs4 import BeautifulSoup

"""Extract URL from HTML.

This parser extracts destination URL from HTML.

  Usage:

  parser = UrlParser()
  filenames = parser.parse(html)

"""
class UrlParser(object):
    """Parses URL from HTML. 

    Args:
        text: HTML
    
    Returns:
        A list of URL.
    """
    def parse(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        links = soup.find_all('a')
        result = []
        for link in links:
            url = link.get('href')
            if not url or not url.endswith('.tar.gz'):
                continue
            result.append(url)
        return result 