# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET

tree = ET.parse('environment.xml')
root = tree.getroot()
for ch in root:
    print(ch.tag, ch.attrib)
    for ch2 in ch:
        print(ch2.tag, ch2.attrib)


def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()