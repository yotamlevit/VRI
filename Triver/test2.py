# -*- coding: utf-8 -*-

from googlesearch.googlesearch import GoogleSearch
response = GoogleSearch().search("something")
for result in response.results:
    print("Title: " + result.title)
    print("Content: " + result.getText())


def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()