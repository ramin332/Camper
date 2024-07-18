import streamlit as st
import matplotlib.pyplot as plt
st.set_page_config(layout='wide')
st.title("Vakantiekosten Vergelijking: Camper vs. Vliegen")

col1, col2 = st.columns(2)
with col1:
    # Algemeen
    st.header("Algemeen")
    dagelijkse_kosten_eten_drinken_totaal = st.number_input("Dagelijkse Kosten voor Eten en Drinken totaal (€)", min_value=0, value=75) 
    aantal_dagen = st.slider('Aantal dagen', 2, 14, 7)
    aantal_personen = st.slider('Aantal personen', 1, 4, 2)

    # Invoer voor Camper
    st.header("Kosten Camper")
    kosten_camper_per_dag = st.number_input("Kosten Camper per Dag totaal (€)", min_value=0, value= 100)  # Assuming the original 1166 was for 13 days
    benzine_kosten_per_liter = st.number_input("Benzine Kosten per Liter (€)", min_value=0.0, value=2.0)
    benzineverbruik_per_100_km = st.number_input("Benzineverbruik per 100 km (L)", min_value=0.0, value=8.0)
    totale_afstand = st.number_input("Totale Afstand (km)", min_value=0, value=2000)
    gemiddelde_kosten_per_staplaats_per_dag = st.number_input("Gemiddelde Kosten per Staplaats per Dag totaal (€)", min_value=0, value=40)
    
    with st.popover("Onbeperkt km"):
        onbeperkt_km= st.toggle("Onbeperkte km?")
        if (onbeperkt_km == False):
            gratis_km = st.number_input("Gratis km", min_value=0, value=500)
            kostenextrakm = st.number_input("Extra kosten pkm (€)", min_value=0.00, value=0.0015, step=0.0001, format="%.4f")
            totale_kosten_extra_km = ((totale_afstand-gratis_km)*kostenextrakm)
        else:
            totale_kosten_extra_km = 0
    # Berekeningen Camper
    totale_benzine_kosten = ((totale_afstand / 100) * benzineverbruik_per_100_km * benzine_kosten_per_liter) 
    totale_kosten_camper = kosten_camper_per_dag * aantal_dagen
    staplaatskosten = gemiddelde_kosten_per_staplaats_per_dag * aantal_dagen
    totale_kosten_camper_huren = totale_kosten_camper + totale_benzine_kosten + totale_kosten_extra_km +  staplaatskosten + (dagelijkse_kosten_eten_drinken_totaal * aantal_dagen) 
    totale_kosten_camper_huren_per_persoon = totale_kosten_camper_huren / aantal_personen
    
    # Invoer voor Vliegen
    st.header("Kosten Vliegen")
    kosten_vlucht_retour = st.number_input("Kosten vlucht retour p.p (€)", min_value=0, value=750)
    kosten_kites_meenemen_vliegtuig = st.number_input("Kosten voor Kites meenemen in het vliegtuig p.p (€)", min_value=0, value=100)
    kosten_auto_huren = st.number_input("Kosten auto huren per dag totaal (€)", min_value=0, value=50)
    kosten_verblijf_per_nacht = st.number_input("Kosten per nacht totaal (€)", min_value=0, value=85)
    totale_kosten_vliegen = (dagelijkse_kosten_eten_drinken_totaal * aantal_dagen) + kosten_vlucht_retour*2 + (kosten_verblijf_per_nacht * aantal_dagen) + kosten_kites_meenemen_vliegtuig*2 + (kosten_auto_huren * aantal_dagen)
    totale_kosten_per_persoon_vliegen = totale_kosten_vliegen/2
    # Berekeningen Vliegen
    beschikbaar_budget_vliegen = totale_kosten_camper_huren_per_persoon - totale_kosten_per_persoon_vliegen
with col2:


    st.header("Resultaten")

    # Maak een lijst van dictionaries voor de resultaten
    results = [
        {"Type reis": "Camper", "Totale kosten per persoon (€)": f"€{totale_kosten_camper_huren_per_persoon:.0f}"},
        {"Type reis": "Vliegen", "Totale kosten per persoon (€)": f"€{totale_kosten_per_persoon_vliegen:.0f}"},
        {"Type reis": "Verschil (Camper vs Vliegen)", "Totale kosten per persoon (€)": f"€{beschikbaar_budget_vliegen:.0f}"}
    ]

    # Toon de resultaten als een tabel in Streamlit
    st.table(results)


    labels = ['Camper', 'Vliegen']
    costs = [totale_kosten_camper_huren_per_persoon, totale_kosten_per_persoon_vliegen]

    fig, ax = plt.subplots()
    ax.bar(labels, costs, color=['blue', 'green'])
    ax.set_ylabel('Kosten (€)')
    ax.set_title('Vergelijking van Vakantiekosten per Persoon')
    st.pyplot(fig)

