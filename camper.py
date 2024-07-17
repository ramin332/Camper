import streamlit as st
import matplotlib.pyplot as plt
st.set_page_config(layout='wide')
st.title("Vakantiekosten Vergelijking: Camper vs. Vliegen")

col1, col2 = st.columns(2)
with col1:
    # Algemeen
    st.header("Algemeen")
    dagelijkse_kosten_eten_drinken_per_persoon = st.number_input("Dagelijkse Kosten voor Eten en Drinken per Persoon (€)", min_value=0, value=35)
    aantal_dagen = st.slider('Aantal dagen', 2, 14, 7)
    aantal_personen = st.slider('Aantal personen', 1, 4, 2)

    # Invoer voor Camper
    st.header("Kosten Camper")
    kosten_camper_per_dag = st.number_input("Kosten Camper per Dag (€)", min_value=0, value=90)  # Assuming the original 1166 was for 13 days
    benzine_kosten_per_liter = st.number_input("Benzine Kosten per Liter (€)", min_value=0.0, value=2.0)
    benzineverbruik_per_100_km = st.number_input("Benzineverbruik per 100 km (L)", min_value=0.0, value=8.0)
    totale_afstand = st.number_input("Totale Afstand (km)", min_value=0, value=2000)
    gemiddelde_kosten_per_staplaats_per_dag = st.number_input("Gemiddelde Kosten per Staplaats per Dag (€)", min_value=0, value=40)

    # Berekeningen Camper
    kosten_camper = kosten_camper_per_dag * aantal_dagen
    benzinekosten = (totale_afstand / 100) * benzineverbruik_per_100_km * benzine_kosten_per_liter
    staplaatskosten = gemiddelde_kosten_per_staplaats_per_dag * aantal_dagen
    totale_kosten_camper = kosten_camper + benzinekosten + staplaatskosten + (dagelijkse_kosten_eten_drinken_per_persoon * aantal_dagen * aantal_personen)
    totale_kosten_per_persoon_camper = totale_kosten_camper / aantal_personen
    
    # Invoer voor Vliegen
    st.header("Kosten Vliegen")
    #totale_budget_per_persoon_vliegen = st.number_input("Totale Budget per Persoon voor Vliegen (€)", min_value=0, value=1500)
    kosten_vlucht_retour = st.number_input("Kosten vlucht retour (€)", min_value=0, value=750)
    kosten_auto_huren = st.number_input("Kosten auto huren per dag (€)", min_value=0, value=50)
    kosten_verblijf_per_nacht = st.number_input("Kosten per nacht per Persoon (€)", min_value=0, value=40)
    kosten_kites_meenemen_vliegtuig = st.number_input("Kosten voor Kites meenemen in het vliegtuig (€)", min_value=0, value=100)
    totale_kosten_per_persoon_vliegen = dagelijkse_kosten_eten_drinken_per_persoon + kosten_vlucht_retour + (kosten_verblijf_per_nacht * aantal_dagen)/aantal_personen + kosten_kites_meenemen_vliegtuig + (kosten_auto_huren * aantal_dagen)/aantal_personen
    # Berekeningen Vliegen
    beschikbaar_budget_vliegen = totale_kosten_per_persoon_camper - totale_kosten_per_persoon_vliegen
with col2:


    st.header("Resultaten")

    # Maak een lijst van dictionaries voor de resultaten
    results = [
        {"Type reis": "Camper", "Totale kosten per persoon (€)": f"€{totale_kosten_per_persoon_camper:.0f}"},
        {"Type reis": "Vliegen", "Totale kosten per persoon (€)": f"€{totale_kosten_per_persoon_vliegen:.0f}"},
        {"Type reis": "Verschil (Camper vs Vliegen)", "Totale kosten per persoon (€)": f"€{beschikbaar_budget_vliegen:.0f}"}
    ]

    # Toon de resultaten als een tabel in Streamlit
    st.table(results)


    labels = ['Camper', 'Vliegen']
    costs = [totale_kosten_per_persoon_camper, totale_kosten_per_persoon_vliegen]

    fig, ax = plt.subplots()
    ax.bar(labels, costs, color=['blue', 'green'])
    ax.set_ylabel('Kosten (€)')
    ax.set_title('Vergelijking van Vakantiekosten per Persoon')
    st.pyplot(fig)
