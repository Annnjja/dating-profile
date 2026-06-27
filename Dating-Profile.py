import streamlit as s

# --- 1. DESIGN & HINTERGRUND (CSS) ---
s.markdown(
    """
    <style>
    /* Elegante und romantische Schriftart direkt von Google Fonts laden */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');

    /* Hintergrund & neue Schriftart für die gesamte App erzwingen */
    .stApp {
        background: radial-gradient(circle, red 0%, darkred 100%) !important;
    }
    
    .stApp, .stApp * {
        font-family: 'Playfair Display', serif !important;
    }
    
    /* Haupttexte auf der Seite weiß und zentriert */
    h1, h2, h3, h4, p {
        color: white !important;
        text-align: center !important;
        margin-bottom: 20px !important;
    }
    
    /* Zentrierung des Hauptinhalts auf der Seite */
    .block-container {
        max-width: 800px !important;
        margin: 0 auto !important;
        padding-top: 5rem !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
    }   
    
    /* Extra Klasse, um den "Sprich mich an"-Text schwarz zu färben */
    .schwarzer-text h3 {
        color: black !important;
    }
    
    /* ZENTRIERUNG FÜR DIE UNTEREINANDER-BUTTONS ("Frauen", "Männer", "Alle") */
    [data-testid="stVerticalBlock"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 100% !important;
    }

    /* ZENTRIERUNG FÜR DIE NEBENEINANDER-BUTTONS ("Ja" / "Nein") */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        justify-content: center !important;
        gap: 5px !important;
        width: 100% !important;
    }
    
    [data-testid="column"] {
        flex: 0 0 auto !important;
        width: auto !important;
    }

    /* ALLGEMEINES BUTTON-CONTAINER LAYOUT */
    div.stButton {
        display: flex !important;
        justify-content: center !important;
        width: 100% !important;
        margin: 5px 0 !important;
    }

    /* ABSOLUTE KONTROLLE ÜBER DAS BUTTON-DESIGN */
    div.stButton > button {
        width: 220px !important; 
        height: 55px !important;  
        background-color: white !important;
        border-radius: 15px !important; 
        border: none !important;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3) !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }

    /* Text im Button auf Darkred zwingen */
    div.stButton > button p,
    div.stButton > button span,
    div.stButton > button div {
        color: darkred !important;
        font-size: 20px !important; 
        font-weight: bold !important;
        text-align: center !important;
        margin: 0 !important;
        padding: 0 !important;
        width: 100% !important;
    }
    
    /* HOVER-EFFEKT: Wird beim Überfahren rot */
    div.stButton > button:hover {
        background-color: red !important;
    }
    
    div.stButton > button:hover p,
    div.stButton > button:hover span,
    div.stButton > button:hover div {
        color: darkred !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Platzhalter für deinen späteren Bild-Hintergrund bei "JA" ---
def setze_bild_hintergrund():
    s.markdown(
        """
        <style>
        .stApp {
            background: url('https://www.w3schools.com/howto/img_girl.jpg') !important;
            background-size: cover !important;
            background-position: center !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# --- 2. ZUSTAND SPEICHERN ---
if "schritt" not in s.session_state:
    s.session_state.schritt = "start"

# --- 3. LOGIK & ABLAUF ---

# ERSTE FRAGE
if s.session_state.schritt == "start":
    s.write("### Findest du die Person vor dir attraktiv?")
    
    col1, col2 = s.columns(2)
    with col1:
        if s.button("Ja", key="ja_btn"):
            s.session_state.schritt = "ja_seite"
            s.rerun()
    with col2:
        if s.button("Nein", key="nein_btn"):
            s.session_state.schritt = "nein_seite"
            s.rerun()

# ANTWORT JA
elif s.session_state.schritt == "ja_seite":
    setze_bild_hintergrund()
    s.write("### Sprich mich an! :)")

# ANTWORT NEIN (Geschlechter-Auswahl)
elif s.session_state.schritt == "nein_seite":
    s.write("### Kein Problem, hier sind ein paar meiner single Freundinnen und Freunde:")
    s.write("") 
    s.write("#### Welches Geschlecht datest du?")
    
    if s.button("Frauen", key="frauen_btn"):
        s.session_state.schritt = "galerie_frauen"
        s.rerun()
    if s.button("Männer", key="maenner_btn"):
        s.session_state.schritt = "maenner_alle"
        s.rerun()
    if s.button("Alle", key="alle_btn"):
        s.session_state.schritt = "galerie_alle"
        s.rerun()

# GALERIE: FRAUEN
elif s.session_state.schritt == "galerie_frauen":
    s.write("### Single Frauen:")
    s.image("https://via.placeholder.com/300x400", caption="Name, Alter")

# GALERIE: MÄNNER
elif s.session_state.schritt == "maenner_alle":
    s.write("### Single Männer:")
    s.image("https://via.placeholder.com/300x400", caption="Name, Alter")

# GALERIE: ALLE
elif s.session_state.schritt == "galerie_alle":
    s.write("### Alle Singles:")
    s.image("https://via.placeholder.com/300x400", caption="Name, Alter")
