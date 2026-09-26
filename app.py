Comprehensive Civic Guide & Institutional Framework of the 13th Parliament of Kenya
----------------------------------------------------------------------------------
This script encodes statutory breakdowns, public participation memorandum generators,
civic advocacy frameworks, constitutional summaries, and structural records for both 
the Senate and the National Assembly of Kenya.
"""

from dataclasses import dataclass, field
from datetime import date
from typing import List, Dict, Optional, Union


# ==============================================================================
# SECTION 1: CITIZEN CIVIC GUIDE & STATUTORY BREAKDOWNS
# ==============================================================================

@dataclass
class StatutoryProvision:
    section_number: str
    title: str
    statutory_text: str
    plain_translation: str

@dataclass
class LegislativeBill:
    title: str
    gazette_supplement: str
    bill_number: str
    enactment_status: str
    publication_date: date
    table_office_date: date
    mover: Optional[str]
    sections: List[StatutoryProvision]

# --- Finance Bill 2025 ---
finance_bill_2025 = LegislativeBill(
    title="The Finance Bill, 2025",
    gazette_supplement="Kenya Gazette Supplement No. 63",
    bill_number="National Assembly Bills No. 19",
    enactment_status="Published and Tabled",
    publication_date=date(2025, 5, 6),
    table_office_date=date(2025, 5, 7),
    mover="Chairperson, Departmental Committee on Finance and National Planning",
    sections=[
        StatutoryProvision(
            section_number="Section 1",
            title="Preliminary - Commencement",
            statutory_text="This Act may be cited as the Finance Act, 2025 and shall come into operation as follows— "
                           "(a) sections 12 and 56, on the 1st of January, 2026; and "
                           "(b) all other sections, on 1st July, 2025.",
            plain_translation="Most tax changes in this bill start on July 1, 2025, while rules regarding "
                              "Advance Pricing Agreements (Section 12) and KRA system error penalty waivers "
                              "(Section 56) start on January 1, 2026."
        ),
        StatutoryProvision(
            section_number="Section 3",
            title="Employment Gains - Gratuity & Allowances",
            statutory_text="Section 5 of the Income Tax Act is amended in item (iii) of the proviso to "
                           "subsection (2)(a), by deleting the words 'two thousand shillings' and "
                           "substituting therefor the words 'ten thousand shillings'.",
            plain_translation="When an employee travels out of their usual workstation on official duty, "
                              "the non-taxable daily allowance/per diem limit is increased from KSh 2,000 per day "
                              "to KSh 10,000 per day."
        ),
        StatutoryProvision(
            section_number="Section 26",
            title="Income Exempt from Tax - SHIF",
            statutory_text="The First Schedule to the Income Tax Act is amended... by deleting paragraph 45A and "
                           "substituting therefor the following new paragraph— 45A. All contributions and other payments "
                           "into and out of the Social Health Insurance Fund established under section 25 of the "
                           "Social Health Insurance Act, 2023.",
            plain_translation="All money paid into SHIF by citizens and all benefits paid out by SHIF for medical cover "
                              "are legally tax-exempt."
        ),
        StatutoryProvision(
            section_number="Section 36",
            title="VAT Exemptions & Zero-Rating Adjustments",
            statutory_text="The First Schedule to the Value Added Tax Act is amended... by inserting the following "
                           "new paragraphs... 157. Transportation of sugarcane from farms to milling factories. "
                           "158. The supply of locally assembled and manufactured mobile phones. 159. The supply of "
                           "motorcycles of tariff heading 8711.60.00. 160. The supply of electric bicycles. "
                           "161. The supply of solar and lithium ion batteries. 162. The supply of electric buses...",
            plain_translation="To promote local manufacturing and green energy, 16% VAT is removed from locally made "
                              "mobile phones, electric bikes, electric buses, solar batteries, and sugarcane farm transport."
        ),
        StatutoryProvision(
            section_number="Section 56",
            title="Waiver of Penalties Due to KRA System Failures",
            statutory_text="Section 89 of the Tax Procedures Act is amended... (5A) The Cabinet Secretary may, on the "
                           "recommendation of the Commissioner, waive the whole or part of any penalty or interest "
                           "imposed under this Act where the liability to pay the penalty or interest was due to— "
                           "(a) an error generated by an electronic tax system; (b) a delay in the updating of an electronic "
                           "tax system; (c) a duplication of a penalty or interest due to a malfunction of an electronic tax "
                           "system; or (d) the incorrect registration of the tax obligations of a taxpayer.",
            plain_translation="If KRA's online system (eTIMS/iTax) glitches, delays updating, or wrongly charges you "
                              "penalties or interest, the Cabinet Secretary can officially forgive and clear those fines."
        ),
    ]
)

# --- Finance Bill 2026 ---
finance_bill_2026 = LegislativeBill(
    title="The Finance Bill, 2026",
    gazette_supplement="Kenya Gazette Supplement No. 113",
    bill_number="National Assembly Bills No. 26",
    enactment_status="Published and Tabled",
    publication_date=date(2026, 5, 5),
    table_office_date=date(2026, 5, 5),
    mover="Hon. Kuria Kimani, MP (Chairperson, Departmental Committee on Finance and National Planning)",
    sections=[
        StatutoryProvision(
            section_number="Section 2",
            title="Digital Platforms & Merchant Fees",
            statutory_text="Section 2 of the Income Tax Act is amended... (b) in the definition of 'management or "
                           "professional fee' by inserting the words 'and includes interchange fees and merchant "
                           "service fees arising from transactions that use a card or an electronic payment' "
                           "immediately after the word 'calculated'; (c) by deleting the definition of 'royalty' "
                           "and substituting therefor the following new definition— 'royalty' means a payment made as a "
                           "consideration for... (iv) any software, proprietary or off-the-shelf, whether in the form "
                           "of licence, development, training, maintenance or support fees...",
            plain_translation="Banks, card providers, and mobile payment platforms charging transaction fees to "
                              "shop owners/merchants will now have those fees taxed under professional service withholding taxes. "
                              "Software subscriptions are explicitly categorized as royalties for tax purposes."
        ),
        StatutoryProvision(
            section_number="Section 36",
            title="Excise Duty - Betting & Digital Assets",
            statutory_text="Part II of the First Schedule to the Excise Duty Act is amended... 4B. Excise duty on gaming "
                           "or betting shall be five percent on the amount deposited into a customer's betting wallet. "
                           "8. Excise duty on fees charged on virtual asset transactions by virtual asset service "
                           "providers shall be ten percent of the excisable value.",
            plain_translation="Every time you deposit money into a betting account, 5% excise duty is deducted immediately. "
                              "Crypto and virtual asset trading platforms will also charge 10% tax on transaction fees."
        ),
    ]
)


# --- Public Participation Email Memorandum Generator ---

@dataclass
class CitizenProfile:
    full_name: str
    national_id: str
    county_constituency: str
    phone_number: str
    email_address: str

class PublicParticipationMemorandum:
    RECIPIENT_TITLE = "The Clerk of the National Assembly"
    RECIPIENT_ADDRESS = "Parliament Buildings, P.O. Box 41842-00100, Nairobi, Kenya."
    RECIPIENT_EMAILS = ["clerk.nationalassembly@parliament.go.ke", "cna@parliament.go.ke"]

    @staticmethod
    def generate_email_text(citizen: CitizenProfile, bill_title: str = "FINANCE BILL 2026") -> str:
        return f"""TO: {PublicParticipationMemorandum.RECIPIENT_TITLE},
{PublicParticipationMemorandum.RECIPIENT_ADDRESS}
EMAIL: {', '.join(PublicParticipationMemorandum.RECIPIENT_EMAILS)}

