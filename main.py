import requests
import json


error_dictionary={400:'Invalid Format',
                  403:'Forbidden',
                  404:'Not Found',
                  429:'Too Many Requests',
                  502:'Bad Gateway',
                  504:'Gateway Timeout'}


class CarClass:
    def __init__(self, registrationNumber, co2Emissions, engineCapacity, euroStatus, fuelType, motStatus, colour,
                 make, yearOfManufacture, taxStatus, dateOfLastV5CIssued, wheelplan, realDrivingEmissions):

        self.registrationNumber = registrationNumber
        self.co2Emissions = co2Emissions
        self.engineCapacity = engineCapacity
        self.euroStatus = euroStatus
        self.fuelType = fuelType
        self.motStatus = motStatus
        self.colour = colour
        self.make = make
        self.yearOfManufacture = yearOfManufacture
        self.taxStatus = taxStatus
        self.dateOfLastV5CIssued = dateOfLastV5CIssued
        self.wheelplan = wheelplan
        self.realDrivingEmissions = realDrivingEmissions

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
        print("Emissions: " + self.realDrivingEmissions)

#test_url = 'https://uat.driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles'
#live_url = 'https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles'

headers = {
    #'x-api-key': 'YOUR API KEY',  # TEST API
    #'x-api-key': 'YOUR API KEY',  # LIVE API
    'Content-Type': 'application/json'
}

data = {

    'registrationNumber':'AA19DSL'
}

response = requests.post('YOUR URL FROM ABOVE', headers=headers, data=json.dumps(data))

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
        response_json.get('wheelplan', 'Unknown'),
        response_json.get('realDrivingEmissions', 'Unknown'))

    CarClass.display_details(car_object)


elif response.status_code in error_dictionary:
    print(f"Error: {response.status_code}: {error_dictionary[response.status_code]}")

else:
    print("Unknown Status Code: " + str(response.status_code))




