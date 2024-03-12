from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False) # Headless abre por trás dos panos e Headless=False mostra a automação na sua frente
    pagina = navegador.new_page() # Abertura de uma nova página no Browser
    pagina.goto("https://www.facebook.com/") # Abertura do site escolhido
    pagina.fill('xpath=//*[@id="email"]' , "testepython@gmail.com") # Preenchimento do campo de e-mail
    pagina.fill('xpath=//*[@id="pass"]' , "12345678") #  Preenchimento do campo de senha
    time.sleep(2) # Tempo
    pagina.locator('xpath=//*[@id="u_0_5_bK"]').click()
    time.sleep(2) # Tempo de espera da automação