import streamlit as st
st.title('El ayudante de la pala')
option = st.selectbox(
     '¿ Que estas buscando ?',
     ('Insecticidas', 'Fertilizante', 'Desinfectante RBM-Q','',''))
st.sidebar.title('¿ Quienes somos ?')
st.sidebar.write('Somos una empresa socialmente responsable que busca la eficacia y seguridad de productos quimicos en materia de agricultura por medio de nuestra pagina web, garantizando productos de alta calidad y seguridad en transporte. ')
st.sidebar.image('https://conceptoabc.com/wp-content/uploads/2021/07/Agricultura.jpg')
st.balloons()
