# DVLA_Check
Simple Python script, to check a UK Car on the DVLA Site

I decided to write a small Application, that would allow someone to enter a UK Registration Number, and it SHOULD give back the details of the car.
Users can download and run the application, Please check the Requirements below

Requirements
You will require an API Key from DVLA  https://developer-portal.driver-vehicle-licensing.api.gov.uk/apis/vehicle-enquiry-service/vehicle-enquiry-service-description.html
Python modules in use are requests and json

Make sure to enter your API keys on lines 7/8.
Also make sure you change which key to use on line 63.
If you want to use the LIVE data then you will need to enter your VRNs on line 68 under the data section, it should look like as an example

'registrationNumber':'AA60BRL'
