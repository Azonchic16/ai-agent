import sys
from pathlib import Path
import streamlit as st
from app.interface.streamlit_ui import ChatInterface
from app.utils.llm_model import LlmModel
import os
from dotenv import load_dotenv

def main():
    # Настройка путей
    ROOT_DIR = Path(__file__).parent.parent.parent
    sys.path.append(str(ROOT_DIR))
    load_dotenv(ROOT_DIR / '.env')
    
    # Создаем интерфейс и модель
    chat_interface = ChatInterface("RAG-система")
    llm_model = LlmModel(api_key=os.getenv('MISTRAL_KEY'))
    
    # Запускаем интерфейс
    user_input = chat_interface.run_interface()
    
    if user_input:
        # Обрабатываем через Mistral AI
        python_variable_result = llm_model.do_req(user_input)
        
        # Показываем результат
        chat_interface.process_and_display(user_input, python_variable_result)
        
        # Обновляем интерфейс
        st.rerun()

if __name__ == '__main__':
    main()