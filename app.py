import calendar
from dataclasses import dataclass, field
from datetime import date
from typing import Dict, List, Optional, Union

# ==============================================================================
# SECTION 1: FINANCE BILL 2025 (PART I & PART II - PROGRAMMATIC LOGIC)
# ==============================================================================

# --- META DATA & PREAMBLE ---
GAZETTE_SUPPLEMENT = "Kenya Gazette Supplement No. 63"
NATIONAL_ASSEMBLY_BILL_NO = 19
PUBLICATION_DATE = date(2025, 5, 6)
PUBLICATION_PLACE = "Nairobi"
BILL_TITLE = "THE FINANCE BILL, 2025"
ACT_PURPOSE = (
    "AN ACT of Parliament to amend the laws relating to various taxes and duties; "
    "and for matters incidental thereto."
)
ENACTING_BODY = "Parliament of Kenya"


# --- PART I: PRELIMINARY ---
class CommencementDates:
    SECTION_12_AND_56 = date(2026, 1, 1)
    ALL_OTHER_SECTIONS = date(2025, 7, 1)

    @classmethod
    def get_effective_date(cls, section_number: int) -> date:
        """Section 1: Commencement schedule determination."""
        if section_number in (12, 56):
            return cls.SECTION_12_AND_56
        return cls.ALL_OTHER_SECTIONS


# --- PART II: INCOME TAX ACT AMENDMENTS ---
@dataclass
class RelatedPerson:
    """Section 2(a)(vii): Definition of Related Person."""
    person_id: str
    management_participation: bool = False
    control_participation: bool = False
    capital_participation: bool = False
    marriage_consanguinity_affinity_association: bool = False

    def is_related_to(self, other: 'RelatedPerson') -> bool:
        """Determines direct/indirect control or relational association between two entities."""
        direct_control = (
            self.management_participation or 
            self.control_participation or 
            self.capital_participation
        )
        indirect_association = (
            self.marriage_consanguinity_affinity_association and 
            (other.management_participation or other.control_participation or other.capital_participation)
        )
        return direct_control or indirect_association


class IncomeTaxActAmendments:
    """Encapsulates amendments enacted in Part II (Sections 2 - 12) of the Finance Bill, 2025."""

    @staticmethod
    def section_2_amendments():
        """Section 2: Definition Updates."""
        return {
            "debenture": "Deleted expression: 'and, for the purposes of paragraphs (d) and (e) of section 7(1) of this Act, includes any loan or loan stock, whether secured or unsecured'",
            "individual_retirement_fund": "Deleted: 'subject to the Income Tax (Retirement Benefit) Rules'",
            "royalty": "Expanded paragraph (b) to include: 'and includes the distribution of software where regular payments are made for the use of the software through the distributor'",
            "compensating_tax": "DELETED",
            "tribunal": "DELETED",
            "venture_company": "DELETED",
            "subsection_2": "DELETED"
        }

    @staticmethod
    def section_3_daily_per_diem_limit(current_limit: float) -> float:
        """
        Section 3: Amends Section 5(2)(a)(iii) proviso.
        Updates daily tax-free threshold from 2,000 KES to 10,000 KES.
        """
        NEW_LIMIT = 10000.00
        return NEW_LIMIT

    @staticmethod
    def section_4_gender_neutrality_and_deletions():
        """Section 4: Section 8 Amendments."""
        return {
            "gender_neutrality": "Substituted 'husband' with 'spouse' in subsection (1)",
            "deleted_subsections": [4, 5, 6, 7, 9, "9A"]
        }

    @staticmethod
    def section_5_withholding_tax_scope() -> List[str]:
        """
        Section 5: Amends Section 10(1) to insert new income streams.
        """
        return [
            "(l) supply of goods to a public entity",
            "(m) sale of scrap"
        ]

    @staticmethod
    def section_6_digital_marketplace_tax():
        """Section 6: Amends Section 12E for electronic networks and digital marketplace scope."""
        return {
            "scope_expansion": "Inserted 'the internet or an electronic network including through' immediately after 'carried out over'",
            "deleted_paragraphs": ["subsection (3)(d)"]
        }

    @staticmethod
    def calculate_minimum_top_up_tax_due_date(financial_year_end_date: date) -> date:
        """
        Section 7: Inserts Subsection 12G(3A).
        Minimum top-up tax payable by end of the 4th month post fiscal year-end.
        """
        year = financial_year_end_date.year
        month = financial_year_end_date.month + 4
        if month > 12:
            month -= 12
            year += 1
        
        _, last_day = calendar.monthrange(year, month)
        return date(year, month, last_day)

    @staticmethod
    def section_8_deductions_allowance():
        """Section 8: Amends Section 15(2), (3), (4), (5), and (7)."""
        return {
            "diminution_of_implements": "100% deduction rate applied in that year of income for non-machinery implements/utensils employed in production",
            "public_sports_facility": "Expenditure incurred in construction of public sports facility allowed",
            "loss_carry_forward": "Tax loss carry-forward deduction period limited to five (5) succeeding years",
            "cs_power_extension_deleted": "Subsection 15(5) allowing Cabinet Secretary extensions beyond 10 years DELETED"
        }

    @staticmethod
    def section_9_disallowed_deductions():
        """Section 9: Amends Section 16."""
        return {
            "compensating_tax": "Deleted 'including compensating tax' reference from section 16(2)(c)",
            "subsection_4": "DELETED"
        }

    @staticmethod
    def section_11_cbcr_notification(reporting_year_end: date) -> Dict[str, str]:
        """
        Section 11: Amends Section 18D(8) & (9).
        Country-by-Country Reporting (CbCR) notification rules.
        """
        return {
            "deadline": f"Must notify Commissioner by last day of reporting year: {reporting_year_end.strftime('%Y-%m-%d')}",
            "requirement": "Submit notification regarding CbCR filing in designated format"
        }


