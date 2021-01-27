import streamlit as st
import utils
import os
st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("Supermercados Lisboa")
products = ["cebola", "alho"]

option = st.multiselect('Produtos',products)
price_list = []
for i in option:
    price_list.append(st.text_input(f'Preço {i}'))


check = st.checkbox('Tudo certo!')

if check:
    video = utils.video_build(option, price_list)
    video_file = open('output.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.text("Pronto!")
