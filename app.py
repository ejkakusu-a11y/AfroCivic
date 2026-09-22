import streamlit as st

# ---------------------------------------------------------
# Page Configuration & Proprietary Branding
# ---------------------------------------------------------
st.set_page_config(
    page_title="Afro Civic (AFCI)",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling & SVG Logo Integration
st.markdown("""
<style>
    .main-header {
        background-color: #0F172A;
        padding: 1.5rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-text {
        color: #94A3B8;
        font-size: 1.1rem;
    }
    .footer-text {
        text-align: center;
        color: #64748B;
        font-size: 0.85rem;
        padding-top: 2rem;
        border-top: 1px solid #E2E8F0;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# Hero Header with SVG Brand Mark
st.markdown("""
<div class="main-header">
    <svg width="72" height="72" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="100" height="100" rx="20" fill="#0F172A"/>
        <path d="M30 35C35 30 45 28 55 32C65 36 75 30 78 40C80 48 70 58 65 68C60 78 48 82 42 75C36 68 28 62 26 50C24 40 28 37 30 35Z" stroke="#0284C7" stroke-width="4" fill="none"/>
        <line x1="42" y1="45" x2="42" y2="60" stroke="#F59E0B" stroke-width="4" stroke-linecap="round"/>
        <line x1="50" y1="40" x2="50" y2="65" stroke="#10B981" stroke-width="4" stroke-linecap="round"/>
        <line x1="58" y1="47" x2="58" y2="58" stroke="#F59E0B" stroke-width="4" stroke-linecap="round"/>
    </svg>
    <h1 style="margin: 0.5rem 0 0 0; color: #FFFFFF;">Afro Civic (AFCI)</h1>
    <p class="sub-text">Democratizing Civic Engagement & Legislative Clarity Across Africa</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar Navigation & Localization
# ---------------------------------------------------------
st.sidebar.title("Navigation / Urambazaji")
language = st.sidebar.radio("Select Language / Chagua Lugha", ["English", "Kiswahili"])

st.sidebar.markdown("---")
menu_option = st.sidebar.selectbox(
    "Modules" if language == "English" else "Nyanja Kuu",
    [
        "Bill Decoder (Ufafanuzi wa Mswada)",
        "Representative Resolver (Tafuta Mwawakilishi)",
        "Public Participation (Ushiriki wa Umma)",
        "Voice & Accessibility (Sauti na Ufikiaji)"
    ]
)

# ---------------------------------------------------------
# Module 1: Bill Decoder
# ---------------------------------------------------------
if menu_option == "Bill Decoder (Ufafanuzi wa Mswada)":
    if language == "English":
        st.header("📜 Legislative & Policy Bill Decoder")
        st.caption("Upload or paste any parliamentary bill, act, or policy to receive a plain-language summary and impact breakdown.")
        
        bill_text = st.text_area("Paste Legislative Text or Clause here:", height=150, placeholder="e.g., Section 12 of the Proposed Climate & Energy Bill...")
        category = st.selectbox("Select Primary Focus Area:", ["Finance & Tax", "Agriculture & Land", "Health & Social Security", "Governance & Rights"])
        
        if st.button("Decode Bill"):
            if bill_text:
                st.success("Analysis Complete!")
                st.subheader("Key Takeaways in Plain Language")
                st.write("1. **Summary:** This clause outlines community resource allocation frameworks.")
                st.write("2. **Direct Impact:** Citizens will have structured avenues to request local fund audits.")
                st.write("3. **Action Required:** Public feedback open until the end of the current legislative session.")
            else:
                st.warning("Please input text to decode.")
    else:
        st.header("📜 Ufafanuzi wa Miswada na Sheria")
        st.caption("Weka au pakia mswada wa bunge ili kupata muhtasari kwa lugha rahisi na athari zake kwako.")
        
        bill_text = st.text_area("Weka Maandishi ya Mswada hapa:", height=150, placeholder="Mifano: Sehemu ya 12 ya Mswada wa Mazingira...")
        category = st.selectbox("Chagua Eneo Kuu:", ["Fedha na Kodi", "Kilimo na Ardhi", "Afya na Hifadhi ya Jamii", "Utawala na Haki"])
        
        if st.button("Fafanua Mswada"):
            if bill_text:
                st.success("Uchambuzi Umekamilika!")
                st.subheader("Muhtasari kwa Lugha Rahisi")
                st.write("1. **Maelezo:** Sehemu hii inaeleza ugawaji wa rasilimali kwa jamii.")
                st.write("2. **Athari ya Moja kwa Moja:** Wananchi watakuwa na njia rasmi za kuhoji matumizi ya fedha za eneo lao.")
                st.write("3. **Hatua Inayotakiwa:** Maoni ya umma yanapokelewa hadi mwisho wa kikao hiki.")
            else:
                st.warning("Tafadhali weka maandishi ili kufafanua.")

# ---------------------------------------------------------
# Module 2: Representative Resolver
# ---------------------------------------------------------
elif menu_option == "Representative Resolver (Tafuta Mwawakilishi)":
    if language == "English":
        st.header("🏛️ Representative Resolver")
        st.caption("Find your local constituency, county, or ward representatives and their official contact avenues.")
        
        county = st.text_input("Enter your County / Region:", placeholder="e.g., Kitui, Nairobi, Machakos")
        constituency = st.text_input("Enter your Constituency / Sub-County:", placeholder="e.g., Kitui East")
        
        if st.button("Find Representatives"):
            if county or constituency:
                st.info(f"Showing leadership details for {constituency if constituency else county}:")
                st.markdown("- **Member of Parliament (MP):** National Assembly Representative")
                st.markdown("- **Woman Representative:** County Level Oversight")
                st.markdown("- **Senator:** County Resource Guardian")
            else:
                st.warning("Please provide a region or constituency name.")
    else:
        st.header("🏛️ Tafuta Mwawakilishi Wako")
        st.caption("Pata maelezo ya wawakilishi wa eneo bunge lako, kaunti, au wodi pamoja na anwani zao rasmi.")
        
        county = st.text_input("Ingiza Kaunti / Eneo lako:", placeholder="Mfano: Kitui, Nairobi, Machakos")
        constituency = st.text_input("Ingiza Eneo Bunge (Constituency):", placeholder="Mfano: Kitui East")
        
        if st.button("Tafuta Wawakilishi"):
            if county or constituency:
                st.info(f"Orodha ya viongozi wa {constituency if constituency else county}:")
                st.markdown("- **Mbunge (MP):** Muwakilishi wa Bunge la Kitaifa")
                st.markdown("- **Muwakilishi wa Wanawake:** Msimamizi wa Ngazi ya Kaunti")
                st.markdown("- **Seneta:** Mlinzi wa Rasilimali za Kaunti")
            else:
                st.warning("Tafadhali ingiza jina la kaunti au eneo bunge.")

# ---------------------------------------------------------
# Module 3: Public Participation Response Builder
# ---------------------------------------------------------
elif menu_option == "Public Participation (Ushiriki wa Umma)":
    if language == "English":
        st.header("✍️ Public Participation Submission Builder")
        st.caption("Draft structured memorandum submissions for county or national legislative calls for public views.")
        
        topic = st.text_input("Bill or Policy Title:", placeholder="e.g., Finance Bill 2026 Submission")
        concern = st.text_area("What is your primary recommendation or objection?", height=120)
        
        if st.button("Generate Memorandum Draft"):
            if topic and concern:
                st.subheader("Your Generated Memorandum")
                st.code(f"""TO: The Clerk of the Assembly / Senate
RE: SUBMISSION OF PUBLIC PARTICIPATION ON {topic.upper()}

1. INTEREST & STAND
I am writing to submit my formal views regarding {topic}. 

2. KEY RECOMMENDATION / OBJECTION
{concern}

3. CONCLUSION
I request that the committee considers these views in the interest of civic progress and public good.

Submitted by a Concerned Citizen via Afro Civic (AFCI).""", language="markdown")
            else:
                st.warning("Please fill in both the title and your concerns.")
    else:
        st.header("✍️ Mfumo wa Kuwasilisha Maoni ya Umma")
        st.caption("Tengeneza barua au kumbukumbu rasmi ya maoni kwa ajili ya ushiriki wa umma katika serikali ya kaunti au kitaifa.")
        
        topic = st.text_input("Kichwa cha Mswada au Sera:", placeholder="Mfano: Maoni kuhusu Mswada wa Fedha 2026")
        concern = st.text_area("Je, ni pendekezo gani au pingamizi gani kuu ulilo nalo?", height=120)
        
        if st.button("Tengeneza Kumbukumbu ya Maoni"):
            if topic and concern:
                st.subheader("Kumbukumbu Yako Iliyotengenezwa")
                st.code(f"""KWA: Karani wa Bunge
KUHUSU: UWASILISHAJI WA MAONI YA UMMA JUU YA {topic.upper()}

1. DHAMIRA NA MSIMAMO
Mimi kama mwananchi naandika kuwasilisha maoni yangu rasmi kuhusu {topic}.

2. PENDEKEZO / PINGAMIZI KUU
{concern}

3. HITIMISHO
Ninaomba kamati izingatie maoni haya kwa manufaa ya maendeleo ya jamii na haki za wananchi.

Imewasilishwa kupitia Afro Civic (AFCI).""", language="markdown")
            else:
                st.warning("Tafadhali jaza kichwa cha mswada na maoni yako.")

# ---------------------------------------------------------
# Module 4: Voice & Accessibility Integration
# ---------------------------------------------------------
elif menu_option == "Voice & Accessibility (Sauti na Ufikiaji)":
    if language == "English":
        st.header("🎙️ Voice & Accessibility Hub")
        st.info("Voice-first civic engagement allows citizens to listen to bill summaries in local languages or dictate submissions directly.")
        st.write("• **Audio Summaries:** Native Swahili and regional language audio narration pipelines.")
        st.write("• **Low-Bandwidth Mode:** Optimized for offline usage and feature phone / USSD access.")
    else:
        st.header("🎙️ Kituo cha Sauti na Ufikiaji")
        st.info("Ufikiaji kwa njia ya sauti unawawezesha wananchi kusikiliza muhtasari wa miswada kwa lugha za kienyeji au kurekodi maoni yao moja kwa moja.")
        st.write("• **Sauti za Kiswahili:** Usomaji wa miswada kwa Kiswahili sanifu na lugha za maeneo.")
        st.write("• **Njia ya Intaneti Kidogo:** Imewekwa tayari kufanya kazi hata kwenye simu za kawaida (USSD/Offline).")

# ---------------------------------------------------------
# Footer & Legal Notice
# ---------------------------------------------------------
st.markdown("""
<div class="footer-text">
    © 2026 Afro Civic (AFCI). All Rights Reserved. <br>
    <i>Piloting in Kenya | Scaling Pan-Africa</i>
</div>
""", unsafe_allow_html=True)
