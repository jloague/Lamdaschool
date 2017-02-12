import requests

contact = {'name': "Derrick", 'lastname': "Daniels", 'email': "derrickisdp@gmail.com", 'message': "Testing this out."}
r = requests.post('https://lambdaschool.com/contact-form', json=contact)

print(r.text)
