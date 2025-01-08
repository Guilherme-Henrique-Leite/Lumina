"""
Module for customer registration
"""
import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
from customer_management.database.settings import engine
from sqlalchemy import text
from customer_management.utils.location_data import COUNTRY_STATES, COUNTRY_CITIES, CITY_NEIGHBORHOODS, COUNTRY_CODES
import re

def save_customer_to_db(customer_data):
    """Save customer to database"""
    try:
        query = text("""
            INSERT INTO customers (
                name, email, contact, country, state, city, neighborhood, created_at
            )
            VALUES (
                :name, :email, :contact, :country, :state, :city, :neighborhood, NOW()
            )
            RETURNING id;
        """)
        
        with engine.connect() as conn:
            result = conn.execute(query, customer_data)
            id = result.fetchone()[0]
            conn.commit()
            
        return id, None
    except Exception as e:
        return None, str(e)

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_phone(phone):
    """Validate phone number format"""
    phone = re.sub(r'\D', '', phone)
    return 10 <= len(phone) <= 15

def validate_name(name):
    """Validate name format"""
    return bool(name.strip()) and all(char.isalpha() or char.isspace() for char in name)

def validate_form(form_data):
    """Validate form data"""
    errors = []
    
    if not form_data['nome'].strip():
        errors.append("Nome é obrigatório")
    elif not validate_name(form_data['nome']):
        errors.append("Nome deve conter nome e sobrenome (apenas letras)")
        
    if not form_data['email'].strip():
        errors.append("Email é obrigatório")
    elif not validate_email(form_data['email']):
        errors.append("Formato de email inválido")
        
    if not form_data['contact'].strip():
        errors.append("Contato é obrigatório")
    elif not validate_phone(form_data['contact']):
        errors.append("Formato de telefone inválido (deve conter 10 ou 11 dígitos)")
        
    if not form_data['pais'].strip():
        errors.append("País é obrigatório")
        
    if not form_data['cidade'].strip():
        errors.append("Cidade é obrigatória")
    elif not form_data['cidade'].replace(' ', '').isalpha():
        errors.append("Cidade deve conter apenas letras")
        
    if not form_data['bairro'].strip():
        errors.append("Bairro é obrigatório")
    elif not form_data['bairro'].replace(' ', '').replace('-', '').isalpha():
        errors.append("Bairro deve conter apenas letras")
        
    return errors

def clear_form():
    """Clear all form fields"""
    keys_to_clear = [
        'nome', 'email', 'contact', 'country_code',
        'pais', 'estado', 'cidade', 'bairro'
    ]
    for key in keys_to_clear:
        if key in st.session_state:
            del st.session_state[key]

def run():
    """Function to run customer registration page"""
    st.session_state.last_page = 'registration'
    
    st.title("Cadastro de Clientes")
    
    col1, col2 = st.columns(2)
    
    with col1:
        nome = st.text_input(
            "Nome do Cliente *",
            placeholder="Ex: João Silva",
            help="Campo obrigatório - Digite apenas letras",
            key="nome"
        )
        if nome and not validate_name(nome):
            st.warning("Nome deve conter apenas letras", icon="⚠️")
            
        pais = st.selectbox(
            "País *",
            options=[""] + list(COUNTRY_STATES.keys()),
            index=0,
            key="pais",
            placeholder="Selecione um país"
        )
        
        estado = st.selectbox(
            "Estado *",
            options=[""] + COUNTRY_STATES.get(pais, []),
            index=0,
            key="estado",
            placeholder="Selecione um estado"
        )
    
    with col2:
        email = st.text_input(
            "Email *",
            placeholder="Ex: joao.silva@email.com",
            help="Campo obrigatório - Digite um email válido",
            key="email"
        )
        
        cidade = st.selectbox(
            "Cidade *",
            options=[""] + COUNTRY_CITIES.get(pais, {}).get(estado, []),
            index=0,
            key="cidade",
            placeholder="Selecione uma cidade"
        )
        
        bairro = st.selectbox(
            "Bairro *",
            options=[""] + CITY_NEIGHBORHOODS.get(cidade, []),
            index=0,
            key="bairro",
            placeholder="Selecione um bairro"
        )

    contact_col1, contact_col2 = st.columns([1, 3])
    
    with contact_col1:
        country_code = COUNTRY_CODES.get(pais, "")
        st.text_input(
            "Código *",
            value=f"+{country_code}" if country_code else "",
            key="country_code",
            disabled=True,
            help="Código do país selecionado"
        )
    
    with contact_col2:
        contact = st.text_input(
            "Contato *",
            placeholder="Ex: 11999999999",
            help="Campo obrigatório - Digite apenas números (DDD + número)",
            max_chars=15,
            key="contact"
        )
        if contact:
            clean_contact = re.sub(r'\D', '', contact)
            if not validate_phone(clean_contact):
                st.warning("Formato de telefone inválido (deve conter entre 10 e 15 dígitos)", icon="⚠️")
            elif len(clean_contact) > 15:
                st.error("Número de telefone muito longo. Máximo de 15 dígitos permitido.", icon="⚠️")

    with st.form("customer_registration"):
        submitted = st.form_submit_button(
            "Cadastrar Cliente",
            type="primary",
            use_container_width=True
        )

        if submitted:
            clean_contact = re.sub(r'\D', '', contact)
            if len(clean_contact) > 15:
                clean_contact = clean_contact[:15]
            
            full_contact = f"{country_code}{clean_contact}" if country_code and clean_contact else clean_contact
            
            form_data = {
                'nome': nome,
                'email': email,
                'contact': full_contact,
                'pais': pais,
                'estado': estado,
                'cidade': cidade,
                'bairro': bairro
            }
            
            if (nome and validate_name(nome) and 
                email and validate_email(email) and 
                contact and validate_phone(contact) and 
                pais and estado and cidade and bairro):
                
                codigo_cliente, error = save_customer_to_db({
                    'name': nome,
                    'email': email,
                    'contact': full_contact,
                    'country': pais,
                    'state': estado,
                    'city': cidade,
                    'neighborhood': bairro
                })
                
                if error:
                    st.error(f"Erro ao cadastrar cliente: {error}")
                else:
                    st.session_state['show_summary'] = {
                        'codigo_cliente': codigo_cliente,
                        'nome': nome,
                        'email': email,
                        'contact': full_contact,
                        'pais': pais,
                        'estado': estado,
                        'cidade': cidade,
                        'bairro': bairro
                    }
                    
                    clear_form()
                    st.rerun()
            else:
                st.error("Por favor, preencha todos os campos corretamente antes de cadastrar.")

    if 'show_summary' in st.session_state:
        st.success("Cliente cadastrado com sucesso!")
        
        st.markdown("""
            <style>
                .registration-summary {
                    background-color: rgba(50, 205, 50, 0.1);
                    padding: 1rem;
                    border-radius: 5px;
                    margin-top: 1rem;
                }
            </style>
        """, unsafe_allow_html=True)
        
        summary = st.session_state['show_summary']
        st.markdown('<div class="registration-summary">', unsafe_allow_html=True)
        st.write("### Resumo do Cadastro")
        st.write(f"**Código do Cliente:** {summary['codigo_cliente']}")
        st.write(f"**Nome:** {summary['nome']}")
        st.write(f"**Email:** {summary['email']}")
        st.write(f"**Contato:** {summary['contact']}")
        st.write(f"**País:** {summary['pais']}")
        st.write(f"**Estado:** {summary['estado']}")
        st.write(f"**Cidade:** {summary['cidade']}")
        st.write(f"**Bairro:** {summary['bairro']}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        del st.session_state['show_summary']
