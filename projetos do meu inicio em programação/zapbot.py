from selenium import webdriver
import time


class bot:
    def opcoes(self):
        self.fotos = ["Larissa"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang-pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')



    def enviaresposta(self):
        self.driver.get('https://docs.google.com/forms/d/e/1FAIpQLScyFykTjAStLlR0gf3T3JhHlwaIEbFb8Q2uI0VNyvc24JtfLg/viewform?chromeless=true')
        opcao = self.driver.find_elements_both

    <div class="appsMaterialWizToggleRadiogroupOnRadio exportInnerCircle"></div>


    <span class="appsMaterialWizButtonPaperbuttonLabel quantumWizButtonPaperbuttonLabel exportLabel">Enviar</span>

<a href="https://docs.google.com/forms/u/0/d/e/1FAIpQLScyFykTjAStLlR0gf3T3JhHlwaIEbFb8Q2uI0VNyvc24JtfLg/viewform?chromeless=true&amp;usp=form_confirm">Enviar outra resposta</a>