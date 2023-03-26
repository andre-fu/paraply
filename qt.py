from pprint import pprint
form_dict = {
    'topmostSubform[0].Page1[0].N12CB[0]': 'Yes',
	'topmostSubform[0].Page1[0].N12CB[1]': 'No',
	'topmostSubform[0].Page1[0].N13ACB[0]': 'Yes',
	'topmostSubform[0].Page1[0].N13ACB[1]': 'No',
	'topmostSubform[0].Page1[0].N13BFLD[0]': 'other countries social credits',
	'topmostSubform[0].Page1[0].N14ACB[0]': 'Yes',
	'topmostSubform[0].Page1[0].N14ACB[1]': 'No',
	'topmostSubform[0].Page1[0].N14BCB[0]': 'Off',
	'topmostSubform[0].Page1[0].N14BFLD1[0]': 'B MONTH',
	'topmostSubform[0].Page1[0].N14BFLD2[0]': 'B YEAR',
	'topmostSubform[0].Page1[0].N14CFLD1[0]': 'c month',
	'topmostSubform[0].Page1[0].N14CFLD2[0]': 'c YEAR',
	'topmostSubform[0].Page1[0].N1FLD[0]': 'name',
	'topmostSubform[0].Page1[0].N2FLD[0]': 'SSNss',
	'topmostSubform[0].Page1[0].N3CB[0]': 'Female',
	'topmostSubform[0].Page1[0].N3CB[1]': 'Male',
	'topmostSubform[0].Page1[0].N4SpeakFLD[0]': 'speak lang',
	'topmostSubform[0].Page1[0].N4WriteFLD[0]': 'write lang',
	'topmostSubform[0].Page1[0].N5AFLD[0]': 'dob',
	'topmostSubform[0].Page1[0].N5BFLD[0]': '5b: name of city',
	'topmostSubform[0].Page1[0].N6ACB[0]': 'Yes',
	'topmostSubform[0].Page1[0].N6ACB[1]': 'No',
	'topmostSubform[0].Page1[0].N6BCB[0]': 'Yes',
	'topmostSubform[0].Page1[0].N6BCB[1]': 'No',
	'topmostSubform[0].Page1[0].N6CFLD[0]': 'Lawful Admission',
	'topmostSubform[0].Page1[0].N7AFLD[0]': 'name if diff ',
	'topmostSubform[0].Page1[0].N7BCB[0]': 'Yes',
	'topmostSubform[0].Page1[0].N7BCB[1]': 'No',
	'topmostSubform[0].Page1[0].N7CFLD[0]': 'other names',
	'topmostSubform[0].Page1[0].N8ACB[0]': 'Yes',
	'topmostSubform[0].Page1[0].N8ACB[1]': 'No',
	'topmostSubform[0].Page1[0].N8BFLD[0]': 'more ssns',
	'topmostSubform[0].Page1[0].N9FLD[0]': 'date for severerity',

	'topmostSubform\\1330\\135\\056Page1\\1330\\135\\056N14CCB\\1330\\135': 'Off',
	'topmostSubform\\1330\\135\\056Page1\\1330\\135\\056TextField1\\1330\\135': ''
 }


newd = dict()
for k, v in form_dict.items():
	newd[v] = k

pprint(newd)
