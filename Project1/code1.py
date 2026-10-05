import ollama
import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Temple Seva - Digital Temple Guide",
    page_icon="🛕",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Poppins:wght@300;400;500;600&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at top left, #fff1c1 0%, transparent 30%),
        radial-gradient(circle at bottom right, #ffe0b2 0%, transparent 30%),
        #fffaf0;
}


/* Remove default top space */

.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
}


/* ============================================================
   HERO SECTION
   ============================================================ */

.hero {
    background:
        linear-gradient(
            rgba(86, 25, 0, 0.82),
            rgba(128, 38, 0, 0.78)
        ),
        linear-gradient(135deg, #7b1e00, #d97706);

    padding: 65px 30px;
    border-radius: 28px;
    text-align: center;
    color: white;

    box-shadow:
        0 15px 40px rgba(91, 36, 0, 0.25);

    margin-bottom: 30px;
}

.hero-symbol {
    font-size: 65px;
    margin-bottom: 5px;
}

.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 48px;
    margin: 5px;
    letter-spacing: 1px;
}

.hero h3 {
    font-weight: 400;
    font-size: 20px;
    margin-top: 10px;
}

.hero p {
    font-size: 15px;
    opacity: 0.9;
}


/* ============================================================
   SECTION TITLE
   ============================================================ */

.section-title {
    text-align: center;
    margin: 35px 0 20px 0;
}

.section-title h2 {
    font-family: 'Playfair Display', serif;
    color: #7b1e00;
    font-size: 32px;
}

.section-title p {
    color: #76594b;
}


/* ============================================================
   INFORMATION CARDS
   ============================================================ */

.info-card {
    background: rgba(255,255,255,0.9);
    padding: 25px 18px;
    border-radius: 22px;

    text-align: center;

    min-height: 190px;

    border: 1px solid #f4d9a6;

    box-shadow:
        0 8px 25px rgba(94, 45, 0, 0.09);

    transition: all 0.3s ease;
}

.info-card:hover {
    transform: translateY(-8px);

    box-shadow:
        0 18px 35px rgba(94, 45, 0, 0.16);

    border-color: #e5a83b;
}

.card-icon {
    font-size: 42px;
}

.info-card h3 {
    color: #7b1e00;
    font-family: 'Playfair Display', serif;
    font-size: 21px;
}

.info-card p {
    color: #735b4c;
    font-size: 13px;
}


/* ============================================================
   SPECIAL HIGHLIGHT
   ============================================================ */

.highlight {
    background:
        linear-gradient(
            135deg,
            #fff0bd,
            #fff9e7
        );

    padding: 28px;
    border-radius: 22px;

    border-left: 6px solid #d68b00;

    box-shadow:
        0 8px 25px rgba(95, 54, 0, 0.08);

    margin-top: 25px;
}

.highlight h3 {
    color: #7b1e00;
    font-family: 'Playfair Display', serif;
}


/* ============================================================
   CHATBOT
   ============================================================ */

.chat-container {
    background: white;

    border-radius: 25px;

    padding: 25px;

    box-shadow:
        0 12px 35px rgba(83, 36, 0, 0.12);

    border: 1px solid #f2d9ac;

    margin-top: 20px;
}

.chat-title {
    background:
        linear-gradient(
            135deg,
            #7b1e00,
            #c85b09
        );

    color: white;

    padding: 20px;

    border-radius: 18px;

    text-align: center;

    margin-bottom: 20px;
}

.chat-title h2 {
    font-family: 'Playfair Display', serif;
    margin: 0;
}

.chat-title p {
    margin: 5px;
    opacity: 0.9;
}


/* BOT MESSAGE */

.bot-message {
    background: #fff1cf;

    padding: 15px 18px;

    border-radius: 18px 18px 18px 4px;

    margin: 10px 0;

    color: #55351e;

    border: 1px solid #f1d49b;
}


/* USER MESSAGE */

.user-message {
    background:
        linear-gradient(
            135deg,
            #7b1e00,
            #bd4e08
        );

    color: white;

    padding: 15px 18px;

    border-radius: 18px 18px 4px 18px;

    margin: 10px 0;

    margin-left: 20%;

    box-shadow:
        0 5px 15px rgba(91, 30, 0, 0.15);
}


