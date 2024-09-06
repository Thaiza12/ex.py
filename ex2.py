class CalculaNota:
    def __init__(self, matricula,nota1, nota2,trabalho, faltas):
        self.matricula=matricula
        self.nota1=nota1
        self.nota2=nota2
        self.trabalho=trabalho
        self.faltas = faltas 

    def calcular_media(self):

        """Calcula a média aritmética das notas"""
        media = (self.nota1 + self.nota2) / 2
        media += self.trabalho

        if(media >= 7 and self.faltas < 11):
            return f"Aluno Aprovado. Média do aluno {self.matricula}: {media:2f} nota do trabalho: {self.trabalho}"
        else:
            return f"Aluno reprovado. Média do aluno {self.matricula}: {media:2f} nota do trabalho: {self.trabalho}"







    def consultar_nota(self):
        """Consulta as notas individuais do aluno"""
        return{
            "matricula": self.matricula,
            "nota1": self.nota1,
            "nota2": self.nota2,
            "trabalho": self.trabalho,
            "faltas":self.faltas
        }

#Exemplo de uso

aluno_nota1 = CalculaNota(matricula=12345, nota1=-7.5, nota2=8.0, trabalho=1, faltas=2)
aluno_nota2 = CalculaNota(matricula=12346, nota1=8.5, nota2=8.0, trabalho=1, faltas=2)
aluno_nota3 = CalculaNota(matricula=12347, nota1=9.5, nota2=8.0, trabalho=3, faltas=2)
aluno_nota4 = CalculaNota(matricula=12348, nota1=1.5, nota2=8.0, trabalho=4, faltas=2)
aluno_nota5 = CalculaNota(matricula=12349, nota1=2.5, nota2=8.0, trabalho=5, faltas=2)
aluno_nota6 = CalculaNota(matricula=12350, nota1=3.5, nota2=8.0, trabalho=6, faltas=2)
aluno_nota7 = CalculaNota(matricula=12351, nota1=4.5, nota2=8.0, trabalho=7, faltas=2)
aluno_nota8 = CalculaNota(matricula=12352, nota1=5.5, nota2=8.0, trabalho=8, faltas=2)
aluno_nota9 = CalculaNota(matricula=12353, nota1=6.5, nota2=8.0, trabalho=9, faltas=2)
aluno_nota10 = CalculaNota(matricula=12354, nota1=7.5, nota2=9.0, trabalho=10, faltas=2)
aluno_nota11 = CalculaNota(matricula=12355, nota1=7.5, nota2=10.0, trabalho=10, faltas=2)
aluno_nota12 = CalculaNota(matricula=12356, nota1=7.5, nota2=1.0, trabalho=9, faltas=2)
aluno_nota13 = CalculaNota(matricula=12357, nota1=7.5, nota2=2.0, trabalho=8, faltas=2)
aluno_nota14 = CalculaNota(matricula=12358, nota1=7.5, nota2=3.0, trabalho=7, faltas=10)
aluno_nota15 = CalculaNota(matricula=12359, nota1=7.5, nota2=4.0,trabalho=6, faltas=14)
aluno_nota16 = CalculaNota(matricula=12360, nota1=7.5, nota2=5.0, trabalho=5, faltas=16)
aluno_nota17 = CalculaNota(matricula=12361, nota1=7.5, nota2=6.0, trabalho=4, faltas=2)
aluno_nota18 = CalculaNota(matricula=12362, nota1=7.5, nota2=7.0, trabalho=3, faltas=2)
aluno_nota19 = CalculaNota(matricula=12363, nota1=7.0, nota2=8.0, trabalho=2, faltas=2)
aluno_nota20 = CalculaNota(matricula=12364, nota1=7.1, nota2=8.0, trabalho=1, faltas=12)

#Consultar as notas do aluno

notas = aluno_nota1.consultar_nota()
print(f"Notas do aluno: {notas}")
#media = aluno_nota1.calcular_media()

notas = aluno_nota2.consultar_nota()
print(f"Notas do aluno: {notas}")

notas = aluno_nota3.consultar_nota()
print(f"Notas do aluno: {notas}")

notas = aluno_nota4.consultar_nota()
print(f"Notas do aluno: {notas}")

notas = aluno_nota5.consultar_nota()
print(f"Notas do aluno: {notas}")

notas = aluno_nota6.consultar_nota()
print(f"Notas do aluno: {notas}")

notas = aluno_nota7.consultar_nota()
print(f"Notas do aluno: {notas}")

notas = aluno_nota8.consultar_nota()
print(f"Notas do aluno: {notas}")

notas = aluno_nota9.consultar_nota()
print(f"Notas do aluno: {notas}")

notas = aluno_nota10.consultar_nota()
print(f"Notas do aluno: {notas}")

notas = aluno_nota11.consultar_nota()
print(f"Notas do aluno: {notas}")

notas = aluno_nota12.consultar_nota()
print(f"Notas do aluno: {notas}")

notas = aluno_nota13.consultar_nota()
print(f"Notas do aluno: {notas}")

notas = aluno_nota14.consultar_nota()
print(f"Notas do aluno: {notas}")

notas = aluno_nota15.consultar_nota()
print(f"Notas do aluno: {notas}")

notas = aluno_nota16.consultar_nota()
print(f"Notas do aluno: {notas}")

notas = aluno_nota17.consultar_nota()
print(f"Notas do aluno: {notas}")

notas = aluno_nota18.consultar_nota()
print(f"Notas do aluno: {notas}")

notas = aluno_nota19.consultar_nota()
print(f"Notas do aluno: {notas}")

notas = aluno_nota20.consultar_nota()
print(f"Notas do aluno: {notas}")

#Calcular e exebir a média

media = aluno_nota1.calcular_media()
print(media)

media = aluno_nota2.calcular_media()
print(media)

media = aluno_nota3.calcular_media()
print(media)

media = aluno_nota4.calcular_media()
print(media)

media = aluno_nota5.calcular_media()
print(media)

media = aluno_nota6.calcular_media()
print(media)

media = aluno_nota7.calcular_media()
print(media)

media = aluno_nota8.calcular_media()
print(media)

media = aluno_nota9.calcular_media()
print(media)

media = aluno_nota10.calcular_media()
print(media)

media = aluno_nota11.calcular_media()
print(media)

media = aluno_nota12.calcular_media()
print(media)

media = aluno_nota13.calcular_media()
print(media)

media = aluno_nota14.calcular_media()
print(media)

media = aluno_nota15.calcular_media()
print(media)

media = aluno_nota16.calcular_media()
print(media)

media = aluno_nota17.calcular_media()
print(media)

media = aluno_nota18.calcular_media()
print(media)

media = aluno_nota19.calcular_media()
print(media)

media = aluno_nota20.calcular_media()
print(media)


        
