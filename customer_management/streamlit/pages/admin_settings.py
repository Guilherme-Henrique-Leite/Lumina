"""
Module for administrative settings
"""
import streamlit as st
from customer_management.database.settings import engine
from sqlalchemy import text
import pycountry
from babel import Locale, UnknownLocaleError
from babel.numbers import get_territory_currencies

def get_country_name_pt(country):
    """Get country name in Portuguese"""
    try:
        locale = Locale('pt_BR')
        return locale.territories.get(country.alpha_2)
    except (UnknownLocaleError, AttributeError):
        return country.name

def get_unique_locations(location_type):
    """Get unique locations from customers table"""
    try:
        column_map = {
            "country": "country",
            "city": "city",
            "neighborhood": "neighborhood"
        }
        
        column = column_map.get(location_type)
        if not column:
            return []
        
        query = text(f"""
            SELECT DISTINCT {column}
            FROM customers
            WHERE {column} IS NOT NULL
            AND {column} != ''
            ORDER BY {column};
        """)
        
        with engine.connect() as conn:
            result = conn.execute(query)
            return [row[0] for row in result]
    except Exception as e:
        st.error(f"Erro ao buscar dados: {str(e)}")
        return []

def get_valid_countries():
    """Get list of valid countries in Portuguese"""
    try:
        countries = []
        for country in pycountry.countries:
            pt_name = get_country_name_pt(country)
            if pt_name:
                countries.append(pt_name)
        return sorted(countries)
    except Exception as e:
        st.error(f"Erro ao obter lista de países: {str(e)}")
        return []

def is_valid_country(country_name):
    """Check if country is valid"""
    valid_countries = get_valid_countries()
    return any(country.lower() == country_name.lower() for country in valid_countries)

def add_new_location(location_type, name):
    """Add new location by creating a dummy customer record"""
    try:
        if location_type == "country":
            if not is_valid_country(name):
                st.error(f"'{name}' não é um país válido!")
                return False
        
        query = text("""
            INSERT INTO customers (name, email, contact, country, city, neighborhood, created_at)
            VALUES (
                'SYSTEM_LOCATION', 
                'system@location', 
                'SYSTEM',
                CASE WHEN :type = 'country' THEN :name ELSE 'SYSTEM' END,
                CASE WHEN :type = 'city' THEN :name ELSE 'SYSTEM' END,
                CASE WHEN :type = 'neighborhood' THEN :name ELSE 'SYSTEM' END,
                NOW()
            )
        """)
        
        with engine.connect() as conn:
            conn.execute(query, {"type": location_type, "name": name})
            conn.commit()
            return True
    except Exception as e:
        st.error(f"Erro ao adicionar localização: {str(e)}")
        return False

def run():
    """Function to run admin settings page"""
    st.title("Configurações Administrativas")
    
    with st.expander("Visualizar Localizações", expanded=True):
        tab1, tab2, tab3 = st.tabs(["Países", "Cidades", "Bairros"])
        
        with tab1:
            col1, col2 = st.columns([2,1])
            with col1:
                st.subheader("Países Cadastrados")
                paises = get_unique_locations("country")
                if paises:
                    st.write(paises)
                else:
                    st.info("Nenhum país cadastrado.")
            
            with col2:
                with st.form("add_country"):
                    valid_countries = get_valid_countries()
                    new_country = st.selectbox(
                        "Selecione o País",
                        options=valid_countries,
                        index=None,
                        placeholder="Escolha um país para adicionar"
                    )
                    
                    if st.form_submit_button("Adicionar País"):
                        if new_country:
                            if add_new_location("country", new_country):
                                st.success(f"País '{new_country}' adicionado com sucesso!")
                                st.rerun()
        
        with tab2:
            col1, col2 = st.columns([2,1])
            with col1:
                st.subheader("Cidades Cadastradas")
                cidades = get_unique_locations("city")
                if cidades:
                    st.write(cidades)
                else:
                    st.info("Nenhuma cidade cadastrada.")
            
            with col2:
                with st.form("add_city"):
                    new_city = st.text_input("Nova Cidade")
                    if st.form_submit_button("Adicionar Cidade"):
                        if new_city:
                            if add_new_location("city", new_city.title()):
                                st.success(f"Cidade '{new_city}' adicionada com sucesso!")
                                st.rerun()
        
        with tab3:
            col1, col2 = st.columns([2,1])
            with col1:
                st.subheader("Bairros Cadastrados")
                bairros = get_unique_locations("neighborhood")
                if bairros:
                    st.write(bairros)
                else:
                    st.info("Nenhum bairro cadastrado.")
            
            with col2:
                with st.form("add_neighborhood"):
                    new_neighborhood = st.text_input("Novo Bairro")
                    if st.form_submit_button("Adicionar Bairro"):
                        if new_neighborhood:
                            if add_new_location("neighborhood", new_neighborhood.title()):
                                st.success(f"Bairro '{new_neighborhood}' adicionado com sucesso!")
                                st.rerun()