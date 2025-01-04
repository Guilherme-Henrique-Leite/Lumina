"""
Database connection settings
"""
import os
import streamlit as st
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
import logging 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_config_value(key):
    """Get configuration from either Streamlit secrets or environment variables"""
    try:
        value = st.secrets.get(key) or os.getenv(key)
        logger.info(f"Configuração carregada para {key}: {'*' * len(str(value)) if 'PASSWORD' in key else value}")
        return value
    except FileNotFoundError:
        logger.warning(f"Arquivo secrets.toml não encontrado, usando variável de ambiente para {key}")
        return os.getenv(key)

logger.info("Iniciando configuração do banco de dados...")

DB_CONFIG = {
    'drivername': 'postgresql',
    'username': get_config_value('DB_USER'),
    'password': get_config_value('DB_PASSWORD'),
    'host': get_config_value('DB_HOST'),
    'port': int(get_config_value('DB_PORT')),
    'database': get_config_value('DATABASE')
}

logger.info(f"Host: {DB_CONFIG['host']}, Port: {DB_CONFIG['port']}, Database: {DB_CONFIG['database']}")

connection_url = URL.create(**DB_CONFIG)

engine = create_engine(
    connection_url,
    pool_size=1,
    max_overflow=2,
    pool_timeout=5,
    pool_recycle=300,
    connect_args={
        'connect_timeout': 5,
        'application_name': 'lumina_app'
    }
)

def test_connection():
    """Test database connection with timeout"""
    logger.info("Testando conexão com o banco de dados...")
    try:
        with engine.connect() as conn:
            logger.info("Tentando executar query de teste...")
            result = conn.execute(text("SELECT 1"))
            logger.info("Conexão estabelecida e query executada com sucesso!")
            return True
    except Exception as e:
        logger.error(f"Erro na conexão: {str(e)}")
        return False

logger.info("Realizando teste inicial de conexão...")
if not test_connection():
    logger.error("Falha no teste inicial de conexão!")
else:
    logger.info("Teste inicial de conexão bem sucedido!")

__all__ = ['engine', 'test_connection']
