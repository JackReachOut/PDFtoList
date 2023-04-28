import requests
from PyPDF2 import PdfReader

# Download the PDF file from the URL
url = 'https://www.schulministerium.nrw/system/files/media/document/file/sozialindexstufen_der_einzelschulen.pdf'
response = requests.get(url)

# Open the downloaded PDF file
pdf_file = open('sozialindexstufen_der_einzelschulen.pdf', 'wb')
pdf_file.write(response.content)
pdf_file.close()
pdf_file = open('sozialindexstufen_der_einzelschulen.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PdfReader(pdf_file)

# Get the number of pages in the PDF file
num_pages = len(pdf_reader.pages)

# Initialize an empty list to store the data
data = []

# Loop through each page in the PDF file
for page in range(num_pages):

    # Get the current page object
    pdf_page = pdf_reader.pages[page]

    # Extract the text from the page
    page_text = pdf_page.extract_text()

    # Split the text into lines
    lines = page_text.split('\n')

    # Loop through each line in the page
    for line in lines:

        # Split the line into cells
        cells = line.split()

        # Check if the line has cells
        if cells:

            # Append the cells to the data list
            data.append(cells)

# Print the data as a 2D array
for row in data:
    print(row)

import random

