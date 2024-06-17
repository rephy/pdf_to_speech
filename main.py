import base64
from requests import get
from pypdf import PdfReader

resume_path = "/Users/rephy/Work/Resume:CV/Raphael Manayon's Resume/Resume.pdf"

reader = PdfReader(resume_path)

for n in range(len(reader.pages)):
    page = reader.pages[n]
    page_name = f'page{n + 1}'
    pdf_text = page.extract_text()

    pdf_text = pdf_text.strip()
    pdf_text = pdf_text.replace("●", "")
    pdf_text = pdf_text.replace("’", "'")
    pdf_text = pdf_text.replace("ﬁ", "fi")
    pdf_text = pdf_text.replace("ﬀ", "ff")
    pdf_text = pdf_text.replace("ﬃ", "ffi")
    pdf_text = pdf_text.replace("\n", " ")

    print(pdf_text)

    ttsAPI_endpoint = "https://api.voicerss.org/"
    ttsAPI_params = {
        'key': 'dd888f9e94cc4e64943d55ae731e64a7',
        'hl': 'en-us',
        'v': 'John',
        'c': 'MP3',
        'b64': 'true',
        'src': pdf_text
    }

    response = get(ttsAPI_endpoint, ttsAPI_params)
    response.raise_for_status()

    b64_string = response.text

    audio_file = open(f"{page_name}.mp3", "wb")

    decoded_string = base64.b64decode(b64_string)
    audio_file.write(decoded_string)

    audio_file.close()