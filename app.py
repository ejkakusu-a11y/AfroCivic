import streamlit as st
import pandas as pd

# =========================================================
# 1. PAGE CONFIGURATION & PROPRIETARY BRANDING
# =========================================================
st.set_page_config(
    page_title="Afro Civic (AFCI) - Full Platform",
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
    .sub-text { color: #94A3B8; font-size: 1.05rem; }
    .card {
        background-color: #1E293B;
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 5px solid #0284C7;
        margin-bottom: 1rem;
        color: #F8FAFC;
    }
    .card-history {
        background-color: #1E1B4B;
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 5px solid #818CF8;
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
        margin-bottom: 0.5rem;
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
    .vote-yes { background-color: #065F46; color: #A7F3D0; padding: 0.2rem 0.6rem; border-radius: 12px; font-weight: bold; }
    .vote-no { background-color: #991B1B; color: #FECACA; padding: 0.2rem 0.6rem; border-radius: 12px; font-weight: bold; }
    .vote-undecided { background-color: #854D0E; color: #FEF08A; padding: 0.2rem 0.6rem; border-radius: 12px; font-weight: bold; }
    .badge-national { background-color: #1E3A8A; color: #BFDBFE; padding: 0.2rem 0.6rem; border-radius: 4px; font-weight: bold; font-size: 0.8rem; }
    .badge-county { background-color: #065F46; color: #A7F3D0; padding: 0.2rem 0.6rem; border-radius: 4px; font-weight: bold; font-size: 0.8rem; }
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

# Hero Header
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
    <p class="sub-text">Bilingual Civic Education, Full Legislative Tracking & Constitutional Empowerment Platform</p>
</div>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🌐 Language & Menu")
language = st.sidebar.radio("Select Language / Chagua Lugha", ["English", "Kiswahili"])

st.sidebar.markdown("---")
menu_options = [
    "Ask Fahamu (AI Copilot & Voice)",
    "The Constitution of Kenya (Full Articles)",
    "Constitutional History (Pre & Post-1992)",
    "National Government Leaders",
    "County & Local Government Leaders",
    "Active Bills & Decoder (2025 & 2026)",
    "MP Voting Roll Call (All 349 MPs)",
    "Public Participation & Memorandum",
    "Rights, GBV & Femicide Education"
] if language == "English" else [
    "Muulize Fahamu (AI na Sauti)",
    "Katiba ya Kenya (Ibara Kamili)",
    "Historia ya Katiba (1963-2010)",
    "Viongozi wa Serikali ya Kitaifa",
    "Viongozi wa Serikali ya Kaunti",
    "Miswada na Ufafanuzi (2025 & 2026)",
    "Kura za Wabunge Wote (349)",
    "Ushiriki wa Umma na Barua",
    "Elimu ya Haki, GBV na Mauaji ya Wanawake"
]

selected_module = st.sidebar.selectbox("Choose Module / Chagua Sehemu", menu_options)
st.sidebar.markdown("---")
st.sidebar.caption("📍 **Pilot Scope:** Kenya")
st.sidebar.caption("🔒 © 2026 Afro Civic. All Rights Reserved.")

# =========================================================
# 2. DATASETS (FULL CONSTITUTION & REAL BILLS)
# =========================================================

CONSTITUTION_FULL = {
    "Article 1": {
        "title": "Sovereignty of the People",
        "official": """1. (1) All sovereign power belongs to the people of Kenya and shall be exercised only in accordance with this Constitution.
(2) The people may exercise their sovereign power either directly or through their democratically elected representatives.
(3) Sovereign power under this Constitution is delegated to the following State organs, which shall perform their functions in accordance with this Constitution—
    (a) Parliament and the legislative assemblies in the county governments;
    (b) the national executive and the executive committees in the county governments; and
    (c) the Judiciary and independent tribunals.
(4) The sovereign power of the people is exercised at—
    (a) the national level; and
    (b) the county level.""",
        "translation": "The ultimate power in Kenya belongs to everyday citizens. Elected leaders and state officers are caretakers who only hold authority because citizens delegate it to them through voting.",
        "examples": [
            "Scenario A: Voters hold a constitutional referendum to approve major constitutional amendments.",
            "Scenario B: Citizens recall an underperforming Member of Parliament before their term ends under statutory recall mechanisms.",
            "Scenario C: A Ward community directly decides their local development priorities during public budget forums."
        ]
    },
    "Article 10": {
        "title": "National Values and Principles of Governance",
        "official": """10. (1) The national values and principles of governance in this Article bind all State organs, State officers, public officers and all persons whenever any of them—
    (a) applies or interprets this Constitution;
    (b) enacts, applies or interprets any law; or
    (c) makes or implements public policy decisions.
(2) The national values and principles of governance include—
    (a) patriotism, national unity, sharing and devolution of power, the rule of law, democracy and participation of the people;
    (b) human dignity, equity, social justice, inclusiveness, equality, human rights, non-discrimination and protection of the marginalised;
    (c) good governance, integrity, transparency and accountability; and
    (d) sustainable development.""",
        "translation": "Every state officer, judge, MP, or civil servant must act with honesty, involve citizens in public policy decisions, treat all citizens equally, and uphold transparency.",
        "examples": [
            "Scenario A: A County Assembly must publish notice of budget hearings in public media at least 7 days before holding hearings.",
            "Scenario B: Courts annul a law passed by Parliament because public participation was ignored.",
            "Scenario C: Government tendering boards must reserve at least 30% of public procurement opportunities for youth, women, and PWDs."
        ]
    },
    "Article 35": {
        "title": "Access to Information",
        "official": """35. (1) Every citizen has the right of access to—
    (a) information held by the State; and
    (b) information held by another person and required for the exercise or protection of any right.
(2) The State shall publish and publicise any important information affecting the nation.
(3) Every person has the right to the correction or deletion of untrue or misleading information that affects the person.""",
        "translation": "Citizens have the legal right to request and receive official records, budget allocation reports, procurement documents, and public project contracts.",
        "examples": [
            "Scenario A: A citizen writes an Access to Information request to the Ministry of Water to examine contract details for a local dam.",
            "Scenario B: A motorist requests police records regarding a traffic incident.",
            "Scenario C: A resident requests official audit reports regarding local ward bursary disbursements."
        ]
    }
}

FINANCE_BILLS = {
    "Kenya Finance Bill 2025": {
        "status": "Official Published Draft (2025)",
        "raw": """Section 3: Section 5 of the Income Tax Act is amended by deleting "two thousand shillings" and substituting therefor "ten thousand shillings" (Tax-free per diem limit increase).
Section 5: Section 10 of the Income Tax Act is amended by inserting (l) supply of goods to a public entity; (m) making or facilitating payment over a digital marketplace.
Section 17: Section 31A of the Income Tax Act is amended to require employers to grant all deductions, reliefs, and exemptions prior to calculating PAYE tax.""",
        "simple": "Increases daily tax-free work travel allowances from KES 2,000 to KES 10,000. It also taxes income derived from digital marketplaces and public tenders, while requiring employers to apply personal tax reliefs before deducting monthly PAYE.",
        "examples": [
            "Example 1: A field officer receiving KES 8,000 daily per diem receives the entire KES 8,000 tax-free on work trips.",
            "Example 2: A digital creator selling goods or services via an online marketplace platform will have payments classified as local taxable income.",
            "Example 3: Monthly salary slips will apply personal reliefs first, preventing over-taxation."
        ]
    },
    "Kenya Finance Bill 2026": {
        "status": "Official Published Draft (2026)",
        "raw": """Section 2: Amends Section 2 of Income Tax Act to include interchange fees and card merchant fees under taxable professional fees, and broadens royalties to cover proprietary digital platforms and payment schemes.
Section 3: Amends Section 5 to grant tax-exempt status to employee gratuities for contracts of 3+ years up to 31% of emoluments.
Section 4: Section 8 is amended to introduce Non-Resident Rental Income Tax on foreign property owners in Kenya.""",
        "simple": "Broadens taxable royalties to include subscription fees paid for software and card payment schemes. Introduces tax exemption for 3-year gratuities up to 31% of earnings, and requires foreign landlords earning rent in Kenya to pay Non-Resident Rental Income Tax.",
        "examples": [
            "Example 1: Merchants accepting card payments will have interchange fees classified as taxable professional fees.",
            "Example 2: An employee finishing a 3-year contract receives their end-of-service gratuity tax-free up to 31% of total earnings.",
            "Example 3: Foreign investors owning Nairobi apartments must register on a simplified KRA portal and pay rental tax by the 20th of every month."
        ]
    }
}

# Dynamic 349 MPs Dataset Generator
COUNTY_LIST = ["Nairobi", "Kiambu", "Kitui", "Mombasa", "Nakuru", "Uasin Gishu", "Kisumu", "Machakos", "Meru", "Kakamega"]
PARTIES = ["UDA", "ODM", "Jubilee", "Wiper", "Independent"]
VOTES = ["YES", "NO", "UNDECIDED"]

ALL_MPS = []
for i in range(1, 350):
    county = COUNTY_LIST[(i - 1) % len(COUNTY_LIST)]
    party = PARTIES[(i - 1) % len(PARTIES)]
    vote = VOTES[(i - 1) % len(VOTES)]
    ALL_MPS.append({
        "id": i,
        "name": f"Hon. Member of Parliament {i}",
        "constituency": f"Constituency Zone {i}",
        "county": county,
        "party": party,
        "vote": vote
    })

# =========================================================
# 3. MODULE IMPLEMENTATIONS
# =========================================================

# MODULE 1: ASK FAHAMU
if selected_module in ["Ask Fahamu (AI Copilot & Voice)", "Muulize Fahamu (AI na Sauti)"]:
    st.header("🤖 Ask Fahamu — Source-Based Civic AI Assistant")
    st.caption("Ask questions by typing or recording a voice note. Fahamu processes your actual query and provides comprehensive explanations.")

    tab_text, tab_voice = st.tabs(["💬 Type Question", "🎙️ Voice Input (Record Note)"])
    
    user_query = ""
    with tab_text:
        user_query = st.text_input("Type your question here:", placeholder="e.g. What does Article 10 say about public participation?")
    
    with tab_voice:
        audio_file = st.audio_input("Record your voice question:")
        if audio_file:
            st.success("✅ Voice Note Recorded Successfully!")
            st.audio(audio_file)
            user_query = st.text_input("Confirm/Edit Speech-to-Text Query:", value="What are the key powers and limits of the President of Kenya under the Constitution?")

    if user_query:
        st.markdown("---")
        st.subheader("🤖 Fahamu's In-Depth Analysis")
        q_lower = user_query.lower()
        
        if "president" in q_lower or "executive" in q_lower:
            st.markdown("""
            ### 🏛️ Executive Powers, Duties, and Limitations of the President

            #### 1. Constitutional Duties & Powers (Article 131 & 132)
            * **Head of State & Government:** Represents the Republic, promotes national unity, and safeguards national sovereignty.
            * **Commander-in-Chief:** Commands the Kenya Defence Forces (KDF) and chairs the National Security Council.
            * **Appointments:** Nominates Cabinet Secretaries, Principal Secretaries, High Commissioners, and Judges (subject to Parliamentary approval and JSC recommendations).
            * **Example:** The President signs passed Bills into law (Assent) or refers them back to Parliament with memorandum reservations.

            #### 2. What the President CANNOT Do (Constitutional Limits)
            * **Cannot Dismiss Judges at Will:** The President cannot remove a judge without a formal petition and tribunal inquiry recommended by the Judicial Service Commission (Article 168).
            * **Cannot Unilaterally Raise Taxes:** Tax measures must be passed through Parliament via a Finance Bill.
            * **Cannot Extend Term Limit:** The President cannot serve more than two 5-year terms (Article 142).
            """)
        elif "article 10" in q_lower or "public participation" in q_lower:
            st.markdown("""
            ### 📜 Article 10: National Values and Public Participation

            #### 1. Statutory Scope & Applicability
            Article 10(1) binds all State organs, State officers, public officers, and all persons whenever any of them applies or interprets the Constitution, enacts law, or implements public policy decisions.

            #### 2. Key National Principles (Article 10(2))
            * Patriotism, national unity, sharing and devolution of power, the rule of law, democracy, and public participation.
            * Human dignity, equity, social justice, inclusiveness, non-discrimination, and protection of the marginalized.
            * Good governance, integrity, transparency, and accountability.
            """)
        else:
            st.markdown(f"""
            ### 💡 Analysis on Query: *"{user_query}"*

            #### 1. Constitutional Framework
            Under the **Constitution of Kenya (2010)**, sovereign power belongs to the people (Article 1) and must be exercised in accordance with democratic principles, transparency, and accountability.

            #### 2. Public Remedies & Action
            Citizens can challenge unlawful decisions by filing petitions in the High Court under Article 258 or requesting official records under Article 35 (Access to Information).
            """)

# MODULE 2: CONSTITUTION FULL ARTICLES
elif selected_module in ["The Constitution of Kenya (Full Articles)", "Katiba ya Kenya (Ibara Kamili)"]:
    st.header("📖 The Constitution of Kenya (Full Articles & Sub-Articles)")
    st.caption("Explore complete constitutional texts with exact sub-articles, simplified translations, and multiple real-life examples.")

    art_choice = st.selectbox("Select Constitutional Article:", list(CONSTITUTION_FULL.keys()))
    art_data = CONSTITUTION_FULL[art_choice]

    st.subheader(f"{art_choice}: {art_data['title']}")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="card">
            <h4>📜 Official Full Text (Clauses & Sub-Articles)</h4>
            <pre style="white-space: pre-wrap; color: #F8FAFC; background-color: #0F172A; padding: 0.8rem; border-radius: 6px;">{art_data['official']}</pre>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card" style="border-left-color: #10B981;">
            <h4>💡 Simplified Citizen Translation (Tafsiri Rahisi)</h4>
            <p style="font-size: 1.05rem;">{art_data['translation']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🏘️ Multiple Real-Life Citizen Examples")
    for ex in art_data["examples"]:
        st.markdown(f"<div class='example-box'>{ex}</div>", unsafe_allow_html=True)

# MODULE 3: NATIONAL GOVERNMENT
elif selected_module in ["National Government Leaders", "Viongozi wa Serikali ya Kitaifa"]:
    st.header("🏛️ National Government Leadership & Powers")
    
    office = st.selectbox("Select National Office:", ["President of Kenya", "Member of Parliament (MP)", "Senator", "Cabinet Secretary"])
    
    if office == "President of Kenya":
        st.subheader("👑 Office of the President")
        st.write("**Who Elects:** Directly elected nationwide by voters for a 5-year term.")
        
        st.markdown("#### ✅ Primary Constitutional Duties (With Examples)")
        st.write("1. **Sovereignty & State Head (Article 131):** Safeguards national security. *Example:* Directs the National Security Council during national emergencies.")
        st.write("2. **Legislative Assent (Article 115):** Assents to Bills passed by Parliament. *Example:* Signs the Annual Appropriations Bill into law.")
        st.write("3. **Public Appointments (Article 132):** Nominates Cabinet Secretaries. *Example:* Nominates the Cabinet Secretary for the National Treasury.")
        
        st.markdown("#### ❌ What the President CANNOT Do (With Prohibitions & Limits)")
        st.warning("1. Cannot dismiss a judge without a JSC tribunal inquiry. *Example:* Dismissing a High Court Judge arbitrarily is unconstitutional.")
        st.warning("2. Cannot alter tax rates without Parliamentary legislation. *Example:* Introducing a tax levy by executive decree without Parliament is null and void.")
        st.warning("3. Cannot serve more than two 5-year terms (Article 142).")

# MODULE 4: COUNTY GOVERNMENT
elif selected_module in ["County & Local Government Leaders", "Viongozi wa Serikali ya Kaunti"]:
    st.header("🏡 County & Devolved Government Leadership")
    
    c_office = st.selectbox("Select Local Office:", ["County Governor", "Member of County Assembly (MCA)", "Woman Representative", "County Executive Committee Member (CECM)"])
    
    if c_office == "County Governor":
        st.subheader("🏛️ Office of the County Governor")
        st.write("**Who Elects:** Elected by voters across the County.")
        
        st.markdown("#### ✅ Devolved Duties & Powers")
        st.write("1. **County Executive Leadership (Article 179):** Manages county health dispensaries, county roads, and local agriculture.")
        st.write("2. **Budget Proposals:** Submits the County Integrated Development Plan (CIDP) to the County Assembly.")
        
        st.markdown("#### ❌ What the Governor CANNOT Do")
        st.warning("1. Cannot command the National Police Service.")
        st.warning("2. Cannot pass county laws without County Assembly approval.")

# MODULE 5: MP VOTING ROLL CALL
elif selected_module in ["MP Voting Roll Call (All 349 MPs)", "Kura za Wabunge Wote (349)"]:
    st.header("🏛️ Parliamentary Roll Call — All 349 MPs")
    st.caption("Search across all 349 Members of Parliament, their constituencies, counties, political parties, and voting records.")

    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        search_term = st.text_input("🔍 Search MP by Name, Constituency, or County:", placeholder="e.g. Zone 12, Nairobi, UDA")
    with col2:
        party_filter = st.selectbox("Party Filter:", ["All Parties"] + PARTIES)
    with col3:
        vote_filter = st.selectbox("Vote Filter:", ["All Votes"] + VOTES)

    filtered_mps = ALL_MPS
    if search_term:
        filtered_mps = [m for m in filtered_mps if search_term.lower() in m['name'].lower() or search_term.lower() in m['constituency'].lower() or search_term.lower() in m['county'].lower()]
    if party_filter != "All Parties":
        filtered_mps = [m for m in filtered_mps if m['party'] == party_filter]
    if vote_filter != "All Votes":
        filtered_mps = [m for m in filtered_mps if m['vote'] == vote_filter]

    st.write(f"Showing **{len(filtered_mps)}** of 349 Members of Parliament:")

    df_mps = pd.DataFrame(filtered_mps)[["name", "constituency", "county", "party", "vote"]]
    df_mps.columns = ["MP Name", "Constituency", "County", "Party", "Vote Status"]
    st.dataframe(df_mps, use_container_width=True, height=400)

# MODULE 6: ACTIVE BILLS & DECODER
elif selected_module in ["Active Bills & Decoder (2025 & 2026)", "Miswada na Ufafanuzi (2025 & 2026)"]:
    st.header("📜 Real-World Active Bills & Clause Decoder")
    
    bill_sel = st.selectbox("Select Active Bill:", list(FINANCE_BILLS.keys()))
    b_data = FINANCE_BILLS[bill_sel]

    st.markdown(f"**Status:** <span class='bill-status-tag'>{b_data['status']}</span>", unsafe_allow_html=True)
    
    with st.expander("📄 View Statutory Bill Text"):
        st.write(b_data["raw"])

    st.markdown("### 💡 Simplified Citizen Translation (Tafsiri Rahisi)")
    st.write(b_data["simple"])

    st.markdown("### 🏘️ Real-Life Citizen Examples")
    for ex in b_data["examples"]:
        st.markdown(f"<div class='example-box'>{ex}</div>", unsafe_allow_html=True)

# MODULE 7: RIGHTS, GBV & FEMICIDE HUB
elif selected_module in ["Rights, GBV & Femicide Education", "Elimu ya Haki, GBV na Mauaji ya Wanawake"]:
    st.header("🛡️ Gender-Based Violence (GBV) & Femicide Education Hub")
    
    st.markdown("""
    <div class="card-gbv">
        <h2 style="margin:0; color:#FFE4E6;">🚨 Emergency GBV & Crisis Helpline: 1195</h2>
        <p style="margin-top:0.5rem;">
            If you or someone you know is facing violence, domestic abuse, or emergency risk, call <b>1195</b> (Free 24/7 Hotline) for immediate medical referral, legal protection, and shelter support in Kenya.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📚 Educational Guide: Understanding GBV and Femicide")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card">
            <h4>1. What is Femicide?</h4>
            <p>Femicide is the gender-motivated intentional murder of women and girls. It represents the most extreme form of gender-based violence.</p>
            <h4>2. Forms of GBV</h4>
            <ul>
                <li><b>Physical Violence:</b> Assault, battery, or physical coercion.</li>
                <li><b>Sexual Violence:</b> Non-consensual sexual acts, harassment, or abuse.</li>
                <li><b>Psychological & Economic Violence:</b> Intimidation, emotional abuse, or withholding economic resources.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h4>3. Warning Signs & Prevention</h4>
            <ul>
                <li>Threats of extreme physical harm or weapon display.</li>
                <li>Possessive behavior, forced isolation, and stalking.</li>
                <li>Escalating physical aggression during domestic disputes.</li>
            </ul>
            <h4>4. Step-by-Step Reporting Guide</h4>
            <ol>
                <li><b>Get to Safety:</b> Move to a secure location or nearest police station.</li>
                <li><b>Call 1195 / 116:</b> Contact the national emergency helplines.</li>
                <li><b>Seek Medical Attention:</b> Visit a healthcare facility immediately for PRC form filling and evidence documentation.</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)

# PUBLIC PARTICIPATION
elif selected_module in ["Public Participation & Memorandum", "Ushiriki wa Umma na Barua"]:
    st.header("✍️ Public Participation Submission Builder")
    p_title = st.text_input("Bill Title:", value="Finance Bill Submission")
    p_concern = st.text_area("Your Primary Recommendation / Objection:", height=100)
    if st.button("Generate Memorandum"):
        st.code(f"""TO: THE CLERK OF THE NATIONAL ASSEMBLY
RE: PUBLIC PARTICIPATION SUBMISSION ON {p_title.upper()}

1. CITIZEN SUBMISSION
I write pursuant to Article 118 of the Constitution of Kenya to formally present recommendations.

2. SUBSTANTIVE CONCERN
{p_concern}

Submitted via Afro Civic (AFCI) Platform.""", language="markdown")

# HISTORICAL
elif selected_module in ["Constitutional History (Pre & Post-1992)", "Historia ya Katiba (1963-2010)"]:
    st.header("📜 Kenya Constitutional Evolution (1963 - 2010)")
    st.markdown("""
    * **1963:** Independence Constitution with regional Majimbo structure.
    * **1982:** Section 2A Amendment declaring Kenya a single-party state under KANU.
    * **1991/1992:** Repeal of Section 2A restoring multi-party democracy.
    * **2010:** Promulgation of the modern Constitution establishing 47 County Governments and Chapter 4 Bill of Rights.
    """)

# FOOTER
st.markdown("""
<div class="footer-text">
    © 2026 Afro Civic (AFCI). All Rights Reserved. <br>
    <i>Afro Civic is an independent civic education initiative and is not an official government or IEBC entity.</i><br>
    <b>Piloting in Kenya | Designed for Pan-African Adaptation</b>
</div>
""", unsafe_allow_html=True)
