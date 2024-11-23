import pyautogui
import time
import pytesseract
from PIL import Image

def capturar_contato():
    # Captura a tela e salva como imagem
    screenshot_path = "print.png"
    pyautogui.screenshot(screenshot_path, region=(495, 631, 84, 15))


    # Use o Tesseract para extrair texto da imagem
    # Certifique-se de que o Tesseract esteja instalado e configurado no PATH do sistema
    # Para Windows, configure o caminho abaixo se necessário:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    
    # Abre a imagem completa
    imagem = Image.open(screenshot_path)

    # Use o Tesseract para extrair texto da imagem
    # Certifique-se de que o Tesseract esteja instalado e configurado no PATH do sistema
    # Para Windows, configure o caminho abaixo se necessário:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Usar o pytesseract para extrair o texto da imagem
    texto_extraido = pytesseract.image_to_string(imagem)

    texto_limpo =  texto_extraido.replace('\n','') # Ajuste conforme o padrão do telefone ou outro texto

    return texto_limpo

def procurar_contato(alunos):
    for aluno in alunos:
        # Clica no campo de pesquisa
        pyautogui.click(328, 315) 
        time.sleep(1)

        #alterna para o HUB
        pyautogui.hotkey('ctrl','a')
        pyautogui.press('backspace')
        time.sleep(1)

        # Usar o pyautogui para digitar o nome do contato
        pyautogui.write(f'{aluno}')
        time.sleep(1)

        pyautogui.press('enter')
        pyautogui.press('enter')
        time.sleep(1)

        # Clica no aluno encontrado
        pyautogui.doubleClick(699, 240) 
        time.sleep(6)

        contato = capturar_contato()

        contatos.append(contato)


        # Clica para fechar janela
        pyautogui.click(974, 60) 
        time.sleep(1)

        # Clica para fechar janela
        pyautogui.click(974, 60) 
        time.sleep(1)


# Função para ler os contatos de um arquivo TXT
def ler_contatos(arquivo):
    with open(arquivo, "r") as file:
        contatos = file.readlines()
    # Limpar os espaços em branco (como '\n') ao redor dos contatos
    return [contato.strip() for contato in contatos]

# Caminho para o arquivo de contatos e imagem
arquivo_alunos = "alunos.txt"  # Substitua pelo caminho correto

# Ler os contatos
alunos = ler_contatos(arquivo_alunos)
print(f"Contatos encontrados: {alunos}")

contatos = []

#alterna para o HUB
pyautogui.hotkey('alt','tab')
time.sleep(1)

# Clica em administrativo
pyautogui.click(46, 30) 
time.sleep(1)

# Alternar para abrir opção alunos
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(3)

procurar_contato(alunos)

print(contatos)