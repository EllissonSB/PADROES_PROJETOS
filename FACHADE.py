class FacadeMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
class Curso:
    def __init__(self,nome,codigo):
        self.nome=nome
        self.codigo=codigo
    def get_nome(self):
        return self.nome
    def get_codigo(self):
        return self.codigo
    def set_nome(self,nome_):
        self.nome=nome_
    def set_curso(self,curso):
        self.curso=curso
class Aluno:
    def __init__(self,matricula,nome):
        self.matricula=matricula
        self.nome=nome
    def set_nome(self,nome):
        self.nome=nome
    def set_matricula(self,matricula):
        self.matricula=matricula
    def get_nome(self):
        return self.nome
    def get_matricula(self):
        return self.matricula
class Turma:
    def __init__(self):
        self.codigo=''
        self.alunos=[]
        self.curso=''
    def set_aluno(self,aluno):
        self.alunos.append(aluno)
    def set_codigo(self,codigo):
        self.codigo=codigo
    def set_curso(self,curso):
        self.curso=curso
    def get_nome(self):
        return (self.curso)
    def get_curso(self):
        return self.curso.get_nome()
    def get_alunos(self):
        return self.alunos
class Escola:
    def __init__(self,nome):
        self.nome = nome
        self.cursos=[]
        self.alunos=[]
    def get_nome(self):
        return self.nome
    def set_alunos(self,matricula,nome):
        self.alunos.append(Aluno(matricula,nome))
    def set_curso(self,nome,codigo):
        self.cursos.append(Curso(nome,codigo))
    def set_nome(self,nome):
        self.nome = nome
    def get_curso(self,codigo):
        for i in range(len(self.curso)):
            if (self.curso[i].get_codigo() == codigo):
                return self.curso[i]
        else: return None
    def get_aluno(self,matricula):
        for i in range(len(self.aluno)):
            if(self.aluno[i].get_matricula() == matricula):
                return self.aluno[i]
        else: return None
    def get_nome(self):
        return self.nome
    def print_cursos(self):
        for i in range(len(self.cursos)):
            print(self.cursos[i].get_nome())
class Facade(metaclass=FacadeMeta):
    def __init__(self)->None:
        self.escola=[]
        self.turma=[]
    def ver_escola(self,nome):
        for i in range(len(self.escola)):
            if(self.escola[i].get_nome() == nome):
                return i
        else: return None
    def verificar_turma(self,codigo):
        for i in range(len(self.turma)):
            if(self.turma[i].get_codigo==codigo):
                return self.turma[i]
        else: return None
    def matricula(self,matricula,codigo_curso,codigo_turma):
        if(self.verificar_turma(codigo_turma==None)):
            self.turma.append(Turma(codigo_turma))
            self.turma[-1].set_curso(self.escola[0].get_curso(codigo_curso))
        self.turma[self.verificar_turma(codigo_turma)].set_aluno(self.escola[0].get_aluno(matricula))
    def criar_escola(self,nome):
        if(self.ver_escola(nome)==None):
            self.escola.append(Escola(nome))
    def criar_curso(self,escola,nome,codigo):
        self.criar_escola(escola)
        self.escola[self.ver_escola(escola)].set_curso(nome,codigo)
    def criar_aluno(self,nome,escola,matricula):
        self.criar_escola(escola)
        self.escola[self.ver_escola(escola)].set_alunos(matricula,nome)
    def print_escolas(self):
        for i in range(len(self.escola)):
            print(self.escola[i].get_nome())
    def print_escola(self,nome):
        esc=self.escola[self.ver_escola(nome)]
        print("O nome da Escola é",esc.get_nome())
        print('Cursos na Escola:')
        print(esc.print_cursos())
class MatriculaGUI:
    def __init__(self):
        self.facade=Facade()
    def criar_escola(self,nome):
        self.facade.criar_escola(nome)
    def criar_curso(self,escola,nome,codigo):
        self.facade.criar_curso(escola,nome,codigo)
    def criar_aluno(self,nome,escola,matricula):
        self.facade.criar_aluno(nome,escola,matricula)
    def print_escolas(self):
        self.facade.print_escolas()
    def print_escola(self,nome):
        self.facade.print_escola(nome)
class MatriculaShell:
    def __init__(self):
        self.facade=Facade()
    def criar_escola(self,nome):
        self.facade.criar_escola(nome)
    def criar_curso(self,escola,nome,codigo):
        self.facade.criar_curso(escola,nome,codigo)
    def criar_aluno(self,nome,escola,matricula):
        self.facade.criar_aluno(nome,escola,matricula)
    def print_escolas(self):
        self.facade.print_escolas()
    def print_escola(self,nome):
        self.facade.print_escola(nome)
if __name__ == "__main__":
    mat1=MatriculaGUI()
    print("Criando Pela interface Grafica:.....")
    mat1.criar_escola('Teste')
    mat1.criar_curso('Teste',"Eng.computação",125)
    mat1.criar_aluno("Ellisson","Teste","20191250018")
    print("Printando dados pelo Shell")
    shell1=MatriculaShell()
    shell1.print_escolas()
    shell1.print_escola("Teste")
