import PyPDF2
# from PyPDF2 import NameObject
from pprint import pprint

from PyPDF2 import PdfWriter, PdfReader
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject

pdf_file = open('ssa-16-bk.pdf', 'rb')
# pdfreader = PyPDF2.PdfFileReader()

form_dict = {
    "topmostSubform[0].Page1[0].N1FLD[0]": "Bob Johnson",
    "topmostSubform[0].Page1[0].N2FLD[0]": "999-99-999",
    # "topmostSubform[0].Page1[0].N3CB[0]": "/Female",
    # "topmostSubform[0].Page1[0].N3CB[1]": "/Off",
    # "topmostSubform[0].Page1[0].N4SpeakFLD[0]": "",
    # "topmostSubform[0].Page1[0].N4WriteFLD[0]": "",
    # "topmostSubform[0].Page1[0].N5AFLD[0]": "",
    # "topmostSubform[0].Page1[0].N5BFLD[0]": "Bob",
    # "topmostSubform[0].Page1[0].N6ACB[0]": "/Yes",
    # "topmostSubform[0].Page1[0].N6ACB[1]": "/No",
    # "topmostSubform[0].Page1[0].N6BCB[0]": "/Off",
    # "topmostSubform[0].Page1[0].N6BCB[1]": "/Off",
    # "topmostSubform[0].Page1[0].N6CFLD[0]": "",
    # "topmostSubform[0].Page1[0].N7AFLD[0]": "",
    # "topmostSubform[0].Page1[0].N7BCB[0]": "/Off",
    # "topmostSubform[0].Page1[0].N7BCB[1]": "/Off",
    # "topmostSubform[0].Page1[0].N7CFLD[0]": "",
    # "topmostSubform[0].Page1[0].N8ACB[0]": "/Off",
    # "topmostSubform[0].Page1[0].N8ACB[1]": "/Off",
    # "topmostSubform[0].Page1[0].N8BFLD[0]": "",
    # "topmostSubform[0].Page1[0].N9FLD[0]": "",
    # "topmostSubform[0].Page1[0].N12CB[0]": "/Off",
    # "topmostSubform[0].Page1[0].N12CB[1]": "/Off",
    # "topmostSubform[0].Page1[0].N13ACB[0]": "/Off",
    # "topmostSubform[0].Page1[0].N13ACB[1]": "/Off",
    # "topmostSubform[0].Page1[0].N13BFLD[0]": "",
    # "topmostSubform[0].Page1[0].N14ACB[0]": "/Off",
    # "topmostSubform[0].Page1[0].N14ACB[1]": "/Off",
    # "topmostSubform[0].Page1[0].N14BCB[0]": "/Off",
    # "topmostSubform[0].Page1[0].N14BFLD1[0]": "",
    # "topmostSubform[0].Page1[0].N14BFLD2[0]": "1999",
    # "topmostSubform[0].Page1[0].N14CCB[0]": "/Off",
    # "topmostSubform[0].Page1[0].N14CFLD1[0]": "10",
    # "topmostSubform[0].Page1[0].N14CFLD2[0]": "1900",

}
def set_need_appearances_writer(writer: PdfWriter):
    # See 12.7.2 and 7.7.2 for more information: http://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/PDF32000_2008.pdf
    try:
        catalog = writer._root_object
        # get the AcroForm tree
        if "/AcroForm" not in catalog:
            writer._root_object.update({
                NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)
            })

        need_appearances = NameObject("/NeedAppearances")
        writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
        # del writer._root_object["/AcroForm"]['NeedAppearances']
        return writer

    except Exception as e:
        print('set_need_appearances_writer() catch : ', repr(e))
        return writer

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)
writer = set_need_appearances_writer(PyPDF2.PdfWriter())
# writer = PyPDF2.PdfWriter()
# Get the first page of the PDF file
# page = pdf_reader.getPage(0)
page = pdf_reader.pages[0]


# Get the form fields on the page
form = page['/Annots']

# reader = PdfReader("form.pdf")
fields = pdf_reader.get_form_text_fields()
pprint(fields)

# Loop through the form fields and print their values
# for field in form:
#     if isinstance(field, PyPDF2.generic.IndirectObject):
#         field = field.get_object()
#     field_type = field.get('/FT', '')
    
#     # if field_type == '/Tx':  # Check if it is a text field
#         # if '/V' in field:
#         #     pprint(field)
#         #     field_name = field.get('/T', '')
#         #     field_value = field.get('/V', '')
#         #     if field_name in form_dict:
#         #         field.update({'/V': form_dict[field_name]})
#         #         print(f"{field_name}: {field_value} --> {form_dict[field_name]} ")
#         #         pprint(field)
#     #     else:
#     #         print(f"{field_name}: {field_value}")
#     # elif field_type == '/Btn':  # Button field
#     #     field_name = field.get('/T', '')
#     #     field_value = field.get('/V', '')
#         # print(f"{field_name}: {field_value}")
    
writer.add_page(page)
writer.update_page_form_field_values(page, form_dict)
with open("newfile.pdf","wb") as new:
    writer.write(new)

# Close the PDF file
pdf_file.close()



# # Create a PDF writer object
# pdf_writer = PyPDF2.PdfWriter()

# # Get the page containing the form field
# page = pdf_reader.pages[0]

# # Get the form field you want to update
# form_field_name = 'topmostSubform[0].Page1[0].N1FLD[0]'
# form_field = pdf_reader.get_fi(form_field_name)

# # Set the value of the form field
# form_field.update('/V', 'New Value')

# # Add the updated page to the PDF writer object
# pdf_writer.addPage(page)

# # Update the form field values in the PDF writer object
# pdf_writer.updatePageFormFieldValues(page, fields=form_field)

# # Write the updated PDF to a new file
# with open('output.pdf', 'wb') as output_file:
#     pdf_writer.write(output_file)
    
# # Close the input and output files
# pdf_file.close()
# output_file.close()

