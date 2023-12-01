import csv

try:
    with open('sk.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)

        with open('cities.csv', 'w', newline='', encoding='utf-8') as output_file:
            csv_writer = csv.writer(output_file)

            for row in csv_reader:
                if row:  # Provjerite da li red ima podataka
                    # Izvadite podatak do prvog zareza u redu
                    first_comma_index = row[0].find(',')
                    data_before_first_comma = row[0][:first_comma_index] if first_comma_index != -1 else row[0]

                    # Ispišite podatak u novu CSV datoteku
                    csv_writer.writerow([data_before_first_comma])

except UnicodeDecodeError as e:
    print(f"Greška pri dekodiranju: {e}")



with open('people-1000.csv', 'r', newline='', encoding='utf-8') as people_file:
    people_reader = csv.reader(people_file)
    for index, row in enumerate(people_reader):
        if index < 20:
            name = row[2]
            last_name = row[3]
            part_email = row[5].split('@')[0]  # part of email
            print(f"Name: {name}, Last Name: {last_name}, Email: {part_email}")