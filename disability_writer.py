from fillpdf import fillpdfs
from pprint import pprint

a = fillpdfs.get_form_fields("newfile.pdf")
pprint(a)

# returns a dictionary of fields
# Set the returned dictionary values a save to a variable
# For radio boxes ('Off' = not filled, 'Yes' = filled)

form_dict = {
    "topmostSubform\\1330\\135\\056Page1\\1330\\135\\056N1FLD\\1330\\135": "Bob Johnson",
    "topmostSubform\\1330\\135\\056Page1\\1330\\135\\056N2FLD\\1330\\135": "999-99-999",
    'topmostSubform[0].Page1[0].N4SpeakFLD[0]': 'Spanish',
}

q_to_item = {
	'': 'topmostSubform\\1330\\135\\056Page1\\1330\\135\\056TextField1\\1330\\135',
	'5.b: name of city': 'topmostSubform[0].Page1[0].N5BFLD[0]',
	'12b. MONTH': 'topmostSubform[0].Page1[0].N14BFLD1[0]',
	'12b. YEAR': 'topmostSubform[0].Page1[0].N14BFLD2[0]',
	'3. Female': 'topmostSubform[0].Page1[0].N3CB[0]',
	'6.c. Lawful Admission': 'topmostSubform[0].Page1[0].N6CFLD[0]',
	'3. Male': 'topmostSubform[0].Page1[0].N3CB[1]',
	'No': 'topmostSubform[0].Page1[0].N8ACB[1]',
	'Off': 'topmostSubform\\1330\\135\\056Page1\\1330\\135\\056N14CCB\\1330\\135',
	'2. SSN': 'topmostSubform[0].Page1[0].N2FLD[0]',
	'Yes': 'topmostSubform[0].Page1[0].N8ACB[0]',
	'12c. YEAR': 'topmostSubform[0].Page1[0].N14CFLD2[0]',
	'12c. month': 'topmostSubform[0].Page1[0].N14CFLD1[0]',
	'9 date for severerity': 'topmostSubform[0].Page1[0].N9FLD[0]',
	'5.a. dob': 'topmostSubform[0].Page1[0].N5AFLD[0]',
	'8b. more ssns': 'topmostSubform[0].Page1[0].N8BFLD[0]',
	'1. Full Name': 'topmostSubform[0].Page1[0].N1FLD[0]',
	'7a. name if diff ': 'topmostSubform[0].Page1[0].N7AFLD[0]',
	'11.b. other countries social credits': 'topmostSubform[0].Page1[0].N13BFLD[0]',
	'other names': 'topmostSubform[0].Page1[0].N7CFLD[0]',
	'4. speak lang': 'topmostSubform[0].Page1[0].N4SpeakFLD[0]',
	'4. write lang': 'topmostSubform[0].Page1[0].N4WriteFLD[0]'
}


fillpdfs.write_fillable_pdf('newfile.pdf', 'output.pdf', form_dict)