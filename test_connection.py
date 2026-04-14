import psycopg2


import os
from dotenv import load_dotenv
load_dotenv()

passwd=os.getenv('DB_PASSWORD')
#print(passwd)

try:
#    passwd = input('digite a senha: ')
    conn = psycopg2.connect(
        host='db-grande-app-br.crwm0uc8af2g.sa-east-1.rds.amazonaws.com',
        port=5432,
        database='myproject_db',
        user='aws_master',
        password=passwd,
        sslmode='require',
        sslrootcert='./rds-ca-rsa2048-g1.pem'
    )
    print("✅ Conexão bem-sucedida!")
    conn.close()
except Exception as e:
    print(f"❌ Erro: {e}")

