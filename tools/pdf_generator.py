import os
import shutil
from fpdf import FPDF
import json
import base64
from PIL import Image

pdf = FPDF(unit='mm', format='A4')
class PDF(FPDF):
    def box_text(self, text):
        # Set the font and font size
        self.set_font('Arial', 'B', 12)
        
        # Set the background color and line color of the box
        self.set_fill_color(220, 220, 220)
        self.set_draw_color(0, 0, 0)
        
        # Calculate the width and height of the box based on the length of the text
        text_width = self.get_string_width(text) + 6
        text_lines = self.multi_cell(text_width, 5, text)
        text_height = self.get_y() - self.font_size_pt / 2 - self.b_margin
        
        # Draw the box
        self.rect(self.l_margin, self.get_y() - text_height, text_width, text_height, 'FD')
        
        # Move to the next line
        self.ln()
        
        # Return the number of lines written
        return text_lines

    def chapter_body(self, name):
        directory = f"Foto"
        os.mkdir(directory)
        f = open(name, "r", encoding="utf-8")
        data = json.load(f)
        #self.add_font("Arial", "", "arial.ttf", uni=True)
        self.set_font('Arial', 'B', 5)
        for i in range(len(data)):
            text = data[str(i)]['domanda'].replace("\n\n\n\n","\n")
            text = text.encode('latin-1', 'replace').decode('latin-1')
            self.set_fill_color(211,211,211)
            self.multi_cell(0, 5, f"{i+1}) {text}", fill=True)
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
        self.ln()
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
pdf.output('/Users/lucian/Documents/GitHub/ExamScraper/test.pdf', 'F')