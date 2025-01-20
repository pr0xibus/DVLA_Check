# DVLA_Check
Simple Python script, to check a UK Car on the DVLA Site

I decided to write a small Application, that would allow someone to enter a UK Registration Number, and it SHOULD give back the details of the car.
Users can download and run the application, Please check the Requirements below

Requirements:
API Key from DVLA - https://developer-portal.driver-vehicle-licensing.api.gov.uk/apis/vehicle-enquiry-service/vehicle-enquiry-service-description.html
Python Modules - Json, Requests

1:  You will need to uncomment and replace the 'x-api-key' with either your TEST or LIVE API Key.
2:  You will also need to uncomment one of the URLS depending if your using Live or Test
3.  Please enter the Variable used for the URL  on 
3.1 response = requests.post('YOUR URL FROM ABOVE', headers=headers, data=json.dumps(data))


