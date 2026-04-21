# Set Password for PDF file using pikepdf library in Python
# Password: 123abc

import pikepdf

old_pdf = pikepdf.Pdf.open("resume.pdf")

no_extract_pdf = pikepdf.Permissions(extract=False)

old_pdf.save("resume_password.pdf", encryption=pikepdf.Encryption(owner="Ashish", user="123abc", allow=no_extract_pdf))

print("Password set successfully for the PDF file.")    



# To freeze requirements.txt file, use the following command in the terminal:
# pip freeze > requirements.txt