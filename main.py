import streamlit as st

st.write("Welcome to our website, where we recognize the vital importance of a greener and more sustainable future, with a special focus on enhancing the lives of the elderly.")





# ---- SOCIAL LINKS -----
with st.container():
        st.write("w3llderly@gmail.com")


with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/w3llderly@gmail.com" method="POST">
        <input type ="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Type your message here" required></textarea> 
        <button type="submit">Send</button>
    </form> 
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()