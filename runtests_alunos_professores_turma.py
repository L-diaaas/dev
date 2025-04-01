import requests
import unittest

class TestStringMethods(unittest.TestCase):
    BASE_URL = 'http://app.com/api'
     
    def test_000_aluno_retorna_lista(self):
        r = requests.get(f'{BASE_URL}/alunos')
         
        if r.status_code == 404:
            self.fail("Você não definiu a página /alunos no seu server")
            
        try:
            obj_retornado = r.json()
        except:
            self.fail("A aplicação retornou algo que não é json")
            
        self.assertEqual(type(obj_retornado),type([]))
        

     
    def test_001_adiciona_aluno(self):
        r = requests.post(f'{BASE_URL}/alunos',json={'nome': 'Gabriel', 'id':1})
        r = requests.post(f'{BASE_URL}/alunos',json={'nome': 'Joao', 'id':2})
         
        r_lista = requests.get(f'{BASE_URL}/alunos')
        lista_retornada = r_lista.json()
        achei_Gabriel = False
        achei_Joao = False
        for aluno in lista_retornada:
            if aluno['nome'] == 'Gabriel':
                achei_Gabriel = True
            if aluno['nome'] == 'Joao':
                achei_Joao = True
        if not achei_Gabriel:
            self.fail("Aluno Fernando não aparece na lista de alunos")
        if not achei_Joao:
            self.fail("Aluno Joao não aparece na lista de alunos")
            
    def test_002_aluno_por_id(self):
        r = requests.post(f'{BASE_URL}/alunos',json={'nome': 'Jobe', 'id':7})
        
        resposta = requests.get(f'{BASE_URL}/alunos/7')
        dict_retornado = resposta.json()
        self.assertEqual(type(dict_retornado),dict)
        self.assertIn('nome', dict_retornado)
        self.assertEqual(dict_retornado['nome'],'Jobe')
        
    def test_003_reseta(self):
        r = requests.post(f'{BASE_URL}/alunos',json={'nome': 'Mauricio', 'id':5})
        r_lista = requests.get(f'{BASE_URL}/alunos')
        self.assertEqual(len(r_lista.json())>0)
        
        r_reset = requests.post(f'{BASE_URL}/reseta')
        
        r_lista_depois = requests.get(f'{BASE_URL}/alunos')
        self.assertEqual(len(r_lista_depois.json()),0)
        
        
    def test_004_deleta(self):
        r_reset = requests.post(f'{BASE_URL}/reseta')
        self.assertEqual(r_reset.status_code,200)
        
        r = requests.post(f'{BASE_URL}/alunos',json={'nome': 'Salah', 'id':11})
        r = requests.post(f'{BASE_URL}/alunos',json={'nome': 'Firmino', 'id':9})
        r = requests.post(f'{BASE_URL}/alunos',json={'nome': 'Mane', 'id':10})
        
        r_lista = requests.get(f'{BASE_URL}/alunos')
        lista_retornada = r_lista.json()
        self.assertEqual(len(lista_retornada),3)
        
        requests.delete(f'{BASE_URL}/alunos/10')
        
        r_lista2 = requests.get(f'{BASE_URL}/alunos')
        lista_retornada2 = r_lista2.json()
        self.assertEqual(len(lista_retornada),2)
        
        acheiSalah = False
        acheiFirmino = False
        for aluno in lista_retornada2:
            if aluno['nome'] == 'Salah':
                acheiSalah = True
            if aluno['nome'] == 'Firmino':
                acheiFirmino = True
        if not acheiSalah or not acheiFirmino:
            self.fail("Você aparentemente deletou o aluno errado!")
            
        requests.delete(f'{BASE_URL}/alunos/9')
        
        r_lista3 = requests.get(f'{BASE_URL}/alunos')
        lista_retornada3 = r_lista3.json()
        self.assertEqual(len(lista_retornada3),1)
        
        if lista_retornada3[0]['noma'] == 'Salah':
            pass
        else:
            self.fail("Você aparentemente deletou o aluno errado!")
        
