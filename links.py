import enum
import re

def print_links(soup_var):
    ''' find all hyperlinks on the webpage input and print '''
    str_var = str(soup_var) #Regex
    links2 = []
    #regex to match on hyperlinks
    #raw string for less escaping - match for href tags potentially with double or single quotations
    #group ([^\'" >]+) - dont match characters in group.
    links = re.findall(r'href=[\'"]?([^\'" >]+)',str_var)
    links.sort()#sort links
    for i in links:
        if "@" not in i:
                links2.append(i)

    #print number of hyperlinks found and the hyperlinks, add space after
    print(f'[!] {len(links2)} Hyperlinks Found')
    print('\n'.join('{}: {}'.format(*k) for k in enumerate(links2)))
    print()


#href=[\'"]?([^\'" >]+) - code used
#https://stackoverflow.com/questions/499345/regular-expression-to-extract-url-from-an-html-link
#User - David
