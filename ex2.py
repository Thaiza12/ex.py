class CalculaNota:
    def __init__(self, matricula,nota1, nota2):
        self.matricula=matricula
        self.nota1=nota1
        self.nota2=nota2

    def calcular_media(self):

        """Calcula a média aritmética das notas"""
        media = (salf.nota1 + nota2) / 2
        return f"Média do aluno {self.matricula}: {media:2f}"

    def consultar_nota(self):
        """Consulta as notas individuais do aluno"""
        return{
            "matricula": self.matricula,
            "nota1": self.nota1,
            "nota2": self.nota2
        }

#Exemplo de uso

aluno_nota = CalculaNota(matricula=12345, nota1=7.5, nota2=8.0)

#Consultar as notas do aluno

notas = aluno_nota.consultar_nota()
print(f"Notas do aluno: {notas}")

#Calcular e exebir a média

media = aluno_nota.calcular_media()
print(media)


        
