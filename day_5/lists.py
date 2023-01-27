lista_vacia =  list()
lista5 = ["manzana", "agua", "película", "platano", "mamá"]
print(len(lista5))
print(lista5[0]+ " " +  lista5[2] +  " " + lista5[4])
mixed_data_types = ["Ángel" + "16" + "1.85" + "single" + "calle Marcelino Camacho"]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print( it_companies)
print(len(it_companies))
print(f"{it_companies[0]} {it_companies[3]} {it_companies[6]}")
it_companies[3] = "Xiaomi"
print(it_companies)
it_companies.append("Acer")
print(it_companies)
it_companies.insert(4, "HP")
print(it_companies)
it_companies[1] = it_companies[1].upper()
print(it_companies)
print("#, ".join(it_companies))
print("Facebook" in it_companies)
it_companies.sort(reverse=False)
print(it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[3:9])
print(it_companies[0:6])
print(it_companies[0:4]+ it_companies[5:9])
print(it_companies[1:])
it_companies4 = it_companies[:4]+ it_companies[5:]
print(it_companies4)
print(it_companies[:8])
print(it_companies.clear())
del it_companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_back = front_end + back_end
print(front_back)
full_stack = front_end + back_end
full_stack.insert(5,"Python") 
full_stack.insert(6, "SQL") 
print(full_stack)

#voluntario:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort(reverse=False)
print(ages)
print("el número más bajo es " + str(ages[0])+ " y el más alto " + str(ages[9]))
median_age = (ages[4]+ ages[5])/2
print("la mediana es " + str(median_age))
average_age = (ages[0] + ages[9])/2
print("la media es de " + str(average_age))
range_age= ages[0] + ages[9]
print("el rango es de " + str(range_age))
print(abs(ages[0] - range_age))
print(abs(ages[9]- average_age))
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
print(countries[int(len(countries)/2)])
countries_1 = countries[0:int(len(countries)/2)]
countries_2= countries[int(len(countries)/2):]
print(countries_1)
print(countries_2)
paises = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china = paises[0]
rusia = paises[1]
usa = paises[2]
print(china)
print(rusia)
print(usa)
scandic_countries = paises[3:]
print(scandic_countries)