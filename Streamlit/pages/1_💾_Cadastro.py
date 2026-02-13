import streamlit as st

with st.form("cadastro_form"):
    st.write("Cadastro de Usuário")
    nome = st.text_input("Nome Completo", placeholder="Digite nome completo")
    email = st.text_input("Email", placeholder="Digite o email")
    cpf = st.text_input("CPF", placeholder="Digite o CPF")

    submitted = st.form_submit_button("Cadastrar")

if submitted:
    st.success(f"{nome} cadastrado com sucesso!")
    st.write(f"Email: {email}")
    st.write(f"CPF: {cpf}")