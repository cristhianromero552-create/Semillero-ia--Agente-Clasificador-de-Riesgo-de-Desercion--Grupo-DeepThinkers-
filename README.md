# Agente IA – Clasificador de Riesgo de Deserción (ISP) 🛰️

## 🚀 Proyecto: Semillero de IA - Grupo DeepThinkers

Este proyecto consiste en un agente inteligente diseñado para proveedores de servicios de internet (ISP). El sistema combina un asistente de soporte técnico con un motor analítico que predice el riesgo de que un cliente cancele su servicio (*churn*) basándose en su léxico y sentimiento.

### 👥 Integrantes
* **Cristhian Jacinto Romero Orellana** 
* **Christopher Iván Acosta Varela** 
* **Leandro Sebastián Rivero Merchán**
* **Jhon Jairo Contrera Segido**
* **Jomira Aracely Silva Carrasco**
* **Joselyn Angela Gonzalez Yagual**
* **Josué Daniel Cárdenas Zambrano**
* **Edison Jhosue Morales Mina**
* **Julio Alejandro Fernández Quimis**
* **Leida Ariana Espinoza Torres**

---

### 📝 Descripción del Agente
Nuestro agente es una solución integral de retención que utiliza **LLMs (Large Language Models)** para gestionar conversaciones críticas. A diferencia de un bot tradicional, este agente:
1.  **Gestiona Emociones:** Detecta clientes frustrados y aplica protocolos de validación emocional.
2.  **Es Persuasivo:** Utiliza técnicas de negociación para evitar la cancelación.
3.  **Es Técnico:** Consulta manuales de servicio mediante **RAG (Retrieval-Augmented Generation)**.

### 🛠️ Qué hace el agente (Funcionalidades)
* **Análisis Léxico y de Sentimiento:** Clasifica cada mensaje en tiempo real (Muy Negativo a Muy Positivo).
* **Cálculo de Probabilidad de Deserción:** Entrega un valor porcentual (0-100%) sobre la intención de abandono del cliente.
* **Dashboard Operativo:** Interfaz en **Gradio** que permite a los supervisores monitorear el nivel de riesgo de cada caso.
* **Prevención de Alucinaciones:** Respuestas basadas estrictamente en la documentación técnica oficial del ISP.

---

### 🏗️ Arquitectura Técnica
* **Modelo:** Google Gemini 2.5 Flash.
* **Orquestador:** LangChain.
* **Base de Datos Vectorial:** ChromaDB para el almacenamiento de manuales técnicos.
* **Interfaz:** Gradio.
* **Lógica de Riesgo:** Cadena independiente de análisis con salida estructurada en JSON.

---

### 🎥 Video de Presentación 
Haz clic en eel icono para ver nuestra explicación técnica y la demostración del agente en tiempo real:


[![YouTube Badge](https://img.shields.io/badge/YouTube-Video_Demo-red?style=for-the-badge&logo=youtube)](https://youtu.be/DOuBHzkfDtI)
