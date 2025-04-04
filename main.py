import json

arquivo_cadastros = "cadastros.json"

def exibir_menu():
    print("\n --- MENU CADASTRO ---")
    print("1 - Cadastrar pessoa")
    print("2 - Ver cadastros")
    print("3 - Sair")
    print("-----------------------")

def salvar_cadastros (cadastros):
    with open (arquivo_cadastros, "w", encoding="utf-8") as arquivo:
             json.dump(cadastros, arquivo, ident=4,ensure_ascii=False)

def carregar_cadastros():
      try:
            with open (arquivo_cadastros, "r", encoding="utf-8") as arquivos:
                  return json.load(arquivos)
      except(FileNotFoundError, json.JSONDecodeERROR):
            return []
      
def cadastrar_pessoa(cadastras):
      nome= input("Nome: ")
      nome= input("Idade: ")
      nome= input("Turmas: ")
      nome= input("Cursos: ")

      cadastros.append("Nome": nome, "Idade": idade, "Turma":turma, "Cursos":curso)
      salvar_cadastros(cadastros)
      print("Cadastro realizado com sucesso!")

