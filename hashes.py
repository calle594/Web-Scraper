import sys,re
from hashlib import md5

def get_hashes(soup_var):
    ''' find all hashes on the webpage'''
    str_var = str(soup_var)
    hashes2 = []
    #match must be 32 hex characters.
    #cannot be contained within a larger string of other characters
    hashes = re.findall(r'(?i)(?<![a-z0-9])[a-f0-9]{32}(?![a-z0-9])',str_var)
    hashes.sort()#sort files
    for i in hashes:
        if i not in hashes2:
            hashes2.append(i)
    print(f"[!] {len(hashes)} Hashes Found")
    print('\n'.join('{}: {}'.format(*k) for k in enumerate(hashes2)))
    print()

def get_images(soup_var):
    '''Use regex to find image files '''
    str_var = str(soup_var)
    file2 = []
    #match single character in range a-z,A-Z,0-9 | match any whitespace | match _
    #match \ | match . | match - | match ( | match \ | match )| match :
    #match image file types.
    file = re.findall(r'[a-zA-Z0-9\s_\\.\-\(\):]+(?:.bmp|.jpg|.jpeg|.png|.JPG)',str_var)
    file.sort()#sort files
    for i in file:
        if i not in file2:
            file2.append(i)
    print(f"[!] {len(file)} Image Files Found")
    print('\n'.join('{}: {}'.format(*k) for k in enumerate(file2)))
    print()

def get_docs(soup_var):
    '''Get Document files using regex'''
    str_var = str(soup_var)
    file3 = []
    #match single character in range a-z,A-Z,0-9 | match any whitespace | match _
    #match \ | match . | match - | match ( | match \ | match )| match :
    #match document file types.
    file = re.findall('[a-zA-Z0-9\s_\\.\-\(\):]+(?:.doc|.docx|.pdf)', str_var)
    file.sort()
    for i in file:
        if i not in file3:
            file3.append(i)
    print(f"[!] {len(file)} Document Files Found")
    print('\n'.join('{}: {}'.format(*k) for k in enumerate(file3)))
    print()
    
#https://stackoverflow.com/questions/373194/python-regex-for-md5-hash
#user ʞɔıu
#(?i)(?<![a-z0-9])[a-f0-9]{32}(?![a-z0-9])
