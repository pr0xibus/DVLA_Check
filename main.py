import random

import requests
import json


test_API_key= 'YOUR TEST API KEY HERE'
live_API_key= 'YOUR LIVE API KEY HERE'

test_url = 'https://uat.driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles'
live_url = 'https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles'

error_dictionary={400:'Invalid Format',
                  403:'Forbidden',
                  404:'Not Found',
                  429:'Too Many Requests',
                  500:'Internal Error',
                  502:'Bad Gateway',
                  503:'Service Unavailable',
                  504:'Gateway Timeout'}


test_vrn_list=['AA19AAA','AA19EEE','AA19PPP','L2WPS','AA19SRN','AA19MOT',
          'AA19AMP','ER19BAD','ER19NFD','ER19THR','ER19ERR','ER19MNT']


class CarClass:
    def __init__(self, registration_number, co2_emissions, engine_capacity, euro_status, fuel_type, mot_status, car_colour,
                 car_make, year_of_manufacture, tax_status, date_of_last_v5c_issued, wheel_plan):

        self.registrationNumber = registration_number
        self.co2Emissions = co2_emissions
        self.engineCapacity = engine_capacity
        self.euroStatus = euro_status
        self.fuelType = fuel_type
        self.motStatus = mot_status
        self.colour = car_colour
        self.make = car_make
        self.yearOfManufacture = year_of_manufacture
        self.taxStatus = tax_status
        self.dateOfLastV5CIssued = date_of_last_v5c_issued
        self.wheelplan = wheel_plan


    def display_details(self):
        print("Registration Number: " + self.registrationNumber)
        print("Make: " + self.make)
        print("Colour: " + self.colour)
        print("Engine Capacity: " + str(self.engineCapacity))
        print("Fuel Type: " + self.fuelType)
        print("Euro Status: " + str(self.euroStatus))
        print("Co2: " + str(self.co2Emissions))
        print("Year of Manufacture: " + str(self.yearOfManufacture))
        print("MOT: " + self.motStatus)
        print("Tax: " + self.taxStatus)
        print("V5 Issue: " + self.dateOfLastV5CIssued)
        print("Wheel Plan: " + self.wheelplan)


test_vrn = random.choice(test_vrn_list)

headers = {
    'x-api-key': test_API_key,
    'Content-Type': 'application/json'
}

data = {
    'registrationNumber':test_vrn
}

response = requests.post(test_url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    response_json = response.json()
    car_object = CarClass(
        response_json.get('registrationNumber', ''),
        response_json.get('co2Emissions', 0),
        response_json.get('engineCapacity', 0),
        response_json.get('euroStatus' 'Unknown'),
        response_json.get('fuelType', 'Unknown'),
        response_json.get('motStatus', 'Unknown'),
        response_json.get('colour', 'Unknown'),
        response_json.get('make', 'Unknown'),
        response_json.get('yearOfManufacture', 0),
        response_json.get('taxStatus', 'Unknown'),
        response_json.get('dateOfLastV5CIssued', 'Unknown'),
        response_json.get('wheelplan', 'Unknown'))


    CarClass.display_details(car_object)


elif response.status_code in error_dictionary:
    print(f"Error: {response.status_code}: {error_dictionary[response.status_code]}")

else:
    print("Unknown Status Code: " + str(response.status_code))