@dataclass
class AdvancePricingAgreement:
    """
    Section 12: Inserts Section 18G into the Income Tax Act.
    Governance for Advance Pricing Agreements (APA) between Taxpayers and Commissioner.
    """
    agreement_id: str
    taxpayer_id: str
    commencement_date: date
    duration_years: int
    arm_length_methodology: str
    is_misrepresented: bool = False

    def validate_duration(self) -> bool:
        """Subsection 18G(3): APA validity cannot exceed 5 consecutive years."""
        return 0 < self.duration_years <= 5

    def check_validity_status(self) -> Dict[str, Union[bool, str]]:
        """Subsection 18G(4): Fraud / Misrepresentation Clause."""
        if self.is_misrepresented:
            return {
                "status": "VOID",
                "notice_required": True,
                "action": "Commissioner shall declare the agreement void and issue a written notice of declaration to the person."
            }
        return {
            "status": "VALID" if self.validate_duration() else "EXCEEDED_MAX_TERM",
            "notice_required": False,
            "action": "Active Advance Pricing Agreement."
        }


# ==============================================================================
# SECTION 2: CITIZEN CIVIC GUIDE, ADVOCACY & CONSTITUTIONAL STRUCTURE
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

# --- Finance Bill 2025 Structured Record ---
finance_bill_2025_civic_record = LegislativeBill(
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

# --- Finance Bill 2026 Structured Record ---
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
                           "8. Excise duty on fees charged on virtual assets transactions by virtual asset service "
                           "providers shall be ten percent of the excisable value.",
            plain_translation="Every time you deposit money into a betting account, 5% excise duty is deducted immediately. "
                              "Crypto and virtual asset trading platforms will also charge 10% tax on transaction fees."
        ),
    ]
)


# --- Public Participation Generator ---
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


# --- Constitutional Structure ---
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
# SECTION 3: PARLIAMENTARY STRUCTURE (SENATE & NATIONAL ASSEMBLY)
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


# ==============================================================================
# SECTION 4: UNIFIED RUNTIME EXECUTION
# ==============================================================================

if __name__ == "__main__":
    print(f"Loaded {BILL_TITLE} ({GAZETTE_SUPPLEMENT})")
    
    # 1. Section 12 Advance Pricing Agreement (APA) Validation Logic
    apa = AdvancePricingAgreement(
        agreement_id="APA-2026-001",
        taxpayer_id="P051234567X",
        commencement_date=date(2026, 1, 1),
        duration_years=5,
        arm_length_methodology="Transactional Net Margin Method (TNMM)",
        is_misrepresented=False
    )
    print(f"Section 12 APA Status: {apa.check_validity_status()}")

    # 2. Section 3 Per Diem Limit Update
    new_limit = IncomeTaxActAmendments.section_3_daily_per_diem_limit(2000.0)
    print(f"Section 3 New Daily Tax-Free Per Diem Limit: KES {new_limit:,.2f}")

    # 3. Public Participation Memorandum Generation
    sample_citizen = CitizenProfile(
        full_name="Esther Mutheu Johnson",
        national_id="38291047",
        county_constituency="Nairobi County / Lang'ata Constituency",
        phone_number="+254 712 345 678",
        email_address="esther.mutheu@example.com"
    )
    print("\n--- PUBLIC PARTICIPATION MEMORANDUM SAMPLE ---")
    print(PublicParticipationMemorandum.generate_email_text(sample_citizen))

    # 4. Parliamentary Leadership Summary
    print("\n--- PARLIAMENTARY LEADERSHIP ---")
    print(f"Senate Speaker: {SenateStructure.LEADERSHIP['Speaker'].name}")
    print(f"National Assembly Speaker: {NationalAssemblyStructure.LEADERSHIP['Speaker'].name}")
    print(f"Finance Committee Chair (NA): {NationalAssemblyStructure.COMMITTEES[0].chairperson}")
