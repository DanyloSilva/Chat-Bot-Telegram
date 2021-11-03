import requests
import time
import json
import os


class TelegramBot:
    def __init__(self):
        token = '2028241226:AAHFl_4a4e7EKZplmct3cthQRfiK6_jVOYc'
        self.url_base = f'https://api.telegram.org/bot{token}/'

    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]
            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    eh_primeira_mensagem = int(
                        dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(
                        mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)

    # Obter mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Criar uma resposta
      # Criar uma resposta
    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        if eh_primeira_mensagem == True or mensagem in ('Ajuda', 'ajuda', 'Menu','menu'):
            return f'''Olá bem vindo, ao nosso sitema de atendimento:{os.linesep}
            1 - Alteração de roteiro.{os.linesep}
            2 - Pesquisa pendente. {os.linesep}
            3 - Atestado médico.
         
            '''
        if mensagem == '1':
            return f'''Preencha o formulario a seguir https://docs.google.com/forms/d/e/1FAIpQLSdF-EDLey3vF-rBwAGnxrnbf9DeXcEVPR4-82nUpdxIiHqGuw/viewform.{os.linesep}
            A resposta ajudo?(s/n)
            '''
        elif mensagem == '2':
            return f'''Alguma oportunidade aconteceu!, estaremos verificando com o suporte do Agile mas até lá as tarefas também se encontram no menu reportar do Agile. 
(Foto do caminho para o reportar.)
{os.linesep}A resposta ajudo?(s/n)
            '''

        elif mensagem == '3':
            return f'''Prezado colaborador, por gentileza preencha o formulario https://docs.google.com/forms/d/e/1FAIpQLSeMv193CexZ7oBlA7nuVH6dhuLYDkA4sgDAEyNcIwTjC9TStQ/viewform{os.linesep} A resposta ajudo?(s/n)'''
  


        elif mensagem.lower() in ('s', 'sim'):
            return ''' Gratidão ! '''
        elif mensagem.lower() in ('n', 'não'):
            return ''' Digite Menu para voltar para as Opções '''
        else:
            return 'Gostaria de Ajuda? Digite "ajuda"'

    # Responder
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)


bot = TelegramBot()
bot.Iniciar()
