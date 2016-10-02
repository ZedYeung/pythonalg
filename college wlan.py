import mechanicalsoup
from mechanicalsoup import Browser
from pprint import pprint
from bs4 import BeautifulSoup

# 
url = ""

br = Browser()
page = br.get(url)
form = page.soup.select("form")[1]

# user name
form.find("input", {"name": "DDDDD"})["value"] = ""
# password
form.find("input", {"name": "upass"})["value"] = ""
# is ok to keep that OMNKKey empty 
form.find("input", {"name": "0MKKey"})["value"] = ""

# (the method here is __setitem__)
success_page = br.submit(form, page.url)  # submit current form

print("--------------------------------------------------------------------")
print('form texts:')
success_info = success_page.soup.find('form', {'name': 'form1'})
pprint(success_info.get_text())
    
print("--------------------------------------------------------------------")

print('scripts:')
scripts = success_page.soup.findAll('script').get_text()
pprint(scripts)



