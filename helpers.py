import csv

# Functie care permite memorarea datelor de contact
# intr-un ficiser .csv
def write_to_contactCSV(data):
    with open("contact.csv", mode="a", newline="") as contact:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        
        # precizam campurile folosite
        # fieldnames seteaza ordinea de scriere in .csv
        fieldnames = ['email', 'subject', 'message']
        csv_writer = csv.DictWriter(contact, fieldnames=fieldnames)
        
        # construim header-ul fisierului .csv o singura data
        if contact.tell() == 0:
            csv_writer.writeheader()
        
        # scriem fiecare rand in fisierul .csv
        csv_writer.writerow({
            'email' : email,
            'subject' : subject,
            'message' : message
        })
