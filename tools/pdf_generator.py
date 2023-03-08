import os
import shutil
from fpdf import FPDF
import json
import base64

pdf = FPDF(unit='mm', format='A4')
class PDF(FPDF):
    def text_images_pdf(self, name):
        f = open(name, "r", encoding="utf-8")
        data = json.load(f)
        self.set_font('Arial', '', 6)

        domanda_immagine = f"Domanda"
        os.mkdir(domanda_immagine)

        for i in range(len(data)):
            if "domanda-immagine" in data[str(i)]:
                text = data[str(i)]['domanda'].replace("\n\n\n\n","\n")
                text = data[str(i)]['domanda'].replace("\n\n","")
                text = text.encode('latin-1', 'replace').decode('latin-1')
                self.set_fill_color(211,211,211)
                self.multi_cell(0, 5, f"{text}", fill=True)
                img = base64.decodebytes(data[str(i)]['domanda-immagine'].encode('utf-8'))
                file_name = f"Domanda/question_{i}.png"
                with open(file_name, "wb") as file:
                    file.write(img)
                self.image(file_name)
            else:
                continue
            
            scelte_temp = []
            
            scelte_immagine = f"Scelte"
            os.mkdir(scelte_immagine)
            for numero,scelta in enumerate(data[str(i)]['scelte']):
                if len(scelta) > 1500:
                    scelte_temp.append(scelta)
                    img = base64.decodebytes(scelta.encode('utf-8'))
                    file_name = f"Scelte/choice_{numero}.png"
                    with open(file_name, "wb") as file:
                        file.write(img)
                    self.image(file_name)
                else:
                    temp = scelta[3:].lstrip()
                    temp = temp.replace("\n","")
                    scelte_temp.append(temp)
                    text = scelta.replace("\n","")
                    text = text.encode('latin-1', 'replace').decode('latin-1')
                    self.multi_cell(0, 5, f"{text}")
            shutil.rmtree(scelte_immagine)
            if "risposta-immagine" in data[str(i)]:
                text = data[str(i)]['risposta-immagine']
                for numero,question in enumerate(scelte_temp):
                    if question == text:
                        self.multi_cell(0, 5, f"Risposta : {numero+1}",fill=True)
            else:
                self.set_fill_color(144,238,144)
                text = data[str(i)]['risposta'].replace("The correct answer is: ","")
                text = text.replace("\n","")
                text = text.encode('latin-1', 'replace').decode('latin-1')
                for numero,question in enumerate(scelte_temp):
                    if question == text:
                        self.multi_cell(0, 5, f"Risposta : {numero+1}",fill=True)
        shutil.rmtree(domanda_immagine)
    def text_only_pdf(self, name):
        directory = f"Foto"
        os.mkdir(directory)
        f = open(name, "r", encoding="utf-8")
        data = json.load(f)
        self.set_font('Arial', '', 6)
        for i in range(len(data)):
            
            if "domanda-immagine" in data[str(i)]:
                continue
            
            text = data[str(i)]['domanda'].replace("\n\n\n\n","\n")
            text = text.encode('latin-1', 'replace').decode('latin-1')
            self.set_fill_color(211,211,211)
            self.multi_cell(0, 5, f"{text}", fill=True)
            
            scelte_temp = []
            
            for numero,scelta in enumerate(data[str(i)]['scelte']):
                if len(scelta) > 1500:
                    continue
                else:
                    temp = scelta[3:].lstrip()
                    temp = temp.replace("\n","")
                    scelte_temp.append(temp)
                    text = scelta.replace("\n","")
                    text = text.encode('latin-1', 'replace').decode('latin-1')
                    self.multi_cell(0, 5, f"{text}")

            if "risposta-immagine" in data[str(i)]: 
                continue
            if "risposta" in data[str(i)]:
                self.set_fill_color(144,238,144)
                text = data[str(i)]['risposta'].replace("The correct answer is: ","")
                text = text.replace("\n","")
                text = text.encode('latin-1', 'replace').decode('latin-1')
                for numero,question in enumerate(scelte_temp):
                    if question == text:
                        self.multi_cell(0, 5, f"Risposta : {numero+1}",fill=True)
        shutil.rmtree(directory)

    def print_text_pdf(self):
        self.add_page()
        for file in os.listdir("/Users/lucian/Documents/GitHub/ExamScraper/exams_data"):
            if file.endswith(".json"):
                file_name = "/Users/lucian/Documents/GitHub/ExamScraper/exams_data" + "/" + file
                self.text_only_pdf(file_name)
                print(f"Added {file}")
    def print_text_images_pdf(self):
        self.add_page()
        for file in os.listdir("/Users/lucian/Documents/GitHub/ExamScraper/exams_data"):
            if file.endswith(".json"):
                file_name = "/Users/lucian/Documents/GitHub/ExamScraper/exams_data" + "/" + file
                self.text_images_pdf(file_name)
                print(f"Added {file}")
pdf = PDF()
#pdf.print_text_pdf()
#pdf.output('/Users/lucian/Documents/GitHub/ExamScraper/domande_testo.pdf', 'F')

pdf.print_text_images_pdf()
pdf.output('/Users/lucian/Documents/GitHub/ExamScraper/domande_testo_immagini.pdf', 'F')