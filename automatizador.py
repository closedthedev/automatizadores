import pywhatkit as kit
import time

# Lista de números de telefone (inclua o código do país, ex: +5511999999999 para Brasil)
phone_numbers = [

    
    "+5521999999999",
    "+5521999999999",
    "+5521999999999",
    "+5521999999999",
    "+5521999999999",
    "+5521999999999",
    "+5521999999999",
    "+5521999999999",
    "+5521999999999",
    
    
]

# Mensagem a ser enviada
message = "Olá! Esta é uma mensagem automatizada enviada pelo script em Python."

# Tempo de atraso entre mensagens (em segundos)
delay_between_messages = 15

# Função para enviar mensagem
def send_whatsapp_message(phone_number, message):
    kit.sendwhatmsg_instantly(phone_number, message)
    time.sleep(5)  # Tempo para o navegador abrir e enviar a mensagem

# Enviando mensagem para todos os números na lista
for number in phone_numbers:
    send_whatsapp_message(number, message)

    time.sleep(delay_between_messages)  # Espera para evitar problemas com envio rápido demais

print("Mensagens enviadas com sucesso!")