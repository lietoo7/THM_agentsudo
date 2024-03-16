from PIL import Image
import sys

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = image.info.get("text", "")
        return text
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Utilisation: python script.py <chemin_de_l'image>")
        sys.exit(1)

    image_path = sys.argv[1]
    extracted_text = extract_text_from_image(image_path)

    if extracted_text:
        print("Texte extrait de l'image :")
        print(extracted_text)
    else:
        print("Aucun texte dissimulé trouvé dans l'image.")
