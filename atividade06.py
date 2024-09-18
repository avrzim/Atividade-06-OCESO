import subprocess

def list_users():
    # Define o comando PowerShell a ser executado
    command = ["powershell", "-Command", "Get-LocalUser | Format-List"]
    
    try:
        # Executa o comando e captura a saída
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        # Imprime a saída do comando
        print(result.stdout)
        
    except subprocess.CalledProcessError as e:
        # Se o comando retornar um erro, imprime a mensagem de erro
        print(f"Erro ao executar o comando: {e}")
        print(f"Saída de erro: {e.stderr}")

if __name__ == "__main__":
    list_users()
