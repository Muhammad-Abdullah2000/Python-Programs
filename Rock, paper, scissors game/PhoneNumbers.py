import phonenumbers
from phonenumbers import geocoder

phone_numbers = phonenumbers.parse("+923360734521")

print(geocoder.description_for_number(phone_numbers,'en'))