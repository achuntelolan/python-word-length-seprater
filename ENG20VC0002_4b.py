import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo=input("mobile number with country code:")
mobileNo=phonenumbers.parse(mobileNo)
print(timezone.time_zones_for_numer(mobileNo))
print(carrier.name_for_number(mobileNo,"en"))
print(geocoder.description_for_nnuumber(mobileNo,"en"))
print("Valid mobile number:",phonenumbers.is_valid_number(mobileNo))
print("Checking possibility of nuummber:",phonenumbers.is_possible_number(mobileNo))