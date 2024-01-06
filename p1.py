import requests
from bs4 import BeautifulSoup
import csv
import re

def scrape_flipkart_mobiles(query, num_pages=10):
    base_url = "https://www.flipkart.com"

    all_mobiles = []

    for page in range(1, num_pages + 1):
        search_url = f"{base_url}/search?q={query}&page={page}"

        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        mobiles = []
        for product_card in soup.find_all('div', {'class': '_1AtVbE'}):
            name = product_card.find('div', {'class': '_4rR01T'})
            price = product_card.find('div', {'class': '_30jeq3'})
            ratings = product_card.find('div', {'class': '_3LWZlK'})
            features_list = product_card.find_all('li', {'class': 'rgWa7D'})

            if name:
                original_name = name.text

                color_ram_match = re.search(r'\(([^,]+), ([^)]+)\)', original_name)
                color = color_ram_match.group(1) if color_ram_match else None
                ram = color_ram_match.group(2) if color_ram_match else None
                name = re.sub(r'\([^)]*\)', '', original_name).strip()

                price_text = price.text if price else None

                if price_text:
                    currency_type = ""

                    currency_symbols = {'₹': 'Rupees', '$': 'Dollars', '€': 'Euros', '£': 'Pounds', '¥': 'Yen'}
                    for symbol, text in currency_symbols.items():
                        if symbol in price_text:
                            currency_type = text
                            price_text = price_text.replace(symbol, '')
                            break

                    numeric_value = re.sub(r'[^0-9.]', '', price_text)
                else:
                    currency_type = None
                    numeric_value = None

                ratings = ratings.text if ratings else None

                features = [feature.text for feature in features_list]

                rom = features[0].rstrip('ROM') if features else None
                display_info = features[1] if len(features) > 1 else None
                camera_info = features[2] if len(features) > 2 else None
                processor_info = features[3] if len(features) > 3 else None
                warranty = features[4] if len(features) > 4 and 'Warranty' in features[4] else None

                display_size_match = re.search(r'(\d+\.\d+ cm \(\d+\.\d+ inch\))', display_info) if display_info else None
                display_size = display_size_match.group(1) if display_size_match else None
                display_type = display_info.replace(display_size, '').strip() if display_info and display_size else None

                main_camera_match = re.search(r'([^+|]+)', camera_info) if camera_info else None
                main_camera = main_camera_match.group(1).strip() if main_camera_match else None

                front_camera_match = re.search(r'\|([^|]+)', camera_info) if camera_info else None
                front_camera = front_camera_match.group(1).strip().replace('Front Camera', '') if front_camera_match else None

                processor_chip_match = re.search(r'([^,]+)', processor_info) if processor_info else None
                processor_chip = processor_chip_match.group(1).strip() if processor_chip_match else None

                processor_cores_match = re.search(r'(\d+ Core)', processor_info) if processor_info else None
                processor_cores = processor_cores_match.group(1).strip() if processor_cores_match else None

                mobiles.append({'Name': name, 'Ratings': ratings, 'Color': color, 'RAM': ram, 'ROM': rom, 'Price': numeric_value, 'Currency_Type': currency_type, 'Processor_Chip': processor_chip, 'Processor_Cores': processor_cores, 'Main_Camera': main_camera, 'Front_Camera': front_camera, 'Display_Size': display_size, 'Display_Type': display_type, 'Warranty': warranty})

        all_mobiles.extend(mobiles)

    return all_mobiles

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Ratings', 'Color', 'RAM', 'ROM', 'Price', 'Currency_Type', 'Processor_Chip', 'Processor_Cores', 'Main_Camera', 'Front_Camera', 'Display_Size', 'Display_Type', 'Warranty'])
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    num_pages = 10
    mobile_data = scrape_flipkart_mobiles("iPhone", num_pages)

    if mobile_data:
        csv_filename = f"{'iPhone'}_mobiles.csv"
        save_to_csv(mobile_data, csv_filename)
        print(f"Data successfully scraped and saved to {csv_filename}")
    else:
        print("No data found.")
