import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
BACKUP_DIR = os.path.join(DATA_DIR, 'backups')
CSV = os.path.join(DATA_DIR, 'Gastos.csv')

if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)