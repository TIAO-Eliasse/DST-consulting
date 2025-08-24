import streamlit as st

# Titre principal
st.set_page_config(page_title="Site web", layout="wide")
# Créer une barre de navigation horizontale




# --- Définition des couleurs et police ---
primary_color = "#D28E8E"
background_color = "#5C8A59"
secondary_background_color = "#F0F2F6"
text_color = "#31333F"
font_family = "sans-serif" # Correspond à "Sans empattement"

# --- Injection de CSS personnalisé ---
st.markdown(
    f"""
    <style>
    /* Général (corps de la page) */
    body {{
        color: {text_color};
        background-color: {background_color};
        font-family: {font_family};
    }}

    /* Styles pour le conteneur principal de Streamlit */
    .stApp {{
        background-color: {background_color};
        color: {text_color};
        font-family: {font_family};
    }}

    /* Barre latérale et éléments similaires (secondary_background_color) */
    .stSidebar {{
        background-color: {secondary_background_color};
        color: {text_color}; /* Le texte dans la sidebar devrait être lisible */
    }}

    .st-emotion-cache-16txt3u {{ /* Cible le fond des conteneurs par exemple */
        background-color: {secondary_background_color};
    }}

    .st-emotion-cache-zq5wmm {{ /* Cible le fond des conteneurs par exemple */
        background-color: {secondary_background_color};
    }}

    /* Boutons (primary_color) */
    .stButton>button {{
        background-color: {primary_color};
        color: white; /* Texte blanc sur bouton primaire pour un bon contraste */
        border: none;
    }}

    /* Curseurs (sliders) - la couleur principale est souvent utilisée ici */
    .stSlider>div>div>div>div {{ /* La barre du curseur */
        background-color: {primary_color};
    }}
    .stSlider>div>div>div>div>div[data-testid="stSliderHandle"] {{ /* Le "pouce" du curseur */
        background-color: {primary_color};
    }}

    /* Entrées de texte, zones de texte (peut aussi utiliser primaryColor ou textColor) */
    .stTextInput>div>div>input {{
        color: {text_color};
        background-color: {secondary_background_color};
        border-color: {primary_color}; /* Bordure pour les inputs */
    }}
    .stTextArea>div>div>textarea {{
        color: {text_color};
        background-color: {secondary_background_color};
        border-color: {primary_color};
    }}

    /* Titres (H1, H2, etc.) */
    h1, h2, h3, h4, h5, h6 {{
        color: {primary_color}; /* Utiliser la couleur primaire pour les titres peut être sympa */
        font-family: {font_family};
    }}

    /* Texte général */
    p, li, div, span {{
        color: {text_color};
        font-family: {font_family};
    }}

    /* Liens */
    a {{
        color: {primary_color};
    }}

    /* Expander / Checkbox / Radio / Selectbox */
    .st-emotion-cache-1f1c24p, /* Checkbox label */
    .st-emotion-cache-1cpxd0t, /* Radio label */
    .st-emotion-cache-1oe5f0g, /* Selectbox label */
    .st-emotion-cache-1c09d5y, /* Expander header */
    .st-emotion-cache-1y4y1h6 {{ /* Expander header content */
        color: {text_color};
    }}

    .st-emotion-cache-v0n0as, /* Background of selectbox options */
    .st-emotion-cache-j9f0gy,
    .st-emotion-cache-1c9s62z {{ /* Hover background of selectbox options */
        background-color: {secondary_background_color} !important;
        color: {text_color} !important;
    }}

    /* La couleur de survol pour les options sélectionnées */
    .st-emotion-cache-1c9s62z:hover {{
        background-color: {primary_color} !important;
        color: white !important;
    }}

    /* Éléments st.container avec bordure */
    .stContainer {{
        background-color: {secondary_background_color};
        border: 1px solid {primary_color}; /* Ajoute une bordure pour distinguer */
    }}
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-list"] {
        justify-content: space-around;
    }
    </style>
    """, unsafe_allow_html=True)

import streamlit as st

# Créer une barre de navigation horizontale qui occupe toute la largeur
col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 2])  # Colonnes avec un poids égal

# Ajouter des boutons dans chaque colonne
with col1:
    if st.button("Page d'accueil"):
        page = "Page d'accueil"
with col2:
    if st.button("Nos services"):
        page = "Nos services"
with col3:
    if st.button("Nos études"):
        page = "Nos études"
with col4:
    if st.button("Témoignages"):
        page = "Témoignages"
with col5:
    if st.button("Contact"):
        page = "Contact"

# Si aucune page n'est sélectionnée, définir la page par défaut
if 'page' not in locals():
    page = "Page d'accueil"

# Fonction pour afficher chaque page
def page_accueil():
    st.header("Bienvenue à DST Consulting")

def page_services():
    st.header("Nos Services")

def page_etudes():
    st.header("Nos Études")

def page_temignages():
    st.header("Témoignages")

def page_contact():
    st.header("Contact")

# Affichage de la page selon la sélection
if page == "Page d'accueil":
    page_accueil()
elif page == "Nos services":
    page_services()
elif page == "Nos études":
    page_etudes()
elif page == "Témoignages":
    page_temignages()
elif page == "Contact":
    page_contact()

# Si aucune page n'est sélectionnée, définir la page par défaut
if 'page' not in locals():
    page = "Page d'accueil"

