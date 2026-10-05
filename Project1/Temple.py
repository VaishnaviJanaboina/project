import ollama
import streamlit as st
st.title(":green[🙏 🛕WELCOME TO TEMPLE GUIDE CHATBOT!!! 🛕 🙏]")

with st.sidebar:
        st.header(":blue[Temples 🛕]")
        st.image("https://c8.alamy.com/comp/2WH6E1N/view-kakatiya-rudreshwara-temple-or-ramappa-temple-palampet-warangal-telangana-india-2WH6E1N.jpg", caption="Rudreshwara Temple")
        st.image("https://tirupatibalajitravels.co.in/wp-content/uploads/2024/01/balaji-temple-1.webp",caption="Tirumala Tirupati")
        st.image("https://www.way2temples.com/assets/images/temples-big/bhadradri-sita-ramachandraswamy-temple-bhadrachalam.jpg",caption="Bhadrachalam")
        if st.button("Del Chat 🧺"):
                    st.session_state.messages = []
                    st.success("Chat del ✅")
        Services = {
              "Temple timings 🕝" : "Answer the questions like you are explain open and closing timings and other timings also.",
              "Food 🍛" : "Answer the questions which type of food are present in temple and near temple.",
              "Stay 🏘️" : "Answer the questions about where to stay with total information.",
              "Washrooms 🚻" : "Answer the question about where is washroom are located.",
              "Rules 🚫" : "Answer the question what are the rules should follow in temple.",

        }
        Services = st.selectbox("select a Services", Services.keys())
        uploaded_file = st.file_uploader("upload your ticket...")
        try:
              if uploaded_file:
                    content = uploaded_file.read().decode("utf-8")
                    st.success("file uploaded successfully..")
                    if st.button("Display"):
                        st.text(content)
        except:
              st.error("It is not text file")

        
        if uploaded_file:
                st.write("file uploaded successfully!!")
                if st.button("Display"):
                    context = uploaded_file.read().decode("utf-8")
                    st.text(context)
        st.write("Hi, *Guys!* :sunglasses:")
        st.header("Chat Settings")
if "messages" not in st.session_state:
        st.session_state.messages=[]
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question = st.chat_input("You:")
if question:
    st.session_state.messages.append(
        {"role": "user",
         "content": question}
        
    )
    with st.chat_message("user"):
        st.write(question)
    with st.spinner("Thinking..."):
        response =ollama.chat(
            model= "llama3.2:3b",
                messages = [
                    {"role": "system","content": Serviceses[Services]}]
                    +st.session_state.messages)
        
    st.session_state.messages.append(
            {"role":"assistant",
            "content":response["message"]["content"]
            }
        )
    with st.chat_message("assistant"):
        st.write(response["message"]["content"])

        

    