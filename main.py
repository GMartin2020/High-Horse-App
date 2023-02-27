import docxtpl
import os
import requests
import time
import pkg_resources

import streamlit as st
from streamlit_lottie import st_lottie

progress_text = "Custom crafting your document. Please wait."


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def open_documents_folder():
    os.startfile(os.path.expanduser('~/Documents'))


def main():
    col1, col2 = st.columns ([3, 1])

    with col1:
        st.title (":blue[HIGH HORSE LEGAL]")
        st.subheader ("_Staying Ahead of Legal Innovation_")

    with col2:
        lottie_url_hello = "https://assets2.lottiefiles.com/packages/lf20_6ljswtij.json"
        lottie_url_download = "https://assets4.lottiefiles.com/private_files/lf30_t26law.json"
        lottie_hello = load_lottieurl (lottie_url_hello)
        lottie_download = load_lottieurl (lottie_url_download)

        st_lottie (lottie_hello, key="hello", height=140, width=100, )

    st.info (
        "This application will help you to draft legal documents. Complete the fields below and click submit.")
    st.markdown("---")

    name = st.text_input("Enter Name", placeholder="Client Name")
    surname = st.text_input("Enter Surname")
    provinces = ['Eastern Cape', 'Free State', 'Gauteng', 'KwaZulu-Natal', 'Limpopo', 'Mpumalanga', 'North West',
                 'Northern Cape', 'Western Cape']
    province = st.selectbox("Select Province", provinces)

    if st.button("Submit"):
        with st.spinner('Drafting Document. Wait for it...'):
            time.sleep(2)
        doc_path = pkg_resources.resource_filename(__name__, 'Test Doc.docx')
        doc = docxtpl.DocxTemplate(doc_path)
        context = {
            "Name": name,
            "Surname": surname,
            "Province": province
        }
        doc.render(context)
        file_name = f"{name} {surname}.docx"
        file_path = os.path.join(os.path.expanduser("~/Documents/"), file_name)
        doc.save(file_path)
        st.write("")
        alert = st.success("Document Drafted!")  # Display the alert
        time.sleep(2)  # Wait for 3 seconds
        alert.empty()  # Clear the alert

        st.button("Open Document", on_click=open_documents_folder)


if __name__ == "__main__":
    main()