/* ============================================================
   QUICK BUTTONS
   ============================================================ */

.quick-title {
    color: #7b1e00;
    font-weight: 600;
    margin-top: 20px;
}


/* ============================================================
   VISITOR GUIDE
   ============================================================ */

.guide-box {
    background: white;

    padding: 25px;

    border-radius: 22px;

    box-shadow:
        0 8px 25px rgba(80, 40, 0, 0.08);

    border: 1px solid #f0d7aa;

    height: 100%;
}

.guide-box h3 {
    color: #7b1e00;
    font-family: 'Playfair Display', serif;
}

.guide-box li {
    margin: 9px 0;
    color: #644c3c;
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {
    background:
        linear-gradient(
            135deg,
            #4a1600,
            #762600
        );

    color: white;

    padding: 35px;

    text-align: center;

    border-radius: 25px;

    margin-top: 40px;
}

.footer h2 {
    font-family: 'Playfair Display', serif;
}

.footer p {
    opacity: 0.85;
}


/* ============================================================
   STREAMLIT BUTTON
   ============================================================ */

.stButton > button {

    background:
        linear-gradient(
            135deg,
            #8b2500,
            #d97706
        );

    color: white;

    border: none;

    border-radius: 14px;

    padding: 10px 20px;

    font-weight: 600;

    transition: 0.3s;
}

.stButton > button:hover {

    transform: translateY(-2px);

    box-shadow:
        0 8px 20px rgba(117, 38, 0, 0.25);
}


/* ============================================================
   CHAT INPUT
   ============================================================ */

.stChatInput {
    border-radius: 15px;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 700px) {

    .hero h1 {
        font-size: 34px;
    }

    .hero {
        padding: 45px 15px;
    }

    .user-message {
        margin-left: 5%;
    }

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<div class="hero-symbol">🛕</div>

<h1>Temple Seva</h1>

<h3>Your Digital Temple Guide</h3>

<p>
🙏 Discover • Plan • Pray • Experience 🙏
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# WELCOME
# ============================================================

st.markdown("""
<div class="section-title">

<h2>🙏 Welcome, Devotee</h2>

<p>
Everything you need for a peaceful and comfortable temple visit.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# INFORMATION CARDS
# ============================================================

cards = [
    ("🕐", "Temple Timings", "Opening, darshan and closing timings"),
    ("🍚", "Food & Annadanam", "Food menu and serving timings"),
    ("🚻", "Washrooms", "Clean and accessible washroom locations"),
    ("🏨", "Stay & Rooms", "Accommodation and guest house information"),
    ("🙏", "Darshan", "Darshan timings and queue information"),
    ("👗", "Dress Code", "Know what to wear before visiting"),
    ("🚗", "Parking", "Parking information for visitors"),
    ("💧", "Drinking Water", "Find drinking water facilities"),
]


cols = st.columns(4)

for i, card in enumerate(cards):

    with cols[i % 4]:

        st.markdown(f"""
        <div class="info-card">

        <div class="card-icon">
        {card[0]}
        </div>

        <h3>
        {card[1]}
        </h3>

        <p>
        {card[2]}
        </p>

        </div>

        <br>
        """, unsafe_allow_html=True)


# ============================================================
# TODAY'S HIGHLIGHT
# ============================================================

st.markdown("""
<div class="highlight">

<h3>🌸 Today's Temple Highlights</h3>

<p>
🪔 Morning Pooja — <b>6:00 AM</b>
&nbsp;&nbsp; | &nbsp;&nbsp;
🙏 Special Darshan — <b>7:00 AM</b>
&nbsp;&nbsp; | &nbsp;&nbsp;
🍚 Annadanam — <b>12:00 PM</b>
</p>

<p>
✨ Please arrive early during weekends and festival days.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# VISITOR GUIDE
# ============================================================

st.markdown("""
<div class="section-title">

<h2>🧳 New Visitor Guide</h2>

<p>
Helpful information before entering the temple.
</p>

</div>
""", unsafe_allow_html=True)


guide1, guide2, guide3 = st.columns(3)


with guide1:

    st.markdown("""
    <div class="guide-box">

    <h3>🎒 What to Carry</h3>

    <ul>
    <li>Valid ID proof</li>
    <li>Water bottle</li>
    <li>Required medicines</li>
    <li>Small amount of cash</li>
    <li>Temple booking details</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)


with guide2:

    st.markdown("""
    <div class="guide-box">

    <h3>🚫 Things to Avoid</h3>

    <ul>
    <li>Plastic items where prohibited</li>
    <li>Photography in restricted areas</li>
    <li>Outside food where prohibited</li>
    <li>Loud conversations</li>
    <li>Disrespectful behaviour</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)


with guide3:

    st.markdown("""
    <div class="guide-box">

    <h3>🌼 Visitor Tips</h3>

    <ul>
    <li>Wear comfortable traditional clothing</li>
    <li>Reach early for darshan</li>
    <li>Keep your belongings safe</li>
    <li>Follow temple instructions</li>
    <li>Respect the sacred surroundings</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# CHATBOT
# ============================================================

st.markdown("""
<div class="section-title">

<h2>🤖 Ask Temple Seva</h2>

<p>
Your personal temple assistant is ready to help.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# BOT RESPONSE FUNCTION
# ============================================================

def get_response(question):

    question = question.lower()


    # TIMINGS
    if any(word in question for word in
           ["timing", "time", "open", "close"]):

        return """
🕐 **Temple Timings**

🌅 Opening: **5:00 AM**

🙏 Morning Darshan: **5:30 AM – 12:00 PM**

🌆 Evening Darshan: **4:00 PM – 9:00 PM**

🌙 Closing: **9:00 PM**

⚠️ Timings may change during festivals and special occasions.
"""


    # FOOD
    elif any(word in question for word in
             ["food", "annadanam", "breakfast", "lunch", "dinner", "menu"]):

        return """
🍚 **Annadanam & Food**

🌅 Breakfast: **7:30 AM – 9:30 AM**

☀️ Lunch: **12:00 PM – 2:30 PM**

🌙 Dinner: **7:00 PM – 8:30 PM**

📍 Location: Annadanam Hall

**Today's Sample Menu**

🍚 Rice  
🥣 Dal  
🥕 Vegetable Curry  
🥘 Sambar  
🥛 Curd  
🍬 Sweet
"""


    # WASHROOM
    elif any(word in question for word in
             ["washroom", "toilet", "restroom"]):

        return """
🚻 **Washroom Information**

Separate facilities are available for:

👨 Men

👩 Women

♿ Accessible visitors

📍 Main Entrance  
📍 Annadanam Hall  
📍 Parking Area
"""


    # STAY
    elif any(word in question for word in
             ["stay", "room", "hotel", "accommodation"]):

        return """
🏨 **Accommodation**

Visitors can choose from:

🏠 Temple Guest Rooms

🛏️ Dormitory

🏨 Nearby Hotels

🕐 Check-in: **12:00 PM**

🕚 Check-out: **11:00 AM**

Please confirm availability before visiting.
"""


    # DARSHAN
    elif any(word in question for word in
             ["darshan", "queue", "ticket"]):

        return """
🙏 **Darshan Information**

🌸 General Darshan — Available

✨ Special Darshan — Available

🎟️ Tickets may be available through
the temple counter or official booking system.

💡 Tip: Visit early to avoid long queues.
"""


    # DRESS
    elif any(word in question for word in
             ["dress", "clothes", "wear"]):

        return """
👗 **Dress Code**

Visitors are requested to wear
clean and modest clothing.

👨 Men:
Traditional or modest clothing.

👩 Women:
Saree, salwar or other modest clothing.

🙏 Please follow the temple's specific dress rules.
"""


    # PARKING
    elif any(word in question for word in
             ["parking", "car", "bike", "vehicle"]):

        return """
🚗 **Parking**

Parking may be available for:

🏍️ Two-wheelers

🚗 Cars

🚌 Buses

📍 Follow temple parking signs.

🙏 Please follow security staff instructions.
"""


    # FACILITIES
    elif any(word in question for word in
             ["facility", "water", "shoe", "cloakroom", "wheelchair"]):

        return """
⭐ **Temple Facilities**

💧 Drinking Water

👟 Shoe Stand

🧳 Cloakroom

🚻 Washrooms

♿ Wheelchair Assistance

🏥 First Aid

🔎 Lost & Found

🚗 Parking

🍚 Annadanam
"""


    # DIRECTIONS
    elif any(word in question for word in
             ["direction", "location", "reach", "map"]):

        return """
📍 **Temple Directions**

You can reach the temple by:

🚌 Bus

🚆 Train

🚕 Taxi / Auto

🚗 Private Vehicle

🗺️ Please use the temple's official map
for accurate directions.
"""


    # HELLO
    elif any(word in question for word in
             ["hello", "hi", "namaste", "help"]):

        return """
🙏 **Namaste! Welcome to Temple Seva.**

I can help you with:

🕐 Temple Timings

🍚 Food & Annadanam

🚻 Washrooms

🏨 Accommodation

🙏 Darshan

👗 Dress Code

🚗 Parking

💧 Drinking Water

📍 Directions

✨ What would you like to know?
"""


    else:

        return """
🙏 I am still learning.

Try asking me:

🕐 "What are the temple timings?"

🍚 "When is Annadanam?"

🚻 "Where are the washrooms?"

🏨 "Where can I stay?"

🙏 "What is the darshan timing?"

👗 "What is the dress code?"

🚗 "Where is parking?"
"""


# ============================================================
# CHAT HISTORY
# ============================================================

if "chat_history" not in st.session_state:

    st.session_state.chat_history = [

        {
            "role": "bot",
            "message":
            "🙏 Namaste! Welcome to Temple Seva. How can I help you today?"
        }

    ]


# ============================================================
# DISPLAY CHAT
# ============================================================

st.markdown('<div class="chat-container">', unsafe_allow_html=True)

st.markdown("""
<div class="chat-title">

<h2>🤖 Temple Seva Assistant</h2>

<p>Ask anything about your temple visit</p>

</div>
""", unsafe_allow_html=True)


for chat in st.session_state.chat_history:

    if chat["role"] == "bot":

        st.markdown(
            f"""
            <div class="bot-message">
            {chat["message"]}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="user-message">
            {chat["message"]}
            </div>
            """,
            unsafe_allow_html=True
        )


st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
# QUICK QUESTIONS
# ============================================================

st.markdown(
    '<p class="quick-title">✨ Quick Questions</p>',
    unsafe_allow_html=True
)


q1, q2, q3, q4 = st.columns(4)


quick_questions = [
    ("🕐 Timings", "What are the temple timings?"),
    ("🍚 Food", "When is Annadanam?"),
    ("🚻 Washrooms", "Where are the washrooms?"),
    ("🏨 Stay", "Where can I stay?")
]


for column, (button_text, question) in zip(
    [q1, q2, q3, q4],
    quick_questions
):

    with column:

        if st.button(button_text, use_container_width=True):

            st.session_state.chat_history.append(
                {
                    "role": "user",
                    "message": question
                }
            )

            st.session_state.chat_history.append(
                {
                    "role": "bot",
                    "message": get_response(question)
                }
            )

            st.rerun()


# ============================================================
# CHAT INPUT
# ============================================================

question = st.chat_input(
    "💬 Ask your temple question..."
)


if question:

    st.session_state.chat_history.append(
        {
            "role": "user",
            "message": question
        }
    )

    answer = get_response(question)

    st.session_state.chat_history.append(
        {
            "role": "bot",
            "message": answer
        }
    )

    st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

<h2>🛕 Temple Seva</h2>

<p>
Your digital companion for a peaceful temple visit.
</p>

<p>
🙏 Pray • Explore • Experience • Remember 🙏
</p>

<p>
© 2026 Temple Guidance System
</p>

</div>
""", unsafe_allow_html=True)

with st.sidebar:
        if st.button("Del Chat 🧺"):
                            st.session_state.messages = []
                            st.success("Chat del ✅")
        
        st.header(":blue[Temples 🛕]")
        st.image("https://c8.alamy.com/comp/2WH6E1N/view-kakatiya-rudreshwara-temple-or-ramappa-temple-palampet-warangal-telangana-india-2WH6E1N.jpg", caption="Rudreshwara Temple")
        st.image("https://tirupatibalajitravels.co.in/wp-content/uploads/2024/01/balaji-temple-1.webp",caption="Tirumala Tirupati")
        st.image("https://www.way2temples.com/assets/images/temples-big/bhadradri-sita-ramachandraswamy-temple-bhadrachalam.jpg",caption="Bhadrachalam")
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