SUBJECT: SUBMISSION OF PUBLIC PARTICIPATION MEMORANDUM ON THE {bill_title}

Dear Sir/Madam,

RE: CITIZEN SUBMISSION AND OBJECTIONS TO SPECIFIC PROVISIONS OF THE {bill_title}

I am writing as a citizen of Kenya to exercise my constitutional right under Articles 10(2)(a) and 118(1)(b) of the Constitution of Kenya, 2010, which mandate public participation in the legislative processes of Parliament.

Having reviewed the published text of the {bill_title}, I wish to submit the following comments, objections, and proposed amendments for consideration by the Departmental Committee on Finance and National Planning:

1. OBJECTION TO EXCISE DUTY ON DIGITAL & FINANCIAL TRANSACTIONS (SECTION 36):
   - Proposal: The introduction/elevation of excise duties on digital service fees and betting wallet deposits disproportionately burden young citizens and micro-entrepreneurs relying on digital platforms for livelihood.
   - Recommendation: Delete or reduce the proposed excise rates on virtual asset service fees and digital payment transactions to preserve financial inclusion.

2. CALL FOR TRANSPARENCY IN SYSTEM ERROR WAIVERS (SECTION 56 OF TPA AMENDMENTS):
   - Proposal: While acknowledging the need to forgive penalties arising from KRA system glitches (eTIMS/iTax), the process must be automated rather than left to discretionary approval by the Cabinet Secretary.
   - Recommendation: Amend the clause to require automatic reversal of wrongfully assessed penalties upon system audit, without requiring individual administrative appeals.

