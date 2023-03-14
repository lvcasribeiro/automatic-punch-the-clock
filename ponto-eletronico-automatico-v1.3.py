# Bibliotecas necessárias para o corpo do main script:
from selenium.common.exceptions import (TimeoutException, UnexpectedAlertPresentException, WebDriverException)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from datetime import timedelta, datetime, date
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver import chrome
from selenium import webdriver
from PIL import Image

import pytesseract as pyts
import pyautogui as pyag
import pywhatkit as pywp
import time as pytm
import os as pyos


# Função para captura de data e horário correntes:
def captura_data_e_horario():
    # Data:
    data = date.today();
    data = data.strftime('%d/%m/%Y');

    # Horário:
    hora = datetime.now().hour;
    minuto = datetime.now().minute;
    segundo = datetime.now().second;

    # Dia da semana:
    dia_da_semana = datetime.today().weekday();

    return data, hora, minuto, segundo, dia_da_semana


# Função para iniciar a macro habilitada para bater o ponto:
def macro_ponto():
    # Opções do navegador - notificações, visibilidade e tamanho:
    chrome_options = Options();
    chrome_options.add_argument('--disable-notifications');
    # chrome_options.add_argument("--headless");
    chrome_options.add_argument("--window-size=1920x1080");

    # Instanciando e acessando o navegador:
    navegador = webdriver.Chrome(options = chrome_options);

    navegador.maximize_window();

    # Acessando página de login:
    pytm.sleep(1.5);
    navegador.get('https://agility.nexusweb.com.br/');

    # Selecionando CPF:
    pytm.sleep(1.5);
    navegador.find_element(by = By.XPATH, value = '/html/body/div[2]/div/div[2]/div[1]/select').click();
    pytm.sleep(1.5);
    navegador.find_element(by = By.XPATH, value = '/html/body/div[2]/div/div[2]/div[1]/select/option[3]').click();

    # Inserindo usuário:
    pytm.sleep(1.5);
    navegador.find_element(by = By.XPATH, value = '/html/body/div[2]/div/div[2]/div[2]/input').send_keys('login-user');

    # Inserindo senha:
    pytm.sleep(1.5);
    navegador.find_element(by = By.XPATH, value = '/html/body/div[2]/div/div[3]/div[2]/input').send_keys('password');

    # Selecionando REP VIRTUAL:
    pytm.sleep(1.5);
    navegador.find_element(by = By.XPATH, value = '/html/body/div[2]/div/div[4]/div[2]/select').click();
    pytm.sleep(1.5);
    navegador.find_element(by = By.XPATH, value = '/html/body/div[2]/div/div[4]/div[2]/select/option[2]').click();

    # Selecionando campo para inserção do captcha:
    pytm.sleep(1.5);
    navegador.find_element(by = By.XPATH, value = '/html/body/div[2]/div/div[6]/div/input').click();

    # Captura de captcha - "captcha-nexus.png":
    pytm.sleep(2.5);
    with open('captcha-nexus.png', 'wb') as arquivo:
        arquivo.write(navegador.find_element(by = By.XPATH, value = '/html/body/div[2]/div/div[6]/div/img').screenshot_as_png);
    
    captcha = Image.open(r'C:\Users\lucas.ribeiro\Downloads\captcha-nexus.png');

    # Rodando .exe do tesseract para conversão da imagem em texto:
    pyts.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe';
    captcha_em_texto = pyts.image_to_string(captcha);

    # Inserindo código capturado do captcha:
    pytm.sleep(2.5);
    navegador.find_element(by = By.XPATH, value = '/html/body/div[2]/div/div[6]/div/input').send_keys(captcha_em_texto);

    # Clicando em "Registrar":
    pytm.sleep(1.5);
    navegador.find_element(by = By.XPATH, value = '/html/body/div[2]/div/div[7]/button').click();

    # Tratando possibilidade de conversão errônea .png para string:
    while True:
        try:
            # Aferição, isto é, captura da tag superior ["Atenção!"]:
            pytm.sleep(1.75);
            tag_de_alerta = navegador.find_element(by = By.XPATH, value = '/html/body/div[1]/span[1]').text;
        except UnexpectedAlertPresentException:
            tag_de_alerta = '';
                    
        if tag_de_alerta == "Atenção!":
            # Captura de captcha - "captcha-nexus.png":
            pytm.sleep(2.5);
            with open('captcha-nexus.png', 'wb') as arquivo:
                arquivo.write(navegador.find_element(by = By.XPATH, value = '/html/body/div[2]/div/div[6]/div/img').screenshot_as_png);
            
            captcha = Image.open(r'C:\Users\lucas.ribeiro\Downloads\captcha-nexus.png');

            # Rodando .exe do tesseract para conversão da imagem em texto:
            pyts.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe';
            captcha_em_texto = pyts.image_to_string(captcha);

            # Inserindo código capturado do captcha:
            pytm.sleep(1.5);
            navegador.find_element(by = By.XPATH, value = '/html/body/div[2]/div/div[6]/div/input').send_keys(captcha_em_texto);

            # Clicando em "Registrar":
            pytm.sleep(1.5);
            navegador.find_element(by = By.XPATH, value = '/html/body/div[2]/div/div[7]/button').click();
        else:
            # Tratando alert box de sucesso:
            try:
                WebDriverWait(navegador, 5).until(EC.alert_is_present());
                alerta = navegador.switch_to.alert;
                alerta.accept();
            except TimeoutException:
                print('[!] - Captcha correto: alert box tratado!');
            break;
    
    # Fechando o navegador:
    pytm.sleep(1.5);
    navegador.close();

    # Excluindo arquivo "captcha-nexus.png":
    try:
        pyos.remove(r'C:\Users\lucas.ribeiro\Downloads\captcha-nexus.png');
    except:
        print('[?] - Arquivo captcha-nexus.png não encontrado!');
    
    # Atualização de data e horário:
    data, hora, minuto, segundo, dia_da_semana = captura_data_e_horario();

    # Ajuste de segundo:
    if segundo < 10:
        segundo = f'0{segundo}';

    # Ajuste de minuto:
    if minuto < 10:
        minuto = f'0{minuto}';

    # Ajuste de hora:
    if hora < 10:
        hora = f'0{hora}';

    # Log:
    print(f'[!] - Ponto marcado às {hora}:{minuto}:{segundo} em {data}.\n');
    print('----- - ----- - ----- - ----- - ----- - ----- - -----\n');

    # Enviando marcação para o whatsapp:
    pywp.sendwhatmsg_instantly('+5561900000000', f'[⚡] - Ponto marcado às {hora}:{minuto}:{segundo} em {data}.', 15, True, 5);
    
    # Delay de ciclo, evitando marcação em duplicata:
    pytm.sleep(60);


# Menu inicial - main:
print('----- - ----- - ----- - ----- - ----- - ----- - -----\n');
print('[!] - Ponto Eletrônico Automático - v1.3\n');
print('----- - ----- - ----- - ----- - ----- - ----- - -----\n');
    
while True:
    # Atualização de data e horário:
    data, hora, minuto, segundo, dia_da_semana = captura_data_e_horario();
    
    if (dia_da_semana == 0) or (dia_da_semana == 1) or (dia_da_semana == 2) or (dia_da_semana == 3) or (dia_da_semana == 4):
    
        if ((hora == 12) and (minuto == 31)) or ((hora == 15) and (minuto == 0)) or ((hora == 15) and (minuto == 20)) or ((hora == 18) and (minuto == 30)):
            # Função para bater o ponto:
            macro_ponto();
        else:
            if (hora == 18) and (minuto == 35):
                break;
    
    # Delay do laço:
    pytm.sleep(2.5);
