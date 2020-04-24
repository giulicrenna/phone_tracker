import phonenumbers 
from phonenumbers import geocoder
from phonenumbers import carrier

numero = input('Ingrese No. a localizar: ')
ch_numero = phonenumbers.parse(numero, 'CH')

print(geocoder.description_for_number(ch_numero,"en"))

#s_num = pn.parse(numero, 'RO')
#print(carrier.name_for_number(s_num, "en"))