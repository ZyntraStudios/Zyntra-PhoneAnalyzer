import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from phonenumbers.phonenumberutil import NumberParseException

def analizar_numero_telefono(numero_str, pais_defecto):
    """
    Analiza un número de teléfono y extrae toda la información posible
    sin necesidad de APIs externas.
    """
    try:
        numero_parseado = phonenumbers.parse(numero_str, pais_defecto.upper())

        print("\n--- Análisis del Número de Teléfono ---")

        es_posible = phonenumbers.is_possible_number(numero_parseado)
        es_valido = phonenumbers.is_valid_number(numero_parseado)

        print(f"¿Es un número posible?: {'Sí' if es_posible else 'No'}")
        print(f"¿Es un número válido?: {'Sí' if es_valido else 'No'}")

        if not es_valido:
            print("\nEl número no es válido. No se puede continuar con el análisis.")
            return

        formato_e164 = phonenumbers.format_number(numero_parseado, phonenumbers.PhoneNumberFormat.E164)
        formato_internacional = phonenumbers.format_number(numero_parseado, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        formato_nacional = phonenumbers.format_number(numero_parseado, phonenumbers.PhoneNumberFormat.NATIONAL)
        formato_rfc3966 = phonenumbers.format_number(numero_parseado, phonenumbers.PhoneNumberFormat.RFC3966)

        print("\n--- Formatos del Número ---")
        print(f"E.164: {formato_e164}")
        print(f"Internacional: {formato_internacional}")
        print(f"Nacional: {formato_nacional}")
        print(f"RFC3966: {formato_rfc3966}")

        pais_codigo = geocoder.region_code_for_number(numero_parseado)
        pais_nombre = geocoder.country_name_for_number(numero_parseado, "es")
        ubicacion = geocoder.description_for_number(numero_parseado, "es")
        operadora = carrier.name_for_number(numero_parseado, "es")

        print("\n--- Información de Ubicación y Operadora ---")
        print(f"Código de País: {pais_codigo}")
        print(f"País: {pais_nombre}")
        print(f"Ubicación Geográfica (Ciudad/Región): {ubicacion}")
        print(f"Operadora (Carrier): {operadora}")

        zonas_horarias = timezone.time_zones_for_number(numero_parseado)
        print("\n--- Zona Horaria ---")
        print(f"Zona(s) Horaria(s): {', '.join(zonas_horarias)}")

        print("\n--- Desglose del Número ---")
        print(f"Prefijo Internacional: +{numero_parseado.country_code}")
        print(f"Prefijo Nacional (Área): {numero_parseado.national_number}")

    except NumberParseException as e:
        print(f"Error: El número de teléfono introducido no es válido o no se pudo parsear. Detalles: {e}")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")

if __name__ == "__main__":
    # Inputs configurables por el usuario
    color_verde = "\033[92m"
    color_reset = "\033[0m"
    print(color_verde + r"""
███████╗██╗   ██╗███╗   ██╗████████╗██████╗  █████╗ 
╚══███╔╝╚██╗ ██╔╝████╗  ██║╚══██╔══╝██╔══██╗██╔══██╗
  ███╔╝  ╚████╔╝ ██╔██╗ ██║   ██║   ██████╔╝███████║
 ███╔╝    ╚██╔╝  ██║╚██╗██║   ██║   ██╔══██╗██╔══██║
███████╗   ██║   ██║ ╚████║   ██║   ██║  ██║██║  ██║
╚══════╝   ╚═╝   ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝
""" + color_reset)    
    
    print("Configuración inicial (puedes dejar vacío para valores por defecto).")

    numero_telefono = input("Introduce el número de teléfono (ej: +34600112233 o 600112233): ").strip()
    pais_defecto = input("Introduce el código de país por defecto (ej: ES, US, MX) [default: ES]: ").strip() or "ES"

    analizar_numero_telefono(numero_telefono, pais_defecto)