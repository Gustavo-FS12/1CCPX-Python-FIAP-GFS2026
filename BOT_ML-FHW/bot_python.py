import time
import requests
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# ================= CONFIGURAÇÕES =================
URL_PRODUTO = "https://www.mercadolivre.com.br/ferrari-testarossa-hot-wheels-car-culture-miniatura-7-cm/up/MLBU3735887113"
TOKEN_TELEGRAM = "8978301399:AAHotOIEvuxtZocH5n_8ppg1zq9pqjEy-hA"
CHAT_ID = "6099447344"
INTERVALO = 180


# =================================================

def enviar_telegram():
    url = f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendMessage"
    mensagem = (
        f"🚨 *ESTOQUE DISPONÍVEL!*\n\n"
        f"A miniatura da Ferrari voltou ao estoque!\n\n"
        f"🔗 [Clique aqui para acessar o anúncio]({URL_PRODUTO})"
    )
    payload = {"chat_id": CHAT_ID, "text": mensagem, "parse_mode": "Markdown"}

    try:
        print("[Debug] Enviando mensagem para o Telegram...")
        resposta = requests.post(url, json=payload, timeout=10)
        if resposta.status_code == 200:
            print("✅ Mensagem enviada no Telegram com sucesso!")
        else:
            print(f"❌ Erro na API do Telegram. Código: {resposta.status_code}")
    except Exception as e:
        print(f"❌ Falha ao enviar Telegram: {e}")


def checar_estoque():
    print("[Debug] 1. Configurando opções do navegador...")
    opcoes = Options()
    opcoes.add_argument("--headless")
    opcoes.add_argument("--disable-gpu")
    opcoes.add_argument("--window-size=1920,1080")
    opcoes.add_argument("--disable-blink-features=AutomationControlled")
    opcoes.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    try:
        print("[Debug] 2. Iniciando o motor do Chrome (isso pode demorar na 1ª vez)...")
        servico = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=servico, options=opcoes)

        # Trava de segurança contra carregamentos infinitos
        navegador.set_page_load_timeout(30)

        print("[Debug] 3. Acessando a página do Mercado Livre...")
        navegador.get(URL_PRODUTO)

        print("[Debug] 4. Esperando 5 segundos para o site renderizar o texto...")
        time.sleep(5)

        print("[Debug] 5. Lendo o HTML da página...")
        html = navegador.page_source

        if "Este produto está indisponível" in html or "Anúncio pausado" in html or "Sem estoque" in html:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Checando | Status: Produto indisponível no momento.")
            navegador.quit()
            return False

        elif "Comprar agora" in html or "Adicionar ao carrinho" in html:
            print("🎉 Produto retornou ao estoque! Avisando no Telegram...")
            enviar_telegram()
            navegador.quit()
            return True

        else:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Checando | Status indefinido.")
            navegador.quit()
            return False

    except Exception as e:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Falha no processo: {e}")
        try:
            navegador.quit()
        except:
            pass
        return False


# ================= EXECUÇÃO =================
print("🤖 Iniciando robô Web Scraper para Mercado Livre...")

# 💡 TESTE MANUAL DO TELEGRAM:
# Para testar se o Telegram está funcionando, remova o '#' da linha abaixo e dê o Play.
# Depois que o celular apitar, coloque o '#' de volta para o robô rodar normalmente!
# enviar_telegram()

while True:
    encontrou = checar_estoque()

    if encontrou:
        print("✅ Monitoramento finalizado. O script será desligado.")
        break

    print(f"[Debug] Indo dormir por {INTERVALO} segundos. Zzz...")
    time.sleep(INTERVALO)