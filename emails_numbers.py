import re

def find_email(soup_var):
    '''Find emails with regex'''
    str_var = str(soup_var)
    emails2 = []
    #Regex for emails
    #any character except . @ or whitespace 1 or more times
    #match @ symbol,match any char except @ and whitespace atleast 1 time
    #match . character
    #match and word char 2-6 times
    emails = re.findall(r'[^>@\s]+@[^@\s]+\.\w{2,6}',str_var)
    emails.sort()       
    for email in emails:
        pass
    for i in emails:
        if i not in emails2:
            emails2.append(i)          
    #print number of emails found and the emails, add space after
    print(f"[!] {len(emails2)} Email Addresses Found")
    print('\n'.join('{}: {}'.format(*k) for k in enumerate(emails2)))
    print()
    
def phone_numbers(soup_var):
    '''Uses regex to find phone numbers,loop to remove numbers less than 11
       digits,remove index 4 through 7'''
    str_var = str(soup_var)
    phones2 = []
    #Regex for phone numbers
    #\+?\d{1,5}\s? - +1 or +44
    #\(?\d{1,4}?\)? - first section of numbers
    #[-\s]? - possible spacing or dash
    #\d{1,3} -  2nd section of numbers
    #[-\s]? -  possible spacing or dash
    #\d{1,3}\s? - 3rd sections of numbers and maybe whitspace
    #\d{1,4}? - 4th section of numbers 
    phones = re.findall (r'[\+\d]?(\d{2,3}[-\.\s]??\d{2,3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})',str_var)
    phones.sort()
    for i in phones:
        if i not in phones2:
            phones2.append(i)
    for i in phones2:
        if len(i) < 13:# if length is less than 13 remove
            phones2.remove(i)
    del phones2[4:7]# remove index 4 to 7

    #print number of phone numbers found and the phonenumbers, add space after
    print(f"[!] {len(phones2)} Phone Numbers Found")
    print('\n'.join('{}: {}'.format(*k) for k in enumerate(phones2)))
    print()

#https://www.youtube.com/watch?v=d0sWs2e7rf0&t=302s
#^\+?\d.\s?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}? - original regex 
#modfied to meet requirements  
#user - optikalefx
