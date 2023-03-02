import os
import shutil
from fpdf import FPDF
import json
import base64
from PIL import Image

pdf = FPDF(unit='mm', format='A4')
class PDF(FPDF):
    def chapter_body(self, name):
        directory = f"Foto"
        os.mkdir(directory)
        f = open(name, "r", encoding="utf-8")
        data = json.load(f)
        #self.add_font("Arial", "", "arial.ttf", uni=True)
        self.set_font('Arial', 'B', 6)
        for i in range(len(data)):
            text = data[str(i)]['domanda'].replace("\n\n\n\n","\n")
            text = text.encode('latin-1', 'replace').decode('latin-1')
            self.set_fill_color(211,211,211)
            self.multi_cell(0, 5, f"{i+1}) {text}", fill=True)
            #self.ln()
            if "domanda-immagine" in data[str(i)]: 
                img = base64.decodebytes(data[str(i)]['domanda-immagine'].encode('utf-8'))
                file_name = f"Foto/answer_{i}.png"
                with open(file_name, "wb") as file:
                    file.write(img)
                self.multi_cell(0, 5, "Immagine")

            scelte_temp = []
            
            scelte_foto = f"Scelte"
            os.mkdir(scelte_foto)
            for numero,scelta in enumerate(data[str(i)]['scelte']):
                if len(scelta) > 1500:
                    img = base64.decodebytes(scelta.encode('utf-8'))
                    file_name = f"Scelte/scelta_{numero}.png"
                    with open(file_name, "wb") as file:
                        file.write(img)
                    #self.image(file_name)
                    self.multi_cell(0, 5, "Immagine")
                    #self.ln()
                else:
                    temp = scelta[3:].lstrip()
                    temp = temp.replace("\n","")
                    scelte_temp.append(temp)
                    text = scelta.replace("\n","")
                    text = text.encode('latin-1', 'replace').decode('latin-1')
                    self.multi_cell(0, 5, f"{text}")
            shutil.rmtree(scelte_foto)
            if "risposta-immagine" in data[str(i)]: 
                self.set_fill_color(144,238,144)
                self.multi_cell(0, 5, "Risposta: Immagine",fill=True)
            if "risposta" in data[str(i)]:
                self.set_fill_color(144,238,144)
                text = data[str(i)]['risposta'].replace("The correct answer is: ","")
                text = text.replace("\n","")
                text = text.encode('latin-1', 'replace').decode('latin-1')
                if len(text) > 1500:
                    continue
                #self.multi_cell(0, 5, f"{text}",fill=True)
                for numero,question in enumerate(scelte_temp):
                    if question == text:
                        self.multi_cell(0, 5, f"Risposta : {numero+1}",fill=True)
        shutil.rmtree(directory)
    def print_chapter(self):
        self.add_page()
        #file_name = "/Users/lucian/Documents/GitHub/ExamScraper/01:56:51" + "/" + file
        for file in os.listdir("/Users/lucian/Documents/GitHub/ExamScraper/test"):
            if file.endswith(".json"):
                file_name = "/Users/lucian/Documents/GitHub/ExamScraper/test" + "/" + file
                self.chapter_body(file_name)
                print(f"Added {file}")
pdf = PDF()
pdf.print_chapter()
pdf.output('/Users/lucian/Documents/GitHub/ExamScraper/questions.pdf', 'F')