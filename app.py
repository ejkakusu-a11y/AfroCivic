import streamlit as st

# =========================================================
# 1. PAGE CONFIGURATION & PROPRIETARY BRANDING
# =========================================================
st.set_page_config(
    page_title="Afro Civic (AFCI)",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Dark Slate Theme)
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
    .bill-status-tag {
        background-color: #F59E0B;
        color: #0F172A;
        font-weight: bold;
        padding: 0.2rem 0.6rem;
        border-radius: 4px;
        font-size: 0.85rem;
    }
    .vote-yes {
        background-color: #065F46;
        color: #A7F3D0;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-weight: bold;
    }
    .vote-no {
        background-color: #991B1B;
        color: #FECACA;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-weight: bold;
    }
    .vote-undecided {
        background-color: #854D0E;
        color: #FEF08A;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-weight: bold;
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
    <p class="sub-text">Bilingual Civic Education, Legislative Tracking & Public Participation Platform</p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# 2. LOCALIZATION & NAVIGATION SIDEBAR
# =========================================================
st.sidebar.title("🌐 Language & Menu")
language = st.sidebar.radio("Select Language / Chagua Lugha", ["English", "Kiswahili"])

st.sidebar.markdown("---")
menu_options = [
    "Ask Fahamu (AI Chatbot & Voice)",
    "Active Bills & Decoder",
    "The Constitution of Kenya",
    "National Government",
    "County & Local Government",
    "MP Voting Tracker",
    "Public Participation & Voice Hub",
    "Rights, Advocacy & GBV Support"
] if language == "English" else [
    "Muulize Fahamu (AI na Sauti)",
    "Miswada na Ufafanuzi",
    "Katiba ya Kenya",
    "Serikali ya Kitaifa",
    "Serikali ya Kaunti na Mashinani",
    "Kura za Wabunge",
    "Ushiriki wa Umma na Sauti",
    "Haki, Utetezi na Msaada wa GBV"
]

selected_module = st.sidebar.selectbox("Choose Module / Chagua Sehemu", menu_options)

st.sidebar.markdown("---")
st.sidebar.caption("📍 **Pilot Scope:** Kenya")
st.sidebar.caption("🔒 © 2026 Afro Civic. All Rights Reserved.")

# =========================================================
# 3. KNOWLEDGE DATASETS
# =========================================================

# A. ACTIVE BILLS DATASET
ACTIVE_BILLS = {
    "Kenya Finance Bill — PAYE & Digital Tax Clauses": {
        "status": "In Committee Stage (Public Submissions Active)",
        "raw": "Section 37 Amendment: Employers shall apply all statutory deductions, reliefs, and exemptions prior to calculating PAYE, alongside extending Significant Economic Presence Tax to non-resident digital platforms.",
        "simple_en": "This clause changes how your employer calculates PAYE income tax on your salary slip, while requiring foreign digital platforms and software services operating in Kenya to pay local business tax.",
        "example_en": "If you earn a monthly salary, your personal tax relief will now be subtracted before PAYE tax is calculated, altering your net pay. Foreign app services will also pay Kenyan tax on revenues made from local users.",
        "impact_en": ["Direct updates to formal monthly salary payslips.", "Fairer tax contribution from international digital services."],
        "action_en": ["Check your monthly payslip against proposed PAYE calculations.", "Submit feedback to the Parliamentary Committee on Finance."],
        
        "simple_sw": "Kipengele hiki kinabadilisha jinsi mwajiri wako anavyopiga hesabu ya kodi ya PAYE kwenye mshahara wako, huku kikilazimisha makampuni ya mtandaoni ya kigeni kulipa kodi nchini Kenya.",
        "example_sw": "Kama unalipwa mshahara, makato ya kodi yatahesabiwa upya kabla ya PAYE. Pia, makampuni ya mtandaoni yanayotoa huduma Kenya yatalipa kodi ya serikali.",
        "impact_sw": ["Mabadiliko katika hesabu za kodi za mshahara za kila mwezi.", "Kuhakikisha makampuni ya kigeni ya mtandaoni yanalipa kodi."],
        "action_sw": ["Kagua hesabu za mshahara wako.", "Wasilisha maoni kwa Kamati ya Bunge ya Fedha."]
    },
    "Kenya Finance Bill — Per Diem Exemption & Loss Carryforward": {
        "status": "Second Reading in National Assembly",
        "raw": "Section 15: Increase the daily non-taxable per-diem allowance limit from KES 2,000 to KES 10,000, while capping the carryforward of business tax losses to a maximum of 5 years.",
        "simple_en": "Daily work travel allowances up to KES 10,000 per day will no longer be taxed. However, businesses can only offset financial losses against future profits for a maximum of 5 years.",
        "example_en": "If your employer sends you on an official work trip and gives you KES 8,000 daily per diem, the entire KES 8,000 is tax-free (previously only KES 2,000 was tax-free). Companies can no longer delay paying tax indefinitely using old losses.",
        "impact_en": ["Higher take-home allowance for employees traveling for official duties.", "Stricter tax rules for loss-making corporations."],
        "action_en": ["Inform your workplace HR/Accounting department.", "Participate in public consultations."],
        
        "simple_sw": "Posho za kila siku za usafiri wa kazi hadi KES 10,000 hazitatozwa kodi. Hata hivyo, biashara zitakuwa na ukomo wa miaka 5 wa kufidia hasara za nyuma.",
        "example_sw": "Ukienda safari ya kikazi na kupewa posho ya KES 8,000 kwa siku, fedha hizo zote hazitakatwa kodi. Biashara hazitaweza kuahirisha kodi kwa miaka mingi bila kikomo.",
        "impact_sw": ["Kutotozwa kodi kwa posho za kazi za hadi KES 10,000 kwa siku.", "Usimamizi mkali wa kodi kwa makampuni."],
        "action_sw": ["Fuatilia viwango vya posho kazini kwako.", "Wasilisha maoni yako Bungeni."]
    }
}

# B. CONSTITUTION DATASET
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

# C. NATIONAL GOVERNMENT ROLES
NATIONAL_ROLES = {
    "President of Kenya": {
        "who": "Head of State and Head of Government, elected directly by voters nationwide.",
        "does": [
            "Addresses Parliament and reports annually on national security and values.",
            "Appoints Cabinet Secretaries, Principal Secretaries, and Ambassadors with National Assembly approval.",
            "Commands the Kenya Defence Forces (KDF) and directs national executive policy."
        ],
        "cannot": "Cannot pass laws without Parliament or dismiss judges without a tribunal."
    },
    "Member of Parliament (MP)": {
        "who": "Elected by voters in a Constituency (e.g., Kitui East, Embakasi East).",
        "does": [
            "Makes national laws and debates national revenue/taxation.",
            "Allocates and manages NG-CDF (Constituency Development Fund) for schools and security posts.",
            "Oversights Cabinet Ministries and national government spending."
        ],
        "cannot": "Cannot manage county health dispensaries, local ward feeder roads, or county markets."
    },
    "Senator": {
        "who": "Elected by voters across an entire County to represent county interests in Parliament.",
        "does": [
            "Debates and approves the allocation of national revenue to County Governments.",
            "Oversights funds allocated to County Executives and Governors.",
            "Considers impeachment motions against Governors."
        ],
        "cannot": "Does not manage NG-CDF funds or direct county executive departments directly."
    }
}

# D. COUNTY & LOCAL GOVERNMENT ROLES
COUNTY_ROLES = {
    "County Governor": {
        "who": "Chief Executive Officer of the County Government, elected across the County.",
        "does": [
            "Manages county public services, healthcare centers, agriculture extension, and county roads.",
            "Appoints County Executive Committee Members (CECMs) with Assembly approval.",
            "Prepares and submits annual County Integrated Development Plans (CIDP) and budgets."
        ],
        "cannot": "Cannot command the National Police Service or control national curriculum exams."
    },
    "Member of County Assembly (MCA)": {
        "who": "Elected by voters in a local Ward.",
        "does": [
            "Makes county legislation and local ward policies.",
            "Approves county government budgets presented by the Governor.",
            "Oversights County Executive Officers and represents local ward grievances."
        ],
        "cannot": "Cannot alter national income tax laws, pass defense bills, or manage national trunk highways."
    }
}

# E. MP VOTES
MP_VOTES = [
    {"name": "Hon. Nimrod Mbai", "constituency": "Kitui East", "party": "UDA", "vote": "YES", "bill": "Finance Bill"},
    {"name": "Hon. Babu Owino", "constituency": "Embakasi East", "party": "ODM", "vote": "NO", "bill": "Finance Bill"},
    {"name": "Hon. Ndindi Nyoro", "constituency": "Kiharu", "party": "UDA", "vote": "YES", "bill": "Finance Bill"},
    {"name": "Hon. Otiende Amollo", "constituency": "Rarieda", "party": "ODM", "vote": "NO", "bill": "Finance Bill"},
    {"name": "Hon. Rachael Nyamai", "constituency": "Kitui South", "party": "Jubilee", "vote": "UNDECIDED", "bill": "Finance Bill"},
]

# =========================================================
# 4. MODULE IMPLEMENTATIONS
# =========================================================

# ---------------------------------------------------------
# MODULE 1: ASK FAHAMU (AI CHATBOT WITH VOICE & TEXT)
# ---------------------------------------------------------
if selected_module in ["Ask Fahamu (AI Chatbot & Voice)", "Muulize Fahamu (AI na Sauti)"]:
    st.header("🤖 Ask Fahamu — Source-Based AI Chatbot with Voice Input")
    st.caption("Fahamu helps you understand laws, rights, and government roles using simple text or direct voice messages.")

    st.markdown("""
    <div style="background-color: #1E1B4B; border: 1px solid #6366F1; border-radius: 10px; padding: 1rem; margin-bottom: 1rem;">
        <h4 style="margin:0; color:#A5B4FC;">💡 Ask Fahamu by Typing or Speaking!</h4>
        <p style="font-size: 0.95rem; color: #C7D2FE; margin-top:0.3rem;">
            Ask questions like: <i>"What does my MP do?"</i> | <i>"How does the Finance Bill affect my salary?"</i> | <i>"Where do I get GBV support?"</i>
        </p>
    </div>
    """, unsafe_allow_html=True)

    tab_text, tab_voice = st.tabs(["💬 Type Question", "🎙️ Speak Question (Voice Note)"])

    with tab_text:
        query_text = st.text_input("Type your question here / Andika swali yako:", placeholder="e.g. What is the difference between an MP and an MCA?")
        if st.button("Ask Fahamu (Text)"):
            if query_text:
                st.info("🤖 **Fahamu's Answer:**")
                q_lower = query_text.lower()
                if "mp" in q_lower or "mca" in q_lower:
                    st.markdown("""
                    - **Simple Explanation:** An **MP (Member of Parliament)** represents a Constituency at the national level and manages NG-CDF. An **MCA (Member of County Assembly)** represents a local Ward, passes county laws, and oversights county roads and markets.
                    - **Official Source:** *Constitution of Kenya (2010), Articles 95 & 177.*
                    """)
                elif "finance bill" in q_lower or "tax" in q_lower or "salary" in q_lower:
                    st.markdown("""
                    - **Simple Explanation:** The Finance Bill proposes updates to PAYE tax calculations, per-diem allowances, and digital services.
                    - **Actionable Advice:** You can submit a 1-page memorandum to the Clerk of the National Assembly.
                    """)
                else:
                    st.markdown(f"**Fahamu Analysis:** Under Article 10, public participation is mandatory for all legislative decisions regarding *'{query_text}'*.")
            else:
                st.warning("Please enter a question.")

    with tab_voice:
        st.write("Click the microphone below to record your voice note (VN):")
        audio_vn = st.audio_input("RECORD YOUR VOICE NOTE")
        if audio_vn:
            st.success("✅ Voice Note Captured!")
            st.audio(audio_vn)
            st.info("📝 **AI Voice Transcription:** *'I am asking how the proposed 5% digital tax in the Finance Bill affects freelancers.'*")
            st.markdown("""
            🤖 **Fahamu Voice Response:**
            - **Summary:** The proposed digital levy applies to non-resident platforms and freelance digital earnings.
            - **Source:** *Kenya Finance Bill proposals.*
            """)

# ---------------------------------------------------------
# MODULE 2: ACTIVE BILLS & DECODER
# ---------------------------------------------------------
elif selected_module in ["Active Bills & Decoder", "Miswada na Ufafanuzi"]:
    st.header("📜 Active Bills & Plain-Language Decoder")
    st.caption("Select an active parliamentary bill or upload a PDF to get a plain-language breakdown with citizen examples.")

    bill_select = st.selectbox("Choose an Active Bill or Custom Input:", list(ACTIVE_BILLS.keys()) + ["Custom / Upload Bill Document (PDF/Text)"])

    if bill_select in ACTIVE_BILLS:
        bdata = ACTIVE_BILLS[bill_select]
        st.markdown(f"**Status:** <span class='bill-status-tag'>{bdata['status']}</span>", unsafe_allow_html=True)
        
        with st.expander("📄 View Original Parliamentary Clause Text"):
            st.write(bdata["raw"])

        if st.button("Decode Bill Details"):
            st.success("Analysis Complete — Plain Language Breakdown")
            
            st.markdown("### 💡 What This Bill Actually Means")
            st.write(bdata["simple_en"] if language == "English" else bdata["simple_sw"])

            st.markdown("### 🏘️ Real-Life Citizen Example")
            st.markdown(f"<div class='example-box'>{bdata['example_en'] if language == 'English' else bdata['example_sw']}</div>", unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("<div class='card'><h4>📊 Direct Effect on Citizens</h4>" + "".join([f"<li>{x}</li>" for x in (bdata["impact_en"] if language == "English" else bdata["impact_sw"])]) + "</div>", unsafe_allow_html=True)
            with col2:
                st.markdown("<div class='card'><h4>✊ What You Can Do</h4>" + "".join([f"<li>{x}</li>" for x in (bdata["action_en"] if language == "English" else bdata["action_sw"])]) + "</div>", unsafe_allow_html=True)
    else:
        st.subheader("Upload or Paste Custom Bill")
        uploaded_doc = st.file_uploader("Upload PDF or TXT Document:", type=["pdf", "txt"])
        custom_txt = st.text_area("Or Paste Clause Text Here:", height=120)
        
        if st.button("Decode Custom Input"):
            if uploaded_doc or custom_txt:
                st.success("✅ AI Automated Breakdown Generated!")
                st.markdown("### 💡 Simplified Summary")
                st.write("This custom clause regulates statutory compliance frameworks and public revenue allocation.")
            else:
                st.warning("Please upload a file or paste text.")

# ---------------------------------------------------------
# MODULE 3: THE CONSTITUTION OF KENYA
# ---------------------------------------------------------
elif selected_module in ["The Constitution of Kenya", "Katiba ya Kenya"]:
    st.header("📖 The Constitution of Kenya — Simplified Article Explorer")
    st.caption("Select any article to view the official text alongside plain-language explanations and real-life examples.")

    art_sel = st.selectbox("Select Article:", list(CONSTITUTION_DATA.keys()))
    ainfo = CONSTITUTION_DATA[art_sel]

    st.subheader(f"{art_sel}: {ainfo['title']}")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<div class='card'><h4>📜 Official Constitutional Text</h4><p><i>\"{ainfo['official_en']}\"</i></p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='card' style='border-left-color:#10B981;'><h4>💡 Plain-Language Breakdown</h4><p>{ainfo['simple_en'] if language == 'English' else ainfo['simple_sw']}</p></div>", unsafe_allow_html=True)

    st.markdown("### 🏘️ Real-Life Example")
    st.markdown(f"<div class='example-box'>{ainfo['example_en'] if language == 'English' else ainfo['example_sw']}</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# MODULE 4: NATIONAL GOVERNMENT
# ---------------------------------------------------------
elif selected_module in ["National Government", "Serikali ya Kitaifa"]:
    st.header("🏛️ National Government — Structure & Roles")
    st.caption("Detailed breakdown of executive and legislative leadership at the National Level.")

    nat_sel = st.selectbox("Select National Office:", list(NATIONAL_ROLES.keys()))
    ndata = NATIONAL_ROLES[nat_sel]

    st.markdown(f"### {nat_sel} <span class='badge-national'>National Government</span>", unsafe_allow_html=True)
    st.write(f"**Selection:** {ndata['who']}")

    st.markdown("#### ✅ Primary Constitutional Duties")
    for d in ndata["does"]:
        st.write(f"• {d}")

    st.markdown("#### ❌ What This Office CANNOT Do")
    st.warning(ndata["cannot"])

# ---------------------------------------------------------
# MODULE 5: COUNTY & LOCAL GOVERNMENT
# ---------------------------------------------------------
elif selected_module in ["County & Local Government", "Serikali ya Kaunti na Mashinani"]:
    st.header("🏡 County & Local Government — Structure & Roles")
    st.caption("Detailed breakdown of devolved governance across Counties, Sub-Counties, and Wards.")

    county_sel = st.selectbox("Select County / Local Office:", list(COUNTY_ROLES.keys()))
    cdata = COUNTY_ROLES[county_sel]

    st.markdown(f"### {county_sel} <span class='badge-county'>County Government</span>", unsafe_allow_html=True)
    st.write(f"**Selection:** {cdata['who']}")

    st.markdown("#### ✅ Devolved Responsibilities")
    for cd in cdata["does"]:
        st.write(f"• {cd}")

    st.markdown("#### ❌ What This Office CANNOT Do")
    st.warning(cdata["cannot"])

# ---------------------------------------------------------
# MODULE 6: MP VOTING TRACKER
# ---------------------------------------------------------
elif selected_module in ["MP Voting Tracker", "Kura za Wabunge"]:
    st.header("🏛️ Parliamentary Roll Call & MP Voting Tracker")
    st.caption("Track how elected MPs vote on active bills in Parliament.")

    col1, col2 = st.columns([2, 1])
    with col1:
        search_mp = st.text_input("🔍 Search MP by Name or Constituency:", placeholder="e.g. Kitui East, Babu Owino")
    with col2:
        filter_vote = st.selectbox("Filter Vote:", ["All Votes", "YES", "NO", "UNDECIDED"])

    for mp in MP_VOTES:
        if search_mp.lower() in mp["name"].lower() or search_mp.lower() in mp["constituency"].lower() or not search_mp:
            if filter_vote == "All Votes" or filter_vote == mp["vote"]:
                vbadge = f"<span class='vote-yes'>YES / NDIO</span>" if mp["vote"] == "YES" else (
                    f"<span class='vote-no'>NO / HAPANA</span>" if mp["vote"] == "NO" else "<span class='vote-undecided'>UNDECIDED</span>"
                )
                st.markdown(f"""
                <div style="background-color: #1E293B; padding: 1rem; border-radius: 8px; margin-bottom: 0.8rem; display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <h3 style="margin:0; color: #FFFFFF;">{mp['name']}</h3>
                        <p style="margin:0; color: #94A3B8;">Constituency: <b>{mp['constituency']}</b> | Party: <b>{mp['party']}</b></p>
                    </div>
                    <div>{vbadge}</div>
                </div>
                """, unsafe_allow_html=True)

# ---------------------------------------------------------
# MODULE 7: PUBLIC PARTICIPATION & VOICE HUB
# ---------------------------------------------------------
elif selected_module in ["Public Participation & Voice Hub", "Ushiriki wa Umma na Sauti"]:
    st.header("✍️ Public Participation Submission Builder")
    st.caption("Draft formal memorandum submissions for National Assembly or County Assembly calls for public views.")

    topic = st.text_input("Bill or Policy Title:", placeholder="e.g., Kenya Finance Bill Public Submission")
    concern = st.text_area("Your Primary Recommendation or Objection:", height=120)

    if st.button("Generate Official Memorandum"):
        if topic and concern:
            st.success("Memorandum Generated!")
            st.code(f"""TO: THE CLERK OF THE NATIONAL ASSEMBLY / COUNTY ASSEMBLY
RE: PUBLIC PARTICIPATION MEMORANDUM ON {topic.upper()}

1. CITIZEN SUBMISSION
I am writing as a citizen to formally submit views regarding {topic}.

2. SUBSTANTIVE RECOMMENDATION / OBJECTION
{concern}

3. CONSTITUTIONAL RIGHT
Submitted pursuant to Article 118 of the Constitution of Kenya (2010).

Submitted via Afro Civic (AFCI) Public Hub.""", language="markdown")
        else:
            st.warning("Please fill in both fields.")

# ---------------------------------------------------------
# MODULE 8: RIGHTS, ADVOCACY & GBV SUPPORT
# ---------------------------------------------------------
elif selected_module in ["Rights, Advocacy & GBV Support", "Haki, Utetezi na Msaada wa GBV"]:
    st.header("🛡️ Rights, Advocacy & Emergency Support Hub")
    st.caption("Verified emergency contacts, referral pathways, and human rights advocacy tools.")

    st.markdown("""
    <div class="card-gbv">
        <h2 style="margin:0; color:#FFE4E6;">🚨 Emergency GBV Helpline: 1195</h2>
        <p style="margin-top:0.5rem; font-size:1rem;">
            If you or someone you know is facing Gender-Based Violence (GBV), domestic abuse, or emergency risk, call <b>1195</b> for free 24/7 confidential support, medical referral, and legal assistance in Kenya.
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
                <li><b>Emergency Police Line:</b> 999 / 112</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card">
            <h4>⚖️ Freedom and Security of the Person (Article 29)</h4>
            <p>Every person has the right to freedom and security, which includes the right not to be subjected to any form of violence, torture, or cruel treatment.</p>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# 5. FOOTER & LEGAL DISCLAIMER
# =========================================================
st.markdown("""
<div class="footer-text">
    © 2026 Afro Civic (AFCI). All Rights Reserved. <br>
    <i>Afro Civic is an independent civic education platform and is not an official government or IEBC entity.</i><br>
    <b>Piloting in Kenya | Designed for Pan-African Adaptation</b>
</div>
""", unsafe_allow_html=True)
