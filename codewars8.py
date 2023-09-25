'''
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
 For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
'''

def domain_name(url):
    return url.split('//')[-1].split("www.")[-1].split(".")[0]




def domain_name2(url):
    url = url.replace('www.','')
    url = url.replace('https://','')
    url = url.replace('http://','')
    
    return url[0:url.find('.')]


import re
def domain_name3(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')


print(domain_name("http://www.codewars.com/kata/"))