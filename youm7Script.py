import requests
from bs4 import BeautifulSoup
import lxml

base_url = 'https://natega.youm7.com/'
form_action_url = '/Result/1'
full_url = base_url + form_action_url


seatnumber=input("please enter your seat number")
form_data = {
    'seatNo': seatnumber  # Replace with the desired seat number
}
response= requests.post(url=full_url,data=form_data)
if response.status_code == 200:
    print("Form submitted successfully.")
    # Parse the resulting page
    response.encoding='utf-8'
    soup = BeautifulSoup(response.content, 'lxml')
    
    
else:
    print(f"Failed to submit form. Status code: {response.status_code}")
formseatnumber=soup.find('div',class_='FixedLeftSide').contents[1]
allp=formseatnumber.find_all('p')

print(f"seat number is ::: {allp[1].text.strip()}")
print(f"Name ::: {allp[2].text.strip()}")
print(f"Arabic ::: {allp[5].text.strip()}")
print(f"English ::: {allp[6].text.strip()}")
print(f"History ::: {allp[7].text.strip()}")
print(f"Algebra::: {allp[8].text.strip()}")
print(f"Engineering ::: {allp[9].text.strip()}")
print(f"Science ::: {allp[11].text.strip()}")
print(f"Result ::: {allp[12].text.strip()}")
print(f"State ::: {allp[19].text.strip()}")