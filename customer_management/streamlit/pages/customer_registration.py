"""
Module for customer registration
"""
import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
from customer_management.database.settings import engine
from sqlalchemy import text

from customer_management.controller.layer_controller import run_data_pipeline

def save_customer_to_db(customer_data):
    """Save customer to database"""
    try:
        query = text("""
            INSERT INTO customers (
                name, email, contact, country, city, neighborhood, created_at
            )
            VALUES (
                :name, :email, :contact, :country, :city, :neighborhood, NOW()
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

def validate_form(form_data):
    """Validate form data"""
    errors = []
    
    if not form_data['nome'].strip():
        errors.append("Nome é obrigatório")
        
    if not form_data['email'].strip():
        errors.append("Email é obrigatório")
        
    if not form_data['contact'].strip():
        errors.append("Contato é obrigatório")
        
    if not form_data['pais'].strip():
        errors.append("País é obrigatório")
        
    if not form_data['cidade'].strip():
        errors.append("Cidade é obrigatória")
        
    if not form_data['bairro'].strip():
        errors.append("Bairro é obrigatório")
        
    return errors

def generate_next_code(df):
    """Generate next available customer code"""
    if df.empty:
        return 1
    return df['Código Cliente'].max() + 1

def add_customer_to_dataframe(df, new_customer_data, codigo_cliente):
    """Adds a new customer to the existing DataFrame with proper formatting"""
    new_customer = pd.DataFrame({
        'Código Cliente': [codigo_cliente],
        'Nome': [new_customer_data['name']],
        'Email': [new_customer_data['email']],
        'Contato': [new_customer_data['contact']],
        'País': [new_customer_data['country'].title()],
        'Cidade': [new_customer_data['city'].title()],
        'Bairro': [new_customer_data['neighborhood'].title()],
        'Data_Cadastro': [datetime.now(pytz.timezone('America/Sao_Paulo')).replace(tzinfo=None)]
    })
    return pd.concat([df, new_customer], ignore_index=True)

def run():
    """Function to run customer registration page"""
    st.title("Cadastro de Clientes")
    
    if 'df_gold' not in st.session_state:
        st.warning("Nenhum dado encontrado. Por favor, retorne à página principal.")
        return
    
    df = st.session_state['df_gold']
    
    with st.expander("Formulário de Cadastro", expanded=True):
        with st.form("customer_registration", clear_on_submit=True):
            st.markdown("""
                <style>
                    [data-testid="stForm"] {
                        background-color: rgba(0,0,0,0.2);
                        padding: 1rem;
                        border-radius: 5px;
                    }
                </style>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                nome = st.text_input(
                    "Nome do Cliente",
                    placeholder="Digite o nome completo"
                )
                
                email = st.text_input(
                    "Email",
                    placeholder="Digite o email"
                )
                
                contact = st.text_input(
                    "Contato",
                    placeholder="Digite o telefone/contato"
                )
            
            with col2:
                pais = st.text_input(
                    "País",
                    placeholder="Digite o país"
                )
                
                cidade = st.text_input(
                    "Cidade",
                    placeholder="Digite a cidade"
                )
                
                bairro = st.text_input(
                    "Bairro",
                    placeholder="Digite o bairro"
                )
                
                data_cadastro = datetime.now(pytz.timezone('America/Sao_Paulo')).replace(tzinfo=None)
            
            submitted = st.form_submit_button(
                "Cadastrar Cliente",
                type="primary",
                use_container_width=True
            )
            
            if submitted:
                form_data = {
                    'name': nome,
                    'email': email,
                    'contact': contact,
                    'country': pais,
                    'city': cidade,
                    'neighborhood': bairro
                }
                
                errors = validate_form({
                    'nome': nome,
                    'email': email,
                    'contact': contact,
                    'pais': pais,
                    'cidade': cidade,
                    'bairro': bairro
                })
                
                if errors:
                    for error in errors:
                        st.error(error)
                else:
                    codigo_cliente, error = save_customer_to_db(form_data)
                    
                    if error:
                        st.error(f"Erro ao cadastrar cliente: {error}")
                    else:
                        st.session_state['df_gold'] = run_data_pipeline()
                        
                        new_customer = pd.DataFrame({
                            'Nome': [nome],
                            'Código Cliente': [codigo_cliente],
                            'País': [pais],
                            'Cidade': [cidade],
                            'Bairro': [bairro],
                            'Contato': [contact],
                            'Data_Cadastro': [data_cadastro]
                        })
                        
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
                        
                        st.markdown('<div class="registration-summary">', unsafe_allow_html=True)
                        st.write("### Resumo do Cadastro")
                        st.write(f"**Nome:** {nome}")
                        st.write(f"**Código:** {codigo_cliente}")
                        st.write(f"**Localização:** {cidade}, {pais}")
                        st.write(f"**Data de Cadastro:** {data_cadastro.strftime('%d/%m/%Y %H:%M')}")
                        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.expander("Últimos Cadastros", expanded=False):
        if not df.empty:
            st.dataframe(
                st.session_state['df_gold'].tail(5),
                column_config={
                    "Nome": st.column_config.TextColumn(
                        "Nome",
                        help="Nome do cliente"
                    ),
                    "Código Cliente": st.column_config.NumberColumn(
                        "Código Cliente",
                        help="Código Cliente"
                    ),
                    "País": st.column_config.TextColumn(
                        "País",
                        help="País do cliente"
                    ),
                    "Cidade": st.column_config.TextColumn(
                        "Cidade",
                        help="Cidade do cliente"
                    ),
                    "Contato": st.column_config.TextColumn(
                        "Contato",
                        help="Contato do cliente"
                    ),
                    "Bairro": st.column_config.TextColumn(
                        "Bairro",
                        help="Bairro do cliente"
                    ),
                    "Data de Cadastro": st.column_config.DatetimeColumn(
                        "Data de Cadastro",
                        help="Data e hora do cadastro",
                        format="DD/MM/YYYY HH:mm"
                    )
                },
                hide_index=True,
                use_container_width=True
            )
        else:
            st.info("Nenhum cliente cadastrado ainda.")
