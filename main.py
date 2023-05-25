import PyPDF2
import re
import random
import csv

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


def extract_content(all_text):
    start_index = all_text.find("Grundschule")
    end_index = all_text.find("**********", start_index)
    if start_index != -1 and end_index != -1:
        extracted_text = all_text[start_index:end_index].strip()
        return extracted_text
    else:
        return None


def get_random_lines(input_list, num_lines=5):
    random_lines = random.sample(input_list, num_lines)
    return random_lines


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

        # Add a blank line before "Grundschule"
        all_text = re.sub(r'Grundschule', f'\nGrundschule\n', all_text)

        # Add a blank line with "**********" before "Bezirksregierung"
        all_text = re.sub(r'Bezirksregierung', r'**********\nBezirksregierung', all_text)

        # Add a blank line before "Kreis"
        all_text = re.sub(r'Kreis', f'Kreis\n', all_text)

        # Add a blank line before "Stadt"
        all_text = re.sub(r'Stadt', f'Stadt\n', all_text)

        # Add a blank line before each word from german_schools
        for school in german_schools:
            all_text = re.sub(rf'\b{re.escape(school)}\b', f'\n{school}', all_text)

            # Add a blank line with "**********" before "Grundschule"
            all_text = re.sub(r'Grundschule', r'**********\nGrundschule', all_text)

            # Add a blank line with "**********" before "Gymnasium"
            all_text = re.sub(r'Gymnasium', r'**********\nGymnasium', all_text)

            # Add a blank line with "**********" before "Gymnasium"
            all_text = re.sub(r'Gesamtschule', r'**********\nGesamtschule', all_text)

            # Add a blank line with "**********" before "Realschule"
            all_text = re.sub(r'Realschule', r'**********\nRealschule', all_text)

            # Add a blank line with "**********" before "Hauptschule"
            all_text = re.sub(r'Hauptschule', r'**********\nHauptschule', all_text)

            # Add a blank line with "&&&" before "Sekundarschule"
            all_text = re.sub(r'Sekundarschule', r'**********\nSekundarschule', all_text)

            # Extract the desired content
            extracted_text = extract_content(all_text)

            # Add a blank line before "Bezirksregierung"
            extracted_text = re.sub(r'Bezirksregierung', f'\nBezirksregierung', all_text)

            # Extract relevant information
            pattern = r"(?s)(?<=Gymnasium).*?(?=\*{10})"
            relevant_info_Gymnasium = re.findall(pattern, extracted_text)

            # Extract relevant information
            pattern = r"(?s)(?<=Gesamtschule).*?(?=\*{10})"
            relevant_info_Gesamtschule = re.findall(pattern, extracted_text)

            # Extract relevant information
            pattern = r"(?s)(?<=Realschule).*?(?=\*{10})"
            relevant_info_Realschule = re.findall(pattern, extracted_text)

            # Extract relevant information
            pattern = r"(?s)(?<=Hauptschule).*?(?=\*{10})"
            relevant_info_Hauptschule = re.findall(pattern, extracted_text)

            # Extract relevant information
            pattern = r"(?s)(?<=Sekundarschule).*?(?=\*{10})"
            relevant_info_Sekundarschule = re.findall(pattern, extracted_text)

    for info in relevant_info_Gymnasium:
        relevant_info_Gymnasium_list = [info.strip() for info in relevant_info_Gymnasium]

        GymCSV_path = r'C:\Users\Jan\Documents\Projekte\SchulenNRW\CSV\Gymnasium.csv'
        with open(GymCSV_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(relevant_info_Gymnasium_list)
            csvfile.close()

    for info in relevant_info_Gesamtschule:
        relevant_info_Gesamtschule_list = [info.strip() for info in relevant_info_Gesamtschule]

        GymCSV_path = r'C:\Users\Jan\Documents\Projekte\SchulenNRW\CSV\Gesamtschule.csv'
        with open(GymCSV_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(relevant_info_Gesamtschule_list)
            csvfile.close()

    for info in relevant_info_Realschule:
        relevant_info_Realschule_list = [info.strip() for info in relevant_info_Realschule]

        GymCSV_path = r'C:\Users\Jan\Documents\Projekte\SchulenNRW\CSV\Realschule.csv'
        with open(GymCSV_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(relevant_info_Realschule_list)
            csvfile.close()

    for info in relevant_info_Hauptschule:
        relevant_info_Hauptschule_list = [info.strip() for info in relevant_info_Hauptschule]

        GymCSV_path = r'C:\Users\Jan\Documents\Projekte\SchulenNRW\CSV\Hauptschule.csv'
        with open(GymCSV_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(relevant_info_Hauptschule_list)
            csvfile.close()

    for info in relevant_info_Sekundarschule:
        relevant_info_Sekundarschule_list = [info.strip() for info in relevant_info_Sekundarschule]

        GymCSV_path = r'C:\Users\Jan\Documents\Projekte\SchulenNRW\CSV\Sekundarschule.csv'
        with open(GymCSV_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(relevant_info_Sekundarschule_list)
            csvfile.close()
