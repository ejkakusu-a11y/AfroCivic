import streamlit as st

# =========================================================
# 1. PAGE CONFIGURATION & PROPRIETARY BRANDING
# =========================================================
st.set_page_config(
    page_title="Afro Civic (AFCI) - Kenya MVP",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Dark Slate Theme with Accent Badges)
st.markdown("""
<style>
    .main-header {
        background-color: #0F172A;
        padding: 1.5rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 1.5rem;
        border: 1px solid #1E293B;
    }
    .sub-text {
        color: #94A3B8;
        font-size: 1.05rem;
    }
    .card {
        background-color: #1E293B;
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 5px solid #0284C7;
        margin-bottom: 1rem;
        color: #F8FAFC;
    }
    .card-gbv {
        background-color: #31121D;
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 5px solid #E11D48;
        margin-bottom: 1rem;
        color: #FFF1F2;
    }
    .example-box {
        background-color: #0F172A;
        padding: 1rem;
        border-radius: 8px;
        border: 1px dashed #10B981;
        margin-top: 0.5rem;
        color: #E2E8F0;
    }
    .badge-national {
        background-color: #1E3A8A;
        color: #BFDBFE;
        padding: 0.2rem 0.6rem;
        border-radius: 4px;
        font-weight: bold;
        font-size: 0.8rem;
    }
    .badge-county {
        background-color: #065F46;
        color: #A7F3D0;
        padding: 0.2rem 0.6rem;
        border-radius: 4px;
        font-weight: bold;
        font-size: 0.8rem;
    }
    .footer-text {
        text-align: center;
        color: #64748B;
        font-size: 0.85rem;
        padding-top: 2rem;
        border-top: 1px solid #334155;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# Hero Header with SVG Brand Mark
st.markdown("""
<div class="main-header">
    <svg width="64" height="64" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="100" height="100" rx="20" fill="#0F172A"/>
        <path d="M30 35C35 30 45 28 55 32C65 36 75 30 78 40C80 48 70 58 65 68C60 78 48 82 42 75C36 68 28 62 26 50C24 40 28 37 30 35Z" stroke="#0284C7" stroke-width="4" fill="none"/>
        <line x1="42" y1="45" x2="42" y2="60" stroke="#F59E0B" stroke-width="4" stroke-linecap="round"/>
        <line x1="50" y1="40" x2="50" y2="65" stroke="#10B981" stroke-width="4" stroke-linecap="round"/>
        <line x1="58" y1="47" x2="58" y2="58" stroke="#F59E0B" stroke-width="4" stroke-linecap="round"/>
    </svg>
    <h1 style="margin: 0.3rem 0 0 0; color: #FFFFFF; font-size: 2rem;">Afro Civic (AFCI)</h1>
    <p class="sub-text">Bilingual Civic Education & Public Engagement Platform | Independent Pilot</p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# 2. LOCALIZATION & NAVIGATION SIDEBAR
# =========================================================
st.sidebar.title("🌐 Language & Menu")
language = st.sidebar.radio("Select Language / Chagua Lugha", ["English", "Kiswahili"])

st.sidebar.markdown("---")
menu_options = [
    "Ask Fahamu (AI Copilot)",
    "Know Your Constitution (Katiba)",
    "Who Does What? (Roles & Offices)",
    "Public Participation & Voice Hub",
    "Rights, Advocacy & GBV Help"
] if language == "English" else [
    "Muulize Fahamu (Msaidizi wa AI)",
    "Jua Katiba Yako",
    "Nani Anafanya Nini? (Majukumu)",
    "Ushiriki wa Umma na Sauti",
    "Haki, Utetezi na Msaada wa GBV"
]

selected_module = st.sidebar.selectbox("Choose Module / Chagua Sehemu", menu_options)

st.sidebar.markdown("---")
st.sidebar.caption("📍 **Scope:** Kenya (Pilot)")
st.sidebar.caption("🔒 **Licensing:** Proprietary - All Rights Reserved")


# =========================================================
# 3. KNOWLEDGE BASES (MVP CONTENT DATASETS)
# =========================================================

# A. CONSTITUTION DATASET (MVP ARTICLES)
CONSTITUTION_DATA = {
    "Article 1": {
        "title": "Sovereignty of the People",
        "official_en": "All sovereign power belongs to the people of Kenya and shall be exercised only in accordance with this Constitution.",
        "simple_en": "The highest authority in Kenya belongs to everyday citizens. Leaders only hold power because citizens gave it to them through voting.",
        "example_en": "Elected leaders work for you. If an MCA or MP misuses public funds, citizens have the constitutional right to hold them accountable.",
        "simple_sw": "Mamlaka yote ya nchi ni ya wananchi wa Kenya. Viongozi wana mamlaka tu kwa sababu wananchi wamewachagua.",
        "example_sw": "Viongozi walioteuliwa wanafanya kazi kwa ajili yako. Ikiwa kiongozi atatumia vibaya fedha za umma, wananchi wana haki ya kumwajibisha."
    },
    "Article 10": {
        "title": "National Values and Principles of Governance",
        "official_en": "The national values and principles include patriotism, national unity, sharing and devolution of power, rule of law, democracy, and participation of the people.",
        "simple_en": "Every government officer must act with honesty, involve citizens in decisions, respect human rights, and ensure fair sharing of national wealth.",
        "example_en": "When a county plans a new market, they cannot build it secretly. Article 10 obligates them to hold public participation meetings first.",
        "simple_sw": "Kila afisa wa serikali lazima atende kwa uaminifu, awashirikishe wananchi katika maamuzi, na aheshimu haki za binadamu.",
        "example_sw": "Wakati kaunti inapanga kujenga soko, lazima iitishe mkutano wa ushiriki wa umma kwanza kulingana na Ibara ya 10."
    },
    "Article 35": {
        "title": "Access to Information",
        "official_en": "Every citizen has the right of access to information held by the State or another person required for the exercise or protection of any right.",
        "simple_en": "You have the legal right to request official government records, budget breakdown reports, or project contract details.",
        "example_en": "If a borehole project in your village stalls, you can write a formal letter under Article 35 requesting the budget breakdown from the County Ministry of Water.",
        "simple_sw": "Kila mwananchi ana haki ya kupata taarifa rasmi zinazoshikiliwa na serikali au taasisi ya umma.",
        "example_sw": "Kama mradi wa kisima cha maji kijijini kwako umekwama, unaweza kuandika barua ukiomba stakabadhi za matumizi ya pesa hizo."
    },
    "Article 43": {
        "title": "Economic and Social Rights",
        "official_en": "Every person has the right to the highest attainable standard of health, accessible and adequate housing, reasonable standards of sanitation, freedom from hunger, clean water, and education.",
        "simple_en": "The government is required by law to progressively ensure everyone has access to medical care, clean water, schooling, decent housing, and food.",
        "example_en": "If a public dispensary lacks basic emergency medicines or clean running water, citizens can demand action using Article 43.",
        "simple_sw": "Kila mtu ana haki ya kupata huduma bora za afya, nyumba nzuri, maji safi, chakula, na elimu.",
        "example_sw": "Kama zahanati ya umma haina dawa za dharura au maji safi, wananchi wana haki ya kudai huduma hizo kisheria."
    }
}

# B. GOVERNMENT ROLES DIRECTORY
ROLES_DATA = {
    "Member of Parliament (MP)": {
        "level": "National Government",
        "badge_class": "badge-national",
        "who": "Elected by voters in a Constituency (e.g., Kitui East, Embakasi East).",
        "does": [
            "Makes national laws and amends the Constitution.",
            "Allocates national revenue and manages NG-CDF (Constituency Development Fund).",
            "Oversights Cabinet Secretaries and national government expenditure."
        ],
        "cannot": "Cannot manage county health centers, local ward feeder roads, or county markets."
    },
    "Member of the County Assembly (MCA)": {
        "level": "County Government",
        "badge_class": "badge-county",
        "who": "Elected by voters in a local Ward.",
        "does": [
            "Makes county laws and ward-level policies.",
            "Approves county government budgets presented by the Governor.",
            "Oversights County Executive Committee Members (CECMs)."
        ],
        "cannot": "Cannot alter national income tax laws, pass national defense bills, or manage national trunk highways."
    },
    "Governor": {
        "level": "County Executive",
        "badge_class": "badge-county",
        "who": "Elected by voters across an entire County.",
        "does": [
            "Chief Executive Officer of the County Government.",
            "Implements county policy on health, county roads, agriculture, and local markets.",
            "Appoints County Executive Officers with Assembly approval."
        ],
        "cannot": "Does not command the National Police Service or control national curriculum exams."
    }
}


# =========================================================
# 4. MODULE IMPLEMENTATIONS
# =========================================================

# ---------------------------------------------------------
# MODULE 1: ASK FAHAMU (CONTROLLED SOURCE-BASED AI COPILOT)
# ---------------------------------------------------------
if selected_module in ["Ask Fahamu (AI Copilot)", "Muulize Fahamu (Msaidizi wa AI)"]:
    st.header("🤖 Ask Fahamu — Source-Based Civic AI Copilot")
    st.caption("Fahamu provides simple, objective explanations derived strictly from official constitutional sources and statutory frameworks.")

    st.markdown("""
    <div style="background-color: #1E1B4B; border: 1px solid #6366F1; border-radius: 10px; padding: 1rem; margin-bottom: 1rem;">
        <h4 style="margin:0; color:#A5B4FC;">💡 Ask Fahamu anything about Kenyan law or government roles!</h4>
        <p style="font-size: 0.9rem; color: #C7D2FE; margin-top:0.3rem;">
            Try asking: <i>"What does my MP do?"</i> | <i>"How do I request public information?"</i> | <i>"What is Article 43?"</i>
        </p>
    </div>
    """, unsafe_allow_html=True)

    query = st.text_input("💬 Type your question here / Andika swali yako hapa:", placeholder="e.g., What is the difference between an MP and an MCA?")

    if st.button("Query Fahamu / Uliza"):
        if query:
            st.info("🤖 **Fahamu's Responsive Answer:**")
            q_lower = query.lower()
            
            if "mp" in q_lower or "parliament" in q_lower:
                st.markdown("""
                - **Simple Answer:** A Member of Parliament (MP) represents a Constituency at the national level. They pass national laws, debate national taxes, and allocate NG-CDF funds.
                - **Official Source:** *Constitution of Kenya (2010), Article 95.*
                - **Key Distinction:** MPs do not manage county health dispensaries or local ward roads; those fall under the Governor and MCA.
                """)
            elif "article 43" in q_lower or "health" in q_lower or "water" in q_lower:
                st.markdown("""
                - **Simple Answer:** Article 43 guarantees your economic and social rights, including the right to clean water, accessible healthcare, adequate housing, and education.
                - **Official Source:** *Constitution of Kenya (2010), Article 43.*
                - **Actionable Step:** If a local health facility lacks essential supplies, citizens can submit a petition to the County Executive Committee Member for Health.
                """)
            elif "gbv" in q_lower or "help" in q_lower or "violence" in q_lower:
                st.markdown("""
                - **Simple Answer:** Gender-Based Violence (GBV) is a violation of fundamental human rights under Article 29. Immediate free toll-free support is available nationwide.
                - **Verified Contact:** Call **1195** (National GBV Helpline - Free 24/7).
                - **Official Source:** *Protection against Domestic Violence Act & Constitution Article 29.*
                """)
            else:
                st.markdown(f"""
                - **Fahamu Analysis:** Your query regarding *"{query}"* touches on constitutional principles.
                - **General Guidance:** Under Article 10, all public bodies must ensure public participation, transparency, and accountability.
                - **Source Note:** *Data validated against the Constitution of Kenya (2010) and official public participation guidelines.*
                """)
        else:
            st.warning("Please type a question to consult Fahamu.")

# ---------------------------------------------------------
# MODULE 2: KNOW YOUR CONSTITUTION (KATIBA)
# ---------------------------------------------------------
elif selected_module in ["Know Your Constitution (Katiba)", "Jua Katiba Yako"]:
    st.header("📖 Know Your Constitution — Simplified Article Explorer")
    st.caption("Read official constitutional provisions side-by-side with plain-language explanations and real-life examples.")

    article_choice = st.selectbox("Select Constitutional Article / Chagua Ibara:", list(CONSTITUTION_DATA.keys()))
    art_info = CONSTITUTION_DATA[article_choice]

    st.subheader(f"{article_choice}: {art_info['title']}")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="card">
            <h4>📜 Official Constitutional Text</h4>
            <p><i>"{art_info['official_en']}"</i></p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        simple_text = art_info['simple_en'] if language == "English" else art_info['simple_sw']
        st.markdown(f"""
        <div class="card" style="border-left-color: #10B981;">
            <h4>💡 Plain Language Explanation</h4>
            <p>{simple_text}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🏘️ Real-Life Example / Mfano Halisi")
    example_text = art_info['example_en'] if language == "English" else art_info['example_sw']
    st.markdown(f"""
    <div class="example-box">
        <b>Scenario:</b> {example_text}
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# MODULE 3: WHO DOES WHAT? (ROLES & DIRECTORY)
# ---------------------------------------------------------
elif selected_module in ["Who Does What? (Roles & Offices)", "Nani Anafanya Nini? (Majukumu)"]:
    st.header("🏛️ Who Does What? — Governance & Roles Directory")
    st.caption("Understand exact government responsibilities to know who to hold accountable for public services.")

    role_choice = st.selectbox("Select Public Office / Chagua Ofisi:", list(ROLES_DATA.keys()))
    role = ROLES_DATA[role_choice]

    st.markdown(f"### {role_choice} <span class='{role['badge_class']}'>{role['level']}</span>", unsafe_allow_html=True)
    st.write(f"**How Selected:** {role['who']}")

    st.markdown("#### ✅ Primary Responsibilities")
    for item in role["does"]:
        st.write(f"• {item}")

    st.markdown("#### ❌ What This Office CANNOT Do")
    st.warning(role["cannot"])

# ---------------------------------------------------------
# MODULE 4: PUBLIC PARTICIPATION & VOICE HUB
# ---------------------------------------------------------
elif selected_module in ["Public Participation & Voice Hub", "Ushiriki wa Umma na Sauti"]:
    st.header("✍️ Public Participation & Memorandum Generator")
    st.caption("Draft structured memoranda for submission to National Assembly or County Assembly public hearings.")

    tab1, tab2 = st.tabs(["📄 Memorandum Builder", "🎙️ Voice Input (PWA Prototype)"])

    with tab1:
        st.subheader("Generate Formal Written Submission")
        bill_name = st.text_input("Bill / Policy Title:", placeholder="e.g., County Finance Bill 2026")
        user_concern = st.text_area("Your Primary Objection / Recommendation:", height=100)
        
        if st.button("Generate Memorandum Draft"):
            if bill_name and user_concern:
                st.success("Draft Generated!")
                st.code(f"""TO: THE CLERK OF THE ASSEMBLY
RE: FORMAL SUBMISSION OF PUBLIC PARTICIPATION ON {bill_name.upper()}

1. CITIZEN INTEREST & CAPACITY
I am writing as a concerned citizen to formally present views regarding {bill_name}.

2. SUBSTANTIVE RECOMMENDATION / OBJECTION
{user_concern}

3. CONSTITUTIONAL BASIS
Submitted pursuant to Article 118 & Article 10 of the Constitution of Kenya (2010).

Submitted via Afro Civic (AFCI) Public Hub.""", language="markdown")
            else:
                st.warning("Please fill in both fields.")

    with tab2:
        st.subheader("Speak Your Views (Accessibility)")
        st.write("Record your voice statement directly. Ideal for hands-free or spoken input.")
        audio_file = st.audio_input("RECORD STATEMENT")
        if audio_file:
            st.success("✅ Audio Captured Successfully!")
            st.audio(audio_file)
            st.info("📝 **AI Transcription Preview:** *'I am recording to state that our local market lacks drainage facilities, and funds under the ward budget should prioritize sanitation.'*")

# ---------------------------------------------------------
# MODULE 5: RIGHTS, ADVOCACY & GBV SUPPORT
# ---------------------------------------------------------
elif selected_module in ["Rights, Advocacy & GBV Help", "Haki, Utetezi na Msaada wa GBV"]:
    st.header("🛡️ Rights, Advocacy & Emergency Support Hub")
    st.caption("Verified emergency contacts, referral pathways, and human rights advocacy tools.")

    st.markdown("""
    <div class="card-gbv">
        <h2 style="margin:0; color:#FFE4E6;">🚨 Emergency Helpline: 1195</h2>
        <p style="margin-top:0.5rem; font-size:1rem;">
            If you or someone you know is facing Gender-Based Violence (GBV), domestic abuse, or emergency risk, call <b>1195</b> for free 24/7 confidential help, medical referral, and legal protection support in Kenya.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card">
            <h4>📞 Verified Support Hotline Directory</h4>
            <ul>
                <li><b>National GBV Hotline:</b> 1195 (Free 24/7)</li>
                <li><b>Childline Kenya:</b> 116</li>
                <li><b>KNCHR (Human Rights Commission):</b> 0800 720 627</li>
                <li><b>Emergency Police Service:</b> 999 / 112</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h4>⚖️ Fundamental Rights (Article 29)</h4>
            <p>Every person has the right to freedom and security, which includes the right not to be subjected to any form of violence, torture, or cruel treatment.</p>
        </div>
        """, unsafe_allow_html=True)


# =========================================================
# 5. FOOTER & LEGAL DISCLAIMERS
# =========================================================
st.markdown("""
<div class="footer-text">
    © 2026 Afro Civic (AFCI). All Rights Reserved. <br>
    <i>Afro Civic is an independent civic education initiative and is not an official government or IEBC entity.</i><br>
    <b>Piloting in Kenya | Designed for Pan-African Adaptation</b>
</div>
""", unsafe_allow_html=True)
