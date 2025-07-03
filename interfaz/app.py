import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
from agentes.agente_base import AgenteBase
from agentes.agente_llm import AgenteLLM

st.set_page_config(page_title="Agente Inteligente", layout="centered")
st.title("🤖 Tu Asistente Inteligente")

tab1, tab2 = st.tabs(["🧠 Agente Básico", "🦜🔗 Agente con LangChain"])

# ----- Agente Básico -----
with tab1:
    st.subheader("😃 Tu Agente Inteligente")
    st.write("Hazle preguntas sobre el clima, matemáticas o lo que quieras.")

    with st.form("form_basico"):
        pregunta_1 = st.text_input("Escribe tu pregunta:", key="pregunta_basica")
        submitted_1 = st.form_submit_button("Enviar")

    if submitted_1 and pregunta_1:
        agente_basico = AgenteBase()
        respuesta_1 = agente_basico.responder(pregunta_1)
        st.success(respuesta_1)

# ----- Agente con LangChain -----
with tab2:
    st.subheader("😃 Asistente Inteligente con LangChain")
    st.write("Este agente utiliza LangChain para procesar la pregunta.")

    with st.form("form_langchain"):
        pregunta_2 = st.text_input("Hazme una pregunta:", key="pregunta_langchain")
        submitted_2 = st.form_submit_button("Responder")

    if submitted_2 and pregunta_2:
        agente_langchain = AgenteLLM()
        respuesta_2 = agente_langchain.responder(pregunta_2)
        st.success(respuesta_2)