3. DRAFTING OF CLEARER CITIZEN TAXATION GUIDELINES:
   - Request: Parliament should ensure that statutory definitions regarding income tax, royalties, and digital marketplace tax are accompanied by clear, non-ambiguous schedules written in plain language.

I urge the Committee to consider these recommendations in its final report to the House. I remain available to make oral submissions should the Committee convene public hearings.

Yours faithfully,

{citizen.full_name}
National ID: {citizen.national_id}
County/Constituency: {citizen.county_constituency}
Phone: {citizen.phone_number} | Email: {citizen.email_address}
"""


# --- Human Rights, GBV, & Femicide Advocacy Framework ---

@dataclass
class GBVStatistics:
    kdhs_physical_violence_women_pct: float = 34.0
    kdhs_sexual_violence_women_pct: float = 13.0
    annual_femicide_documented_cases: int = 150

@dataclass
class AdvocacyDemand:
    target_body: str
    mandate: str
    action_items: List[str]

gbv_advocacy_framework = {
    "definitions": {
        "GBV": "Any harmful act committed against a person based on socially ascribed gender differences (physical, sexual, psychological, or economic).",
        "Femicide": "The intentional killing of women and girls because of their gender—the ultimate expression of misogyny and systemic violence."
    },
    "statistics": GBVStatistics(),
    "civic_demands": [
        AdvocacyDemand(
            target_body="National Assembly & County Assemblies",
            mandate="Budgetary Allocation",
            action_items=["Allocate funds under Appropriation Acts for GBV Recovery Centres (GBVRCs) and safe shelters across all 47 counties."]
        ),
        AdvocacyDemand(
            target_body="Law Enforcement & Judiciary",
            mandate="Protection & Justice Enforcement",
            action_items=[
                "Establish dedicated Gender Desks staffed by specialized officers at every police station.",
                "Rapid-track judicial processing of femicide and domestic violence cases under the Protection Against Domestic Violence Act (PADVA) 2015."
            ]
        )
    ]
}


# --- Constitutional Structure (18 Chapters) ---

@dataclass
class ConstitutionalChapter:
    number: int
    title: str
    articles: str
    plain_language_summary: str

kenya_constitution_chapters = [
    ConstitutionalChapter(1, "Sovereignty & Supremacy", "Arts. 1–3", "Power belongs to citizens; the Constitution is the highest law above all leaders."),
    ConstitutionalChapter(2, "The Republic", "Arts. 4–11", "Defines Kenya’s territory, national symbols, national values, and county boundaries."),
    ConstitutionalChapter(3, "Citizenship", "Arts. 12–18", "Explains how you become a citizen (birth/registration) and rights to dual citizenship."),
    ConstitutionalChapter(4, "The Bill of Rights", "Arts. 19–59", "Protects basic freedoms: right to life, health, housing, education, free speech, and equality."),
    ConstitutionalChapter(5, "Land & Environment", "Arts. 60–72", "Rules governing Public, Community, and Private land, and protection of natural resources."),
    ConstitutionalChapter(6, "Leadership & Integrity", "Arts. 73–80", "Requires state officers to maintain high ethical standards, avoid corruption, and serve the public."),
    ConstitutionalChapter(7, "Representation", "Arts. 81–92", "Rules for elections, voting rights, political parties, and the establishment of IEBC."),
    ConstitutionalChapter(8, "The Legislature", "Arts. 93–128", "Defines the roles of Parliament (National Assembly & Senate) and mandates public participation."),
    ConstitutionalChapter(9, "The Executive", "Arts. 129–158", "Outlines powers of the President, Deputy President, Cabinet Secretaries, and Attorney General."),
    ConstitutionalChapter(10, "Judiciary", "Arts. 159–173", "Powers of the Courts (Supreme Court, Court of Appeal, High Court) and the Judicial Service Commission."),
    ConstitutionalChapter(11, "Devolved Government", "Arts. 174–200", "Sets up the 47 County Governments (Governors and County Assemblies) to bring services closer to citizens."),
    ConstitutionalChapter(12, "Public Finance", "Arts. 201–231", "Controls how tax money is raised, budgeted, shared between National & County levels, and audited."),
    ConstitutionalChapter(13, "The Public Service", "Arts. 232–236", "Governs public officers, civil service standards, and agencies like PSC and TSC."),
    ConstitutionalChapter(14, "National Security", "Arts. 237–247", "Rules governing the Kenya Defence Forces (KDF), NIS, and National Police Service."),
    ConstitutionalChapter(15, "Commissions & Offices", "Arts. 248–254", "Sets up independent bodies like KNCHR, NGEC, CRA, Auditor-General, and Controller of Budget."),
    ConstitutionalChapter(16, "Amending the Constitution", "Arts. 255–257", "How to change the Constitution (Parliamentary path vs. Citizen Referendum / Popular Initiative)."),
    ConstitutionalChapter(17, "General Provisions", "Arts. 258–260", "Legal definitions and rules on how to interpret constitutional text in court."),
    ConstitutionalChapter(18, "Transitional Provisions", "Arts. 261–264", "Rules on how Kenya moved from the 1963/1969 Constitution to full implementation of 2010.")
]


# ==============================================================================
# SECTION 2: PARLIAMENTARY LEADERSHIP, SENATE & NATIONAL ASSEMBLY STRUCTURES
# ==============================================================================

@dataclass
class Parliamentarian:
    name: str
    role_or_constituency: str
    party_coalition: str
    county: Optional[str] = None

@dataclass
class Committee:
    name: str
    responsibility: str
    chairperson: str
    vice_chairperson: Optional[str] = None


# --- 1. THE SENATE (THE UPPER HOUSE) ---

class SenateStructure:
    PRIMARY_FUNCTION = (
        "Represents the 47 counties, protects devolution, makes laws affecting county governments, "
        "allocates national revenue to counties, and oversights county government expenditure."
    )
    TOTAL_MEMBERS = 67
    ELECTED_COUNTY_MEMBERS = 47
    NOMINATED_MEMBERS = 20

    LEADERSHIP = {
        "Speaker": Parliamentarian("Sen. Amason Jeffah Kingi, EGH", "Speaker of the Senate", "Ex-Officio / Kenya Kwanza"),
        "Deputy Speaker": Parliamentarian("Sen. Kathuri Murungi, MP", "Deputy Speaker / Meru", "UDA / Kenya Kwanza", "Meru"),
        "Majority Leader": Parliamentarian("Sen. Aaron Kipkirui Cheruiyot, EGH, MP", "Leader of the Majority Party", "UDA / Kenya Kwanza", "Kericho"),
        "Deputy Majority Leader": Parliamentarian("Sen. Hillary Kiprotich Sigei, MP", "Deputy Majority Leader", "UDA / Kenya Kwanza", "Bomet"),
        "Majority Whip": Parliamentarian("Sen. Boni Khalwale, CBS, MP", "Majority Whip", "UDA / Kenya Kwanza", "Kakamega"),
        "Deputy Majority Whip": Parliamentarian("Sen. Steve Lelegwe Ltumbesi, MP", "Deputy Majority Whip", "UDA / Kenya Kwanza", "Samburu"),
        "Minority Leader": Parliamentarian("Sen. (Rtd.) Justice Stewart M. Madzayo, CBS, MP", "Leader of the Minority Party", "ODM / Azimio", "Kilifi"),
        "Deputy Minority Leader": Parliamentarian("Sen. Enoch Kiio Wambua, CBS, MP", "Deputy Minority Leader", "Wiper / Azimio", "Kitui"),
        "Minority Whip": Parliamentarian("Sen. Ledama Olekina, MP", "Minority Whip", "ODM / Azimio", "Narok"),
        "Deputy Minority Whip": Parliamentarian("Sen. Edwin Sifuna, MP", "Deputy Minority Whip", "ODM / Azimio", "Nairobi")
    }

    COMMITTEES = [
        Committee("Finance and Budget", "Examines county revenue sharing, national budget allocations to counties, public debt.", "Sen. Ali Roba Ibrahim", "Sen. Tabitha Karanja Keroche"),
        Committee("County Public Accounts Committee (CPAC)", "Examines Auditor-General reports on county government expenditure.", "Sen. Moses Otieno Kajwang'", "Sen. Julius Murgor"),
        Committee("County Public Investments and Special Funds (CPIC)", "Oversights county public investments, water companies, emergency funds.", "Sen. Godfrey Osotsi", "Sen. Prof. Tom Ojienda, SC"),
        Committee("Health", "Oversights county health services, hospital infrastructure, health worker management.", "Sen. Jackson Mandago", "Sen. Mariam Sheikh Omar"),
        Committee("Education", "Oversights ECDE and vocational training centers under county jurisdiction.", "Sen. Joseph Kamau Nyutu", "Sen. Peris Tobiko"),
        Committee("Justice, Legal Affairs and Human Rights (JLAC)", "Human rights oversight, constitutional implementation, statutory instruments.", "Sen. Hillary Kiprotich Sigei", "Sen. Raphael Mwinzago Chimera"),
        Committee("Roads, Transportation and Housing", "Oversights county transport, roads, and housing infrastructure.", "Sen. Karungo wa Thang'wa"),
        Committee("Agriculture, Livestock and Fisheries", "Oversights county agricultural and livestock policy implementation.", "Sen. James Kamau Murango"),
        Committee("Energy", "Oversights energy development and distribution affecting counties.", "Sen. Wahome Wamatinga"),
        Committee("National Security, Defence and Foreign Relations", "Oversights security and international relations matters.", "Sen. William Cheptumo"),
        Committee("Labour and Social Welfare", "Oversights labor policies and social protection.", "Sen. Julius Murgor"),
        Committee("Lands, Environment and Natural Resources", "Oversights land policy, environmental protection, natural resources.", "Sen. John Methu")
    ]

    ELECTED_SENATORS = {
        "Baringo": "Sen. William Cheptumo (UDA)", "Bomet": "Sen. Hillary Kiprotich Sigei (UDA)",
        "Bungoma": "Sen. David Wakoli Wafula (FORD-Kenya)", "Busia": "Sen. Andrew Omtatah Okoiti (NRA)",
        "Elgeyo Marakwet": "Sen. William Kisang (UDA)", "Embu": "Sen. Alexander Mundigi Munyi (Democratic Party)",
        "Garissa": "Sen. Abdulkadir Mohamed Haji (Jubilee)", "Homa Bay": "Sen. Moses Otieno Kajwang' (ODM)",
        "Isiolo": "Sen. Fatuma Adan Dullo (Jubilee)", "Kajiado": "Sen. Kanar Seki (UDA)",
        "Kakamega": "Sen. Boni Khalwale (UDA)", "Kericho": "Sen. Aaron Kipkirui Cheruiyot (UDA)",
        "Kiambu": "Sen. Karungo wa Thang'wa (UDA)", "Kilifi": "Sen. Justice Stewart M. Madzayo (ODM)",
        "Kirinyaga": "Sen. James Kamau Murango (UDA)", "Kisii": "Sen. Richard Onyonka (ODM)",
        "Kisumu": "Sen. Prof. Tom Ojienda, SC (ODM)", "Kitui": "Sen. Enoch Kiio Wambua (Wiper)",
        "Kwale": "Sen. Issa Juma Boy (ODM)", "Laikipia": "Sen. John Kinyua Nderitu (UDA)",
        "Lamu": "Sen. Joseph Githuku Kamau (UDA)", "Machakos": "Sen. Agnes Kavindu Muthama (Wiper)",
        "Makueni": "Sen. Daniel Kitonga Maanzo (Wiper)", "Mandera": "Sen. Ali Roba Ibrahim (UDM)",
        "Marsabit": "Sen. Mohamed Said Chute (UDA)", "Meru": "Sen. Kathuri Murungi (UDA)",
        "Migori": "Sen. Eddy Gicheru Oketch (ODM)", "Mombasa": "Sen. Mohamed Faki Mwinyihaji (ODM)",
        "Murang'a": "Sen. Joseph Kamau Nyutu (UDA)", "Nairobi": "Sen. Edwin Sifuna (ODM)",
        "Nakuru": "Sen. Tabitha Karanja Keroche (UDA)", "Nandi": "Sen. Samson Cherargei (UDA)",
        "Narok": "Sen. Ledama Olekina (ODM)", "Nyamira": "Sen. Okong'o Omogeni, SC (ODM)",
        "Nyandarua": "Sen. John Methu (UDA)", "Nyeri": "Sen. Wahome Wamatinga (UDA)",
        "Samburu": "Sen. Steve Lelegwe Ltumbesi (UDA)", "Siaya": "Sen. Oburu Oginga (ODM)",
        "Taita Taveta": "Sen. Johnes Mwaruma (ODM)", "Tana River": "Sen. Danson Buya Mungatana (UDA)",
        "Tharaka Nithi": "Sen. Mwenda Gataya Mo Fire (UDA)", "Trans Nzoia": "Sen. Allan Kiprotich Chesang (UDA)",
        "Turkana": "Sen. James Lomenen Ekitela (UDA)", "Uasin Gishu": "Sen. Jackson Mandago (UDA)",
        "Vihiga": "Sen. Godfrey Osotsi (ODM)", "Wajir": "Sen. Mohamed Abass Sheikh (UDM)",
        "West Pokot": "Sen. Julius Murgor (UDA)"
    }


# --- 2. THE NATIONAL ASSEMBLY (THE LOWER HOUSE) ---

class NationalAssemblyStructure:
    PRIMARY_FUNCTION = (
        "Passes national legislation, raises revenue through taxation (Finance Bills), "
        "allocates national funds, and oversights national government expenditure and ministries."
    )
    TOTAL_MEMBERS = 349
    CONSTITUENCY_MPS = 290
    COUNTY_WOMAN_REPS = 47
    NOMINATED_MEMBERS = 12

    LEADERSHIP = {
        "Speaker": Parliamentarian("Hon. Moses Wetang'ula, EGH", "Speaker of the National Assembly", "Ex-Officio / Kenya Kwanza"),
        "Deputy Speaker": Parliamentarian("Hon. Gladys Boss Shollei, CBS, MP", "Deputy Speaker / Uasin Gishu Woman Rep", "UDA / Kenya Kwanza", "Uasin Gishu"),
        "Majority Leader": Parliamentarian("Hon. Kimani Ichung'wah, EGH, MP", "Leader of the Majority Party / Kikuyu", "UDA / Kenya Kwanza", "Kiambu"),
        "Deputy Majority Leader": Parliamentarian("Hon. Owen Baya, MP", "Deputy Majority Leader / Kilifi North", "UDA / Kenya Kwanza", "Kilifi"),
        "Majority Whip": Parliamentarian("Hon. Silvanus Osoro, MP", "Majority Whip / South Mugirango", "UDA / Kenya Kwanza", "Kisii"),
        "Deputy Majority Whip": Parliamentarian("Hon. Naomi Jillo Wqo, MP", "Deputy Majority Whip / Marsabit Woman Rep", "UDA / Kenya Kwanza", "Marsabit"),
        "Minority Leader": Parliamentarian("Hon. Junet Mohamed, CBS, MP", "Leader of the Minority Party / Suna East", "ODM / Azimio", "Migori"),
        "Deputy Minority Leader": Parliamentarian("Hon. Robert Mbui, MP", "Deputy Minority Leader / Kathiani", "Wiper / Azimio", "Machakos"),
        "Minority Whip": Parliamentarian("Hon. Millie Odhiambo-Mabona, MP", "Minority Whip / Suba North", "ODM / Azimio", "Homa Bay"),
        "Deputy Minority Whip": Parliamentarian("Hon. Mark Nyamita, MP", "Deputy Minority Whip / Uriri", "ODM / Azimio", "Migori")
    }

    COMMITTEES = [
        Committee("Finance and National Planning", "Scrutinizes tax laws, public debt, financial policy, KRA, CBK, Finance Bills.", "Hon. Kuria Kimani", "Hon. Benjamin Langat"),
        Committee("Budget and Appropriations Committee (BAC)", "Formulates national budget allocations, reviews estimates, sets spending ceilings.", "Hon. Ndindi Nyoro", "Hon. Samuel Atandi"),
        Committee("Public Accounts Committee (PAC)", "Oversights national government accounts based on Auditor-General reports.", "Hon. John Mbadi / Hon. Mark Nyamita"),
        Committee("PIC on Governance and Education", "Oversights governance and education state corporations.", "Hon. Jack Wamboka"),
        Committee("PIC on Commercial and Energy State Corporations", "Oversights commercial and energy state corporations.", "Hon. David Pkosing"),
        Committee("Justice and Legal Affairs (JLAC)", "Handles legal affairs, constitutional bodies, and electoral matters.", "Hon. George Murugara"),
        Committee("Administration and Internal Affairs", "Oversights internal security, police, administrative services.", "Hon. Gabriel Tongoyo"),
        Committee("Health", "Oversights national health policy and referral hospitals.", "Hon. Dr. Robert Pukose"),
        Committee("Education and Research", "Oversights national education policy, primary, secondary, and higher learning.", "Hon. Julius Melly"),
        Committee("Energy", "Oversights electrical energy, petroleum, and nuclear power policy.", "Hon. Vincent Musyoka Musau"),
        Committee("Transport, Industry and Infrastructure", "Oversights national roads, rail, maritime, aviation, and infrastructure.", "Hon. George Kariuki"),
        Committee("Agriculture and Livestock", "Oversights national agricultural policy, crops, and livestock.", "Hon. John Mutunga")
    ]

    CLERK_CONTACTS = {
        "National Assembly": {
            "title": "The Clerk of the National Assembly",
            "office": "Main Parliament Buildings, P.O. Box 41842-00100, Nairobi",
            "emails": ["clerk.nationalassembly@parliament.go.ke", "cna@parliament.go.ke"]
        },
        "Senate": {
            "title": "The Clerk of the Senate",
            "office": "Main Parliament Buildings, P.O. Box 41842-00100, Nairobi",
            "emails": ["clerk.senate@parliament.go.ke"]
        }
    }


# ==============================================================================
# RUNTIME DEMONSTRATION & VERIFICATION
# ==============================================================================

if __name__ == "__main__":
    print("==================================================================")
    print("CIVIC GUIDE & INSTITUTIONAL FRAMEWORK OF 13TH PARLIAMENT OF KENYA")
    print("==================================================================\n")

    # 1. Legislative Bills Summary
    print(f"--- LEGISLATIVE BILL: {finance_bill_2025.title} ---")
    print(f"Status: {finance_bill_2025.enactment_status} ({finance_bill_2025.gazette_supplement})")
    for sec in finance_bill_2025.sections[:2]:
        print(f"\n[{sec.section_number}: {sec.title}]")
        print(f"Text: {sec.statutory_text}")
        print(f"Plain Translation: {sec.plain_translation}")

    print(f"\n--- LEGISLATIVE BILL: {finance_bill_2026.title} ---")
    print(f"Status: {finance_bill_2026.enactment_status} ({finance_bill_2026.gazette_supplement})")
    for sec in finance_bill_2026.sections:
        print(f"\n[{sec.section_number}: {sec.title}]")
        print(f"Plain Translation: {sec.plain_translation}")

    # 2. Public Participation Email Generator
    sample_citizen = CitizenProfile(
        full_name="Amina Otieno Wanjiku",
        national_id="38291047",
        county_constituency="Nairobi County / Lang'ata Constituency",
        phone_number="+254 712 345 678",
        email_address="amina.otieno@example.com"
    )
    print("\n==================================================================")
    print("GENERATING PUBLIC PARTICIPATION MEMORANDUM EMAIL")
    print("==================================================================\n")
    email_output = PublicParticipationMemorandum.generate_email_text(sample_citizen)
    print(email_output)

    # 3. Senate & National Assembly Overview
    print("==================================================================")
    print("PARLIAMENTARY STRUCTURES")
    print("==================================================================")
    print(f"Senate Speaker: {SenateStructure.LEADERSHIP['Speaker'].name}")
    print(f"Senate Majority Leader: {SenateStructure.LEADERSHIP['Majority Leader'].name}")
    print(f"National Assembly Speaker: {NationalAssemblyStructure.LEADERSHIP['Speaker'].name}")
    print(f"National Assembly Majority Leader: {NationalAssemblyStructure.LEADERSHIP['Majority Leader'].name}")
    print(f"Finance Committee Chair (NA): {NationalAssemblyStructure.COMMITTEES[0].chairperson}")
