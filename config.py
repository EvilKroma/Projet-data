# Configuration du projet

import os
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

# Configuration de l'API
API_BASE_URL = "https://api.openaq.org/v3"
API_KEY = os.getenv("API_KEY")

# Configuration par défaut
DEFAULT_STATION_ID = 2005

# Configuration des chemins
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
CLEANED_DATA_DIR = os.path.join(DATA_DIR, "cleaned")