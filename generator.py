import os
import shutil
from fpdf import FPDF
import json
import base64
# Create an instance of the FPDF class
pdf = FPDF()

title = 'Archivio domande Ingegneria del Software'

class PDF(FPDF):

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 6)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_body(self, name):
        #directory = f"Foto"
        #os.mkdir(directory)
        f = open(name, "r")
        data = json.load(f)
        self.set_font('Times', '', 9)
        for i in range(len(data)):
            text = data[str(i)]['domanda'].replace("\n\n\n\n","\n")
            self.multi_cell(0, 5, f"{i+1}) {text}")
            self.ln()
            #if "domanda-immagine" in data[str(i)]: 
                #img = base64.decodebytes(data[str(i)]['domanda-immagine'].encode('utf-8'))
                #file_name = f"Foto/answer_{i}.png"
                #with open(file_name, "wb") as file:
                    #file.write(img)
                #self.image(file_name)
                #self.ln()
            for scelta in data[str(i)]['scelte']:
                if len(scelta) > 1000:
                    print(f"Risposta troppo lunga per la domanda")
                    continue
                self.multi_cell(0, 5, f"   {scelta}")
            if "risposta" in data[str(i)]:
                text = data[str(i)]['risposta']
                if len(text) > 1000:
                    print(f"Risposta troppo lunga per la domanda")
                    continue
                self.multi_cell(0, 5, f"Risposta: {text}")
                self.ln()
        #shutil.rmtree(directory)
    def print_chapter(self, file):
        self.add_page()
        self.chapter_body(file)

pdf = PDF()
pdf.set_title(title)
pdf.set_author('Lucian D. Crainic')

pdf.print_chapter('/Users/lucian/Documents/GitHub/ExamScraper/Exam_0.json')
pdf.output('/Users/lucian/Documents/GitHub/ExamScraper/questions.pdf', 'F')