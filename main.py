import PyPDF2
import re
import random


german_circle = [
    'BR Arnsberg',
    'BR Detmold',
    'BR Düsseldorf',
    'BR Köln',
    'BR Münster'
]

german_schools = [
    'Hauptschule',
    'Realschule',
    'Gesamtschule',
    'Gymnasium',
    'Sekundarschule',
]

german_cities = [
    'Cologne',
    'Düsseldorf',
    'Dortmund',
    'Essen',
    'Duisburg',
    'Bochum',
    'Wuppertal',
    'Bielefeld',
    'Bonn',
    'Münster',
    'Gelsenkirchen',
    'Mönchengladbach',
    'Aachen',
    'Krefeld',
    'Oberhausen',
    'Hagen',
    'Hamm',
    'Herne',
    'Mülheim an der Ruhr',
    'Leverkusen',
    'Solingen',
    'Neuss',
    'Paderborn',
    'Bottrop',
    'Recklinghausen',
    'Bergisch Gladbach',
    'Remscheid',
    'Moers',
    'Siegen',
    'Gütersloh',
    'Witten',
    'Iserlohn',
    'Lünen',
    'Marl',
    'Herford',
    'Ratingen',
    'Castrop-Rauxel',
    'Lüdenscheid',
    'Velbert',
    'Dorsten',
    'Arnsberg',
    'Gladbeck',
    'Bocholt',
    'Lippstadt',
    'Düren',
    'Kerpen',
    'Unna',
    'Dormagen',
    'Grevenbroich',
    'Herten',
    'Bergheim',
    'Euskirchen',
    'Langenfeld (Rheinland)',
    'Ibbenbüren',
    'Hattingen',
    'Sankt Augustin',
    'Ahlen',
    'Pulheim',
    'Eschweiler',
    'Bad Salzuflen',
    'Hürth',
    'Kamen',
    'Erftstadt',
    'Goch',
    'Gronau (Westf.)',
    'Wesel',
    'Datteln',
    'Meerbusch',
    'Emsdetten',
    'Löhne',
    'Kleve',
    'Bornheim',
    'Warendorf',
    'Rheda-Wiedenbrück',
    'Königswinter',
    'Emmerich am Rhein',
    'Rheine',
    'Porta Westfalica',
    'Nordhorn',
    'Bünde',
    'Borken',
    'Ahaus',
    'Detmold',
    'Höxter',
    'Oelde',
    'Wülfrath',
    'Lage',
    'Heinsberg',
    'Würselen',
    'Schwerte',
    'Attendorn',
    'Geldern',
    'Lennestadt',
    'Nettetal',
    'Sprockhövel',
    'Rietberg',
    'Coesfeld',
    'Jülich',
    'Xanten',
    'Beckum',
    'Greven',
    'Steinfurt',
    'Lohmar',
    'Schloß Holte-Stukenbrock',
    'Mettmann',
    'Ennepetal',
    'Wermelskirchen',
    'Werl',
    'Wegberg',
    'Oer-Erkenschwick',
    'Harsewinkel',
    'Rheinberg',
    'Haltern am See',
    'Stolberg (Rheinland)',
    'Gescher',
    'Leichlingen (Rheinland)',
    'Schwelm',
    'Erkelenz',
    'Alfter',
    'Oerlinghausen',
    'Bad Oeynhausen',
    'Senden',
    'Meckenheim',
    'Fröndenberg/Ruhr',
    'Hamminkeln',
    'Bad Honnef',
    'Rheinbach',
    'Lemgo',
    'Lengerich',
    'Heiligenhaus',
    'Neukirchen-Vluyn',
    'Leopoldshöhe',
    'Lübbecke',
    'Werther (Westf.)',
    'Warstein',
    'Hückelhoven',
    'Meinerzhagen',
    'Niederkassel',
    'Bedburg',
    'Rheinwald',
    'Wesseling',
    'Schmallenberg',
    'Sundern (Sauerland)',
    'Netphen',
    'Vreden',
    'Geilenkirchen',
    'Selm',
    'Hövelhof',
    'Langenberg',
    'Neheim-Hüsten',
    'Olpe',
    'Kempen',
    'Waltrop',
    'Eschborn',
    'Hille',
    'Espelkamp',
    'Hörstel',
    'Olfen',
    'Salzkotten',
    'Marienheide',
    'Wiehl',
    'Niederzier',
     'Altena'
]

def extract_content(text):
    pattern = r'Grundschule(.*?)\$\$\$|§§§|!!!|%%%|&&&|\*\*\*\*\*\*\*\*\*\*'
    extracted_text = re.sub(pattern, '', text, flags=re.DOTALL)
    extracted_text = re.sub(r'\n+', '\n', extracted_text)  # Remove multiple consecutive newlines
    extracted_text = extracted_text.strip()  # Remove leading/trailing whitespace
    return extracted_text

pdf_path = 'C:/Users/Jan/Documents/Projekte/SchulenNRW/sozialindexstufen_der_einzelschulen.pdf'

# Open the PDF file
with open(pdf_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Extract text from each page
    all_text = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        all_text += page.extract_text()

        # Add a blank line before "Bezirksregierung"
        all_text = re.sub(r'Bezirksregierung', f'\nBezirksregierung', all_text)

        # Add a blank line with "**********" before "Bezirksregierung"
        all_text = re.sub(r'Bezirksregierung', r'**********\nBezirksregierung', all_text)

        # Add a blank line before "Kreis"
        all_text = re.sub(r'Kreis', f'Kreis\n', all_text)

        # Add a blank line before "Stadt"
        all_text = re.sub(r'Stadt', f'Stadt\n', all_text)

        # Add a blank line before each word from german_schools
        for school in german_schools:
            all_text = re.sub(rf'\b{re.escape(school)}\b', f'\n{school}', all_text)

            # Add a blank line with "$$$" before "Gymnasium"
            all_text = re.sub(r'Gymnasium', r'$$$\nGymnasium', all_text)

            # Add a blank line with "§§§" before "Gesamtschule"
            all_text = re.sub(r'Gesamtschule', r'§§§\nGesamtschule', all_text)

            # Add a blank line with "!!!" before "Realschule"
            all_text = re.sub(r'Realschule', r'!!!\nRealschule', all_text)

            # Add a blank line with "%%%" before "Hauptschule"
            all_text = re.sub(r'Hauptschule', r'%%%\nHauptschule', all_text)

            # Add a blank line with "&&&" before "Sekundarschule"
            all_text = re.sub(r'Sekundarschule', r'&&&\nSekundarschule', all_text)

            # Extract the desired content
            extracted_text = extract_content(all_text)

            # Add a blank line before "Bezirksregierung"
            extracted_text = re.sub(r'Bezirksregierung', f'\nBezirksregierung', all_text)


    print(extracted_text)

