import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import json

def lookup_carrier(phone_number):
    try:
        # Parse nomor telepon
        parsed_number = phonenumbers.parse(phone_number, None)
        
        # Ambil informasi dari nomor telepon
        phone_info = {
            "International Format": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
            "E164 Format": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164),
            "Country Code": parsed_number.country_code,
            "National Number": parsed_number.national_number,
            "Location": geocoder.description_for_number(parsed_number, "id"),  # Lokasi dalam bahasa Indonesia
            "Timezone": ', '.join(timezone.time_zones_for_number(parsed_number)),
            "Carrier": carrier.name_for_number(parsed_number, "en"),  # Nama operator
            "Valid Number": phonenumbers.is_valid_number(parsed_number),
            "Possible Number": phonenumbers.is_possible_number(parsed_number)
        }
        
        # Mengonversi informasi ke format JSON untuk tampilan yang lebih baik
        return json.dumps(phone_info, indent=4)
    except phonenumbers.NumberParseException as e:
        return json.dumps({"error": str(e)}, indent=4)

def main():
    print("=== Tool Cek Carrier Phone ===")
    phone_number = input("Masukkan nomor telepon (dengan kode negara, misal: +628123456789): ")
    result = lookup_carrier(phone_number)
    print(result)

if __name__ == "__main__":
    main()