import fitz
import os
from datetime import datetime, date

class GerarPDf:

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, aluno):
        self.aluno = aluno
        self.PDF_BASE = os.path.join(
            self.BASE_DIR, 
            "modelo",
            "comunicado.pdf"
        )
        self.pdf = fitz.open(self.PDF_BASE)
        self.page = self.pdf[0]
        

        
    def escrever_pdf(self, texto, x, y, tamanho=12, bold=False):
        

        fonte = "helv" if not bold else "helv-bold"
        self.page.insert_text((x, y), texto, fontsize=tamanho, fontname=fonte)


    
    def gerar(self, serie, numero_motivo, professor, disciplina):
        self.escrever_pdf(self.aluno, 139, 222)
        self.escrever_pdf(serie, 139, 247)

        dados_motivo = self.motivo(numero_motivo)

        self.escrever_pdf("(    )", 70, 275)
        self.escrever_pdf("(    )", 70, 300)
        self.escrever_pdf("(    )", 70, 324)
        self.escrever_pdf("(    )", 70, 348)
        self.escrever_pdf("(    )", 70, 382)
        self.escrever_pdf("(    )", 70, 403)
        self.escrever_pdf("(    )", 70, 424)
        self.escrever_pdf("(    )", 70, 448)
        self.escrever_pdf("(    )", 70, 470)

        self.escrever_pdf(dados_motivo["texto"], dados_motivo["x"], dados_motivo["y"])

        self.escrever_pdf(str(date.today().day).zfill(2), 265, 652)
        self.escrever_pdf(self.meses_ano(date.today().month), 340, 652)
        self.escrever_pdf(str(date.today().year), 450, 652)

        self.escrever_pdf(professor, 235, 709)
        self.escrever_pdf(disciplina, 252, 738)


        output = os.path.join(self.BASE_DIR,  f"comunicado_disciplinar - {self.aluno}.pdf")
        self.pdf.save(output)
        self.pdf.close()

        return output


    def motivo(self, motivo):
        match motivo:
            case "1":
                x, y = 70, 275.0
            case "2":
                x, y = 70, 300.0
            case "3":
                x, y = 70, 324.0                
            case "4":
                x, y = 70, 348.0
            case "5":
                x, y = 70, 382.0
            case "6":
                x, y = 70, 403.0
            case "7":
                x, y = 70, 424.0
            case "8":
                x, y = 70, 448.0
            case "9":
                x, y = 70, 470.2
            
        return  {"texto": "( X ", "x": x, "y": y}
    
    def meses_ano(self, mes):
        meses = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
                5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto", 9: "Setembro",
                10: "Outubro", 11: "Novembro", 12: "Dezembro"}
        return meses.get(mes)