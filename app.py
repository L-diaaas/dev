dados = {
    "professores":[
        {
        'id': 1023,
        'nome': 'Lucas Silva',
        'idade': 41,
        'materia': 'Programação Orientada a Objetos',
        'observacoes': 'O professor explica os conteúdos de forma clara e organizada, facilitando o entendimento dos temas abordados.'
        },
        
    ],
    "turmas": [ 
        {    
            "id": 1,
            "descricao": "Turma de Matemática",
            "professor_id": 101,
            "activo": True
        },
        {}
    ],
    "alunos": [
        {
            "nome": "Maria Silva",
            "turma_id": 101,
            "idade": 20,
            "data_nascimento": "2004-03-19",
            "nota_primeiro_semestre": 8.5,
            "nota_segundo_semestre": 9.0,
            "media_final": 8.75
        },
        {}
    ]
}

#Alunos
class Aluno_nao_encontrado(Exception):
    pass

def aluno_por_id(id_aluno):
    lista_alunos = dados['alunos']
    for aluno in lista_alunos:
        if aluno['id'] == id_aluno:
            return aluno
    raise Aluno_nao_encontrado

def aluno_existe(id_aluno):
    try:
        aluno_por_id(id_aluno)
        return True
    except Aluno_nao_encontrado:
        return False

def adiciona_aluno(dict):
    dados['alunos'].append(dict)

def lista_alunos():
    return dados["alunos"]

def apaga_todos_alunos():
    dados['alunos'] = []

#Professores    
class Professor_nao_encontrado(Exception):
    pass
    
def professor_por_id(id_professor):
    lista_professores = dados['professores']
    for professor in lista_professores:
        if professor['id'] == id_professor:
            return professor
    raise Professor_nao_encontrado

def professor_existe(id_professor):
    try:
        professor_por_id(id_professor)
        return True
    except Professor_nao_encontrado:
        return False
    
def adiciona_professor(dict):
    dados['professores'].append(dict)
    
def lista_professores():
    return dados["professores"]

def apaga_todos_professores():
    dados["professores"] = []
    

#Turmas    
class Turma_nao_encontrada(Exception):
    pass

def turma_por_id(id_turma):
    lista_turmas = dados['turmas']
    for turma in lista_turmas:
        if turma['id'] == id_turma:
            return turma 
    raise Turma_nao_encontrada

def turma_existe(id_turma):
    try:
        turma_por_id(id_turma)
        return True
    except Turma_nao_encontrada:
        return False
    
def adiciona_turma(dict):
    dados['turmas'].append(dict)
    
def lista_turmas():
    return dados['professores']

def apaga_todas_turmas():
    dados['turmas'] = []