print("🧪 RANSOMWARE EDUCACIONAL - DIO (MOBILE)")
print("=" * 50)
print("⚠️  AMBIENTE CONTROLADO - APENAS ESTUDO")

import os
import time
import hashlib
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

# CONFIGURAÇÕES DE EMAIL - ATUALIZADAS
EMAIL_ORIGEM = "alengamer64@gmail.com"
EMAIL_DESTINO = "alengamer64@gmail.com"
SENHA_APP = "csqs tbia ldyo aeeg"

class RansomwareMobile:
    def __init__(self):
        self.arquivos_afetados = []
        self.senha_simulada = "DIO2024"
        
    def enviar_relatorio(self, assunto, mensagem):
        """Envia relatório por email"""
        try:
            msg = MIMEText(mensagem, 'plain', 'utf-8')
            msg['Subject'] = f"Ransomware Educacional - {assunto}"
            msg['From'] = EMAIL_ORIGEM
            msg['To'] = EMAIL_DESTINO

            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(EMAIL_ORIGEM, SENHA_APP)
                server.send_message(msg)
            
            print(f"📧 Email enviado: {assunto}")
            return True
        except Exception as e:
            print(f"❌ Erro no email: {e}")
            return False
        
    def criar_arquivos_teste(self):
        """Cria arquivos de teste no diretório do Pydroid"""
        arquivos_teste = [
            "documento_teste.txt",
            "foto_simulada.jpg.txt", 
            "planilha_dados.xlsx.txt",
            "contatos_importantes.txt"
        ]
        
        print("\n📁 CRIANDO ARQUIVOS DE TESTE...")
        for arquivo in arquivos_teste:
            with open(arquivo, 'w', encoding='utf-8') as f:
                f.write(f"Conteúdo importante do {arquivo}\n")
                f.write(f"Criado em: {datetime.now()}\n")
                f.write("--- DIO CYBERSECURITY STUDY ---\n")
            print(f"✅ Criado: {arquivo}")
            self.arquivos_afetados.append(arquivo)
            
    def simular_criptografia(self):
        """Simula criptografia com hash (não real)"""
        print("\n🔒 SIMULANDO CRIPTOGRAFIA...")
        
        for arquivo in self.arquivos_afetados:
            # Ler conteúdo original
            with open(arquivo, 'r', encoding='utf-8') as f:
                conteudo = f.read()
            
            # "Criptografar" com hash (apenas demonstração)
            hash_cripto = hashlib.md5(conteudo.encode()).hexdigest()
            
            # Salvar versão "criptografada"
            with open(arquivo, 'w', encoding='utf-8') as f:
                f.write(f"[CRIPTOGRAFADO] {hash_cripto}\n")
                f.write("⚠️ SEUS ARQUIVOS FORAM BLOQUEADOS!\n")
                
            print(f"🔒 Afetado: {arquivo}")
            time.sleep(1)
            
    def exibir_resgate(self):
        """Mostra mensagem de resgate simulada"""
        mensagem = f"""
        💀 SEUS ARQUIVOS FORAM CRIPTOGRAFADOS! 💀
        
        Não é possível acessar seus documentos!
        
        Para descriptografar, você precisa:
        • Enviar R$ 500 em Bitcoin
        • Ou usar a senha: {self.senha_simulada}
        
        ⏰ Tempo limite: 24 horas
        
        --- ESTA É UMA SIMULAÇÃO DIO ---
        Aperte ENTER para recuperar arquivos...
        """
        print(mensagem)
        
        # Enviar relatório do ataque
        relatorio = f"Simulação de ransomware executada\nArquivos afetados: {len(self.arquivos_afetados)}\nHora: {datetime.now()}"
        self.enviar_relatorio("ATAQUE SIMULADO", relatorio)
        
        input()
        
    def recuperar_arquivos(self):
        """Recupera os arquivos simulados"""
        print("\n🔓 RECUPERANDO ARQUIVOS...")
        
        for arquivo in self.arquivos_afetados:
            with open(arquivo, 'w', encoding='utf-8') as f:
                f.write(f"Arquivo recuperado: {arquivo}\n")
                f.write(f"Recuperado em: {datetime.now()}\n")
                f.write("✅ TODOS OS DADOS FORAM RESTAURADOS!\n")
                f.write("--- PROJETO EDUCACIONAL DIO ---\n")
            print(f"✅ Recuperado: {arquivo}")
            time.sleep(1)
            
        # Enviar relatório de recuperação
        relatorio = f"Recuperação concluída com sucesso!\nTodos os {len(self.arquivos_afetados)} arquivos restaurados."
        self.enviar_relatorio("RECUPERAÇÃO CONCLUÍDA", relatorio)

def executar_simulacao():
    """Executa toda a simulação"""
    print("\n" + "="*50)
    print("🚀 INICIANDO SIMULAÇÃO DE RANSOMWARE")
    print("="*50)
    
    ransomware = RansomwareMobile()
    
    # Fase 1: Preparação
    ransomware.criar_arquivos_teste()
    time.sleep(2)
    
    # Fase 2: Ataque
    ransomware.simular_criptografia()
    time.sleep(2)
    
    # Fase 3: Resgate
    ransomware.exibir_resgate()
    
    # Fase 4: Recuperação
    ransomware.recuperar_arquivos()
    
    print("\n🎯 SIMULAÇÃO CONCLUÍDA!")
    print("📧 Relatórios enviados para seu email")

# Informações educacionais
def mostrar_aprendizados():
    print("\n" + "🔐 APRENDIZADOS SOBRE RANSOMWARE:")
    print("-" * 40)
    
    aprendizados = [
        "✅ Faça backup regular dos dados",
        "✅ Use antivírus atualizado", 
        "✅ Cuidado com emails suspeitos",
        "✅ Mantenha sistema atualizado",
        "✅ Use autenticação em 2 fatores",
        "✅ Eduque-se sobre phishing"
    ]
    
    for item in aprendizados:
        print(item)
        time.sleep(0.5)

if __name__ == "__main__":
    executar_simulacao()
    mostrar_aprendizados()
  