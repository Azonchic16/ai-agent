import streamlit as st

class ChatInterface:
    def __init__(self, title="Чат-интерфейс"):
        self.title = title
        self.setup_page_config()
        self.init_session_state()
    
    def setup_page_config(self):
        """Настройка страницы"""
        st.set_page_config(
            page_title=self.title,
            page_icon="💬",
            layout="wide"
        )
    
    def init_session_state(self):
        """Инициализация состояния сессии"""
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        if 'current_input' not in st.session_state:
            st.session_state.current_input = ""
    

    def get_user_input(self):
        """
        Метод для получения пользовательского ввода с поддержкой Enter
        """
        # Используем форму для поддержки Enter
        with st.form(key="chat_form", clear_on_submit=True):
            input_text = st.text_input(
                "Введите ваш запрос:",
                placeholder="Введите текст и нажмите Enter...",
                key="user_input_field"
            )
            
            # Кнопка внутри формы - будет работать и по клику и по Enter
            submitted = st.form_submit_button("Отправить", type="primary")
            
            if submitted:
                if input_text.strip():
                    return input_text.strip()
                else:
                    st.warning("Пожалуйста, введите текст")
        
        return None
    
    def show_chat_history(self):
        """Показывает историю чата"""
        for i, (user_msg, python_var_result) in enumerate(st.session_state.chat_history):
            # Показываем пользовательский ввод
            with st.container():
                st.markdown(f"**👤 Вы:** {user_msg}")
                st.markdown("---")
            
            # Показываем результат из Python переменной
            with st.container():
                st.markdown(f"**🤖 Ответ:** {python_var_result}")
                st.markdown("---")
    
    def add_to_history(self, user_input, python_variable):
        """
        Добавляет сообщение в историю чата
        user_input: текст от пользователя
        python_variable: переменная из Python для отображения
        """
        st.session_state.chat_history.append((user_input, str(python_variable)))
        st.session_state.current_input = ""  # Очищаем поле ввода
    
    def display_result(self, python_variable, title="Результат"):
        """
        Метод для вывода переменной из Python в красивом окошке
        python_variable: любая переменная из Python
        title: заголовок окошка
        """
        with st.container():
            st.markdown("---")
            st.subheader(f"🎯 {title}")
            
            # Красиво форматируем вывод в зависимости от типа переменной
            if isinstance(python_variable, (list, tuple)):
                st.write("**Список:**")
                for i, item in enumerate(python_variable, 1):
                    st.write(f"{i}. {item}")
            elif isinstance(python_variable, dict):
                st.write("**Словарь:**")
                for key, value in python_variable.items():
                    st.write(f"• **{key}:** {value}")
            elif isinstance(python_variable, str):
                st.info(f"**Текст:** {python_variable}")
            else:
                st.info(f"**Значение:** {python_variable}")
            
            st.markdown("---")
    
    def run_interface(self):
        """
        Основной метод запуска интерфейса
        Возвращает пользовательский ввод если он есть
        """
        st.title(self.title)
        
        # Показываем историю чата
        self.show_chat_history()
        
        # Получаем новый ввод
        user_input = self.get_user_input()
        
        return user_input
    
    def process_and_display(self, user_input, python_variable):
        """
        Полный цикл: добавляет в историю и показывает результат
        """
        self.add_to_history(user_input, python_variable)
        self.display_result(python_variable)