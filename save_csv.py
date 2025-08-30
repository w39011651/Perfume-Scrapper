import csv
from utils import log

def save_to_csv(notes_data):
    with open("perfumes.csv", 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['名稱', '前調', '中調', '後調'])
        for product, product_notes in notes_data.items():
            row = [product, product_notes[0], product_notes[1], product_notes[2]]
            writer.writerow(row)
        log("Save data done.")
        
