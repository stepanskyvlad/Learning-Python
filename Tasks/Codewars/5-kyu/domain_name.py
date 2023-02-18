# https://www.codewars.com/kata/514a024011ea4fb54200004b
# Extract the domain name from a URL

import re


def domain_name(url):
    if "www" in url:
        pattern = r'(?<=[\.]).*?(?=[\.])'
        name = re.search(pattern, url)
        return name[0]
    elif "//" in url:
        pattern = r'(?<=[\/]).*?(?=[\.])'
        name = re.findall(pattern, url)
        return name[0][1:]
    else:
        pattern = r'.*?(?=[\.])'
        name = re.findall(pattern, url)
        return name[0]


if __name__ == "__main__":
    print(domain_name("http://github.com/carbonfive/raygun"))
    print(domain_name("http://www.zombie-bites.com"))
    print(domain_name("http://google.co.jp"))
    print(domain_name("icann.org"))
