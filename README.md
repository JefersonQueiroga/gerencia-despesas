# Gerência de Despesas

Aplicação Django simples para organizar categorias e despesas pessoais com interface baseada em Bootstrap.

## Pré-requisitos

- Windows 10/11
- [Python 3.11+](https://www.python.org/downloads/) (marque a opção “Add Python to PATH” ao instalar)
- Git (opcional, apenas se for clonar o repositório)

## Passo a passo no Windows

1. **Clonar ou baixar o projeto**
   ```powershell
   git clone <url-do-repo>
   cd gerencia-despesas
   ```
   > Se você baixou o `.zip`, extraia e abra o PowerShell na pasta raiz.

2. **Criar o ambiente virtual**
   ```powershell
   python -m venv venv
   ```

3. **Ativar o ambiente virtual**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   > Caso veja um erro de execução de scripts, rode `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` (como administrador) e ative novamente.

4. **Instalar dependências**
   ```powershell
   pip install -r requirements.txt
   ```
   (Se não existir `requirements.txt`, instale manualmente o que precisar, por exemplo: `pip install django`.)

5. **Aplicar migrações**
   ```powershell
   python manage.py migrate
   ```

6. **Criar superusuário (opcional, para acessar /admin)**
   ```powershell
   python manage.py createsuperuser
   ```

7. **Executar o servidor**
   ```powershell
   python manage.py runserver
   ```

8. **Abrir o app**
   - Interface principal: http://127.0.0.1:8000/
   - Admin Django: http://127.0.0.1:8000/admin/

## Variáveis úteis

- Parar o servidor: `Ctrl + C` no terminal.
- Desativar o ambiente virtual: `deactivate`.

## Estrutura resumida

```
gerencia-despesas/
├── gerencia/          # App com models, views e templates das despesas
├── main/              # Configurações do projeto Django
├── manage.py
├── db.sqlite3
└── venv/              # Ambiente virtual (não versionar)
```

Sinta-se à vontade para adaptar o fluxo (por exemplo, usar outro banco) conforme suas necessidades.