# Fonctions pour chaque page
def page_accueil():
    with st.container():
        st.header("DST Consulting")
        st.subheader("Data StoryTellers Consulting")
        st.write("**We make data talk, you take informed decisions**")

        st.write("### Description")
        st.write("""
            La DST Consulting, en version longue **Data StoryTellers Consulting**, est une équipe de jeunes Africains passionnés de data et désireux de contribuer activement à l’émancipation du continent à travers une révolution de la data.
        """)

        st.write("### Vision")
        st.write("""
            La DST Consulting œuvre pour une Afrique où la donnée – de qualité – n’est pas juste collectée, mais convenablement traitée, rendue disponible, étudiée, interprétée et élégamment présentée.
            Ceci afin de permettre des décisions de mieux en mieux éclairées, des politiques bien pensées, des stratégies à fort impact, pour une Afrique avertie, crédible sur la scène internationale, indépendante, fière et prospère.
        """)

        st.write("### Mission")
        st.write("""
            Motivée par cette vision, la DST Consulting s’engage à accompagner aussi bien les administrations publiques que les entreprises privées dans une collecte et/ou un traitement des données qu’elles utilisent alliant rigueur, technique et professionnalisme, tout en étant conscient des spécificités locales.
            Notre rôle est alors de rendre les données accessibles, compréhensibles et actionnables, notamment grâce à :
        """)
        st.write("""
            - **Des visualisations claires et percutantes**
            - **Des modèles statistiques et économétriques adaptés aux besoins**
            - **Des solutions IA sur mesure**
            - **Un appui stratégique dans la gestion et l’exploitation des données**
        """)

        st.write("### Ambitions")
        st.write("""
            Forte de cette mission, guidée par cette vision, la DST Consulting envisage divers accomplissements, à moyen et à long terme :
        """)
        st.write("""
            - **Impact continental** : D’ici 10 ans, contribuer à au moins 100 projets à fort impact économique et social en Afrique.
            - **Excellence technique** : Devenir un pôle d’expertise reconnu pour la qualité et la fiabilité de nos modèles, analyses et solutions IA. La DST obtiendra pour cela au moins 3 certifications qualité d’ici 15 ans.
            - **Renforcement des capacités** : Former et accompagner au moins 500 professionnels et institutions à mieux exploiter la donnée, d’ici 10 ans.
            - **Innovation, durabilité et éthique** : Changer radicalement le point de vue Africain sur la donnée en mettant en relief sa valeur, et militer pour une utilisation responsable.
        """)

        st.write("### Organisation")
        st.write("""
            Pour atteindre ces buts, l’équipe initiale, composée des 5 membres fondateurs, s’organise comme suit :
        """)
        st.write("""
            - **1 Chef(fe)** : Responsable des affaires générales, de l’orientation, de l’organisation et de la coordination (avancement des travaux, respect des délais, implication effective de toute l’équipe, …)
            - **1 Chargé(e) de la Communication et de la coopération**
            - **1 Chargé(e) de la recherche et de l’innovation**
            - **1 Chargé(e) des débouchés et des opportunités**
            - **1 Chargé(e) de l’administration et des finances**
        """)



def page_services():
    with st.container():
        st.write("""
            - **Conception et déploiement de tableaux de bord dynamiques** : Création de visualisations interactives pour une prise de décision rapide et éclairée.
            - **Mise en place de dispositifs de surveillance des GAB** : Développement de systèmes de surveillance pour les Guichets Automatiques Bancaires (GAB), garantissant la sécurité et l'efficacité des opérations.
            - **Développement d’IA génératives à usage privé** : Création de modèles d'intelligence artificielle générative, adaptés à des usages privés, pour l'automatisation de processus complexes.
            - **Accompagnement et conseil financier** : Services de conseil financier pour optimiser la gestion des ressources et les investissements d'entreprises.
            - **Gestion de portefeuille** : Suivi et gestion de portefeuilles d'investissement, en optimisant le rendement et en minimisant les risques.
            - **Suivi et évaluation de projets d’investissement** : Mise en place de mécanismes de suivi et d'évaluation pour garantir la rentabilité et la pérennité des projets d'investissement.
        """)


def page_etudes():
    st.write("Voici quelques-unes de nos études récentes :")

    # Exemple de projet d'étude
    st.subheader("Étude sur la satisfaction des clients")
    st.write("""
        Nous avons réalisé une étude de satisfaction pour une entreprise de télécommunications, mettant en évidence
        les points forts et les axes d'amélioration pour l'amélioration de la relation client.
    """)
    st.subheader("Étude sur le marché des télécommunications")
    st.write("""
        Cette étude portait sur les tendances de consommation des services téléphoniques et internet dans les grandes villes.
    """)

def page_temignages():
    st.write("""
        "Le Cabinet ABC a été d'une grande aide pour notre entreprise. Leur analyse des données a été cruciale pour
        prendre des décisions stratégiques importantes."
        - Client 1, Entreprise XYZ
    """)
    st.write("""
        "Nous avons apprécié leur approche analytique et la qualité de leurs rapports détaillés. Très professionnel !"
        - Client 2, Entreprise 123
    """)

def page_contact():
    st.write("Pour toute demande, n'hésitez pas à remplir le formulaire ci-dessous ou à nous contacter directement.")
    nom = st.text_input("Nom")
    email = st.text_input("Email")
    message = st.text_area("Message")

    if st.button('Envoyer'):
        if nom and email and message:
            st.success("Votre message a été envoyé ! Nous vous répondrons dans les plus brefs délais.")
        else:
            st.error("Veuillez remplir tous les champs avant d'envoyer.")

# Affichage de la page en fonction du choix
if page == "Page d'accueil":
    page_accueil()
elif page == "Nos services":
    page_services()
elif page == "Nos études":
    page_etudes()
elif page == "Témoignages":
    page_temignages()
elif page == "Contact":
    page_contact()
