"""Generate professional PDF CV for Aizaz Ali Shah from portfolio content."""
from pathlib import Path
from fpdf import FPDF

ROOT = Path(r"c:\xampp\htdocs\my-portfolio")
ASSETS = ROOT / "assets"
OUT = ASSETS / "Aizaz-Ali-Shah-CV.pdf"
PHOTO = ASSETS / "photo.jpg"

# Colors matching portfolio
INK = (14, 26, 31)
TEAL = (15, 107, 92)
TEAL_DEEP = (10, 74, 64)
MUTED = (90, 107, 114)
AMBER = (196, 106, 27)
LINE = (210, 218, 214)
WHITE = (255, 255, 255)
MIST = (238, 243, 241)

FONT_REG = r"C:\Windows\Fonts\calibri.ttf"
FONT_BOLD = r"C:\Windows\Fonts\calibrib.ttf"
FONT_ITALIC = r"C:\Windows\Fonts\calibrii.ttf"


class CV(FPDF):
    def __init__(self):
        super().__init__(format="A4", unit="mm")
        self.set_auto_page_break(auto=True, margin=14)
        self.add_font("Body", "", FONT_REG)
        self.add_font("Body", "B", FONT_BOLD)
        self.add_font("Body", "I", FONT_ITALIC)
        self.set_margins(14, 12, 14)

    def footer(self):
        self.set_y(-10)
        self.set_font("Body", "", 8)
        self.set_text_color(*MUTED)
        self.cell(0, 5, f"Aizaz Ali Shah  ·  Page {self.page_no()}/{{nb}}", align="C")

    def section_title(self, title: str):
        self.ln(3)
        self.set_font("Body", "B", 11)
        self.set_text_color(*TEAL)
        self.cell(0, 6, title.upper(), new_x="LMARGIN", new_y="NEXT")
        y = self.get_y()
        self.set_draw_color(*TEAL)
        self.set_line_width(0.5)
        self.line(14, y, 196, y)
        self.ln(3)
        self.set_text_color(*INK)

    def body_text(self, text: str, size=9.5, leading=4.6):
        self.set_font("Body", "", size)
        self.set_text_color(*INK)
        self.multi_cell(0, leading, text)

    def muted(self, text: str, size=9):
        self.set_font("Body", "", size)
        self.set_text_color(*MUTED)
        self.multi_cell(0, 4.2, text)
        self.set_text_color(*INK)

    def job(self, title: str, org: str, dates: str, bullets: list[str]):
        self.set_x(self.l_margin)
        self.set_font("Body", "B", 10)
        self.set_text_color(*INK)
        title_w = self.w - self.l_margin - self.r_margin - 42
        self.cell(title_w, 5, title)
        self.set_font("Body", "", 9)
        self.set_text_color(*MUTED)
        self.cell(42, 5, dates, align="R", new_x="LMARGIN", new_y="NEXT")
        self.set_x(self.l_margin)
        self.set_font("Body", "I", 9)
        self.set_text_color(*TEAL)
        self.multi_cell(0, 4.5, org)
        self.set_text_color(*INK)
        self.set_font("Body", "", 9)
        for b in bullets:
            self.set_x(self.l_margin + 2)
            self.multi_cell(self.w - self.l_margin - self.r_margin - 2, 4.2, f"•  {b}")
        self.ln(1.5)

    def project(self, name: str, meta: str, desc: str, tech: str, link: str | None = None):
        self.set_x(self.l_margin)
        self.set_font("Body", "B", 10)
        self.set_text_color(*INK)
        self.multi_cell(0, 5, name)
        self.set_x(self.l_margin)
        self.set_font("Body", "", 8.5)
        self.set_text_color(*AMBER)
        self.multi_cell(0, 4, meta)
        self.set_x(self.l_margin)
        self.set_font("Body", "", 9)
        self.set_text_color(*INK)
        self.multi_cell(0, 4.2, desc)
        self.set_x(self.l_margin)
        self.set_font("Body", "I", 8.5)
        self.set_text_color(*MUTED)
        self.multi_cell(0, 4, f"Tech: {tech}")
        if link:
            self.set_x(self.l_margin)
            self.multi_cell(0, 4, link)
        self.ln(1.8)
        self.set_text_color(*INK)


def build():
    pdf = CV()
    pdf.alias_nb_pages()
    pdf.add_page()

    # ---- Header band ----
    pdf.set_fill_color(*INK)
    pdf.rect(0, 0, 210, 42, "F")
    pdf.set_fill_color(*TEAL)
    pdf.rect(0, 42, 210, 2.2, "F")

    # Photo
    if PHOTO.exists():
        pdf.image(str(PHOTO), x=14, y=7, w=28, h=28)

    left = 48 if PHOTO.exists() else 14
    pdf.set_xy(left, 9)
    pdf.set_font("Body", "B", 22)
    pdf.set_text_color(*WHITE)
    pdf.cell(0, 9, "Aizaz Ali Shah", new_x="LMARGIN", new_y="NEXT")
    pdf.set_x(left)
    pdf.set_font("Body", "", 11)
    pdf.set_text_color(180, 220, 210)
    pdf.cell(0, 6, "Android & Web Developer", new_x="LMARGIN", new_y="NEXT")
    pdf.set_x(left)
    pdf.set_font("Body", "", 8.5)
    pdf.set_text_color(200, 210, 208)
    contact = (
        "Rawalpindi, Pakistan  ·  +92 314 9461171  ·  aizaz319@gmail.com\n"
        "LinkedIn: linkedin.com/in/aizaz-shah-8603211a3  ·  Portfolio project: apnashadihall.com"
    )
    pdf.set_xy(left, 26)
    pdf.multi_cell(145, 4, contact)

    pdf.set_y(48)

    # ---- Summary ----
    pdf.section_title("Professional Summary")
    pdf.body_text(
        "Dedicated Android and web developer focused on fast, scalable, and user-friendly products. "
        "Delivered Android, Flutter, WordPress, and full-stack web projects for clients, with two personal "
        "Android apps live on the Google Play Store. Helps clients turn ideas into reliable digital solutions — "
        "mobile apps, responsive websites, or complete backend systems — using modern AI tools such as Cursor "
        "and Claude to move faster without sacrificing architecture or code quality."
    )

    # ---- Experience ----
    pdf.section_title("Work Experience")
    pdf.job(
        "Senior Android & WordPress Developer",
        "Niyel Technologies Ltd.  ·  Nicosia, Cyprus",
        "Apr 2022 – Feb 2024",
        [
            "Delivered Android (Java), Flutter, and WordPress solutions for client products.",
            "Built production apps including Bluetooth-connected barcode/label printing workflows.",
            "Developed and customized WordPress sites such as KIBSO (kibso.org).",
        ],
    )
    pdf.job(
        "Front-End Web Developer",
        "MBL High-Tech  ·  Kyrenia, Cyprus",
        "Aug 2020 – Dec 2021",
        [
            "Created and managed responsive front-ends for client websites.",
            "Handled testing, debugging, and ongoing UI improvements.",
        ],
    )
    pdf.job(
        "Android App Developer Intern",
        "Gigabyte Ltd.  ·  Nicosia, Cyprus",
        "Jun 2019 – Aug 2019",
        [
            "Designed a stock management application in Android Studio with SQLite.",
        ],
    )

    # ---- Projects ----
    pdf.section_title("Selected Projects")
    pdf.project(
        "ApnaShadiHall — Marriage Hall Booking Platform (Flagship)",
        "Full-stack · Live",
        "Designed and developed a full-stack platform for discovering, comparing, and booking marriage halls "
        "with role-based dashboards for customers, hall owners, and administrators. Features include real-time "
        "slot availability, owner calendar blocks, booking holds with timed payment windows, SafePay payments "
        "(webhooks & reconciliation), dynamic quoting (seasonal pricing, packages, catering, discounts), "
        "Cloudinary images, and Brevo transactional email.",
        "Laravel 10, PHP, MySQL, Blade, Tailwind CSS, Alpine.js, Vite, SafePay",
        "https://www.apnashadihall.com/",
    )
    pdf.project(
        "Quietify",
        "Android · Google Play Store",
        "Location-based Do Not Disturb automation. Users mark quiet zones on an interactive map; the app "
        "enables silent mode on entry and restores normal mode on exit, with foreground service and real-time "
        "location tracking (OSMDroid, FusedLocationProvider).",
        "Java, Android SDK, OSMDroid, Google Play Services, Foreground Service",
        "play.google.com/store/apps/details?id=com.gghushtipedia.quietify",
    )
    pdf.project(
        "Chhach Deals",
        "Android · Google Play Store",
        "Marketplace app for buying and selling mobile devices — ad posting, buyer–seller connection, "
        "authentication, and messaging.",
        "Android, Java, Auth, Messaging",
        "play.google.com/store/apps/details?id=com.chhachdeals.gghushtipedia",
    )

    # May need page 2
    if pdf.get_y() > 240:
        pdf.add_page()

    pdf.project(
        "Label Printer",
        "Android · Client (Niyel Technologies)",
        "Production Android app for barcode scanning and thermal label printing over Bluetooth, synced with a "
        "remote server database and SQLite offline cache.",
        "Java, Bluetooth SDK, REST APIs, SQLite",
    )
    pdf.project(
        "KIBSO",
        "WordPress · Live",
        "Custom WordPress website for Kıbrıs Türk Sanayi Odası (TRNC), communicating the organization's "
        "mission, services, and offerings.",
        "WordPress, Custom theme",
        "https://www.kibso.org/",
    )
    pdf.project(
        "ADF Cyprus",
        "Web · Archived (site no longer live)",
        "Furniture store website built from scratch with product search, store information, and PDF catalogue viewing.",
        "HTML, CSS, JavaScript, PHP, MySQL",
    )

    # ---- Skills ----
    pdf.section_title("Skills")
    skills = [
        ("Mobile", "Native Android (Java/Kotlin), Flutter, Jetpack Compose, Firebase, Retrofit, Room, Material Design, Play Store deployment"),
        ("Web & Backend", "Laravel, PHP, MySQL, HTML5, CSS3, JavaScript, Bootstrap, Blade, Tailwind, Alpine.js, REST APIs"),
        ("WordPress", "Custom themes & plugins, Elementor, custom post types, hooks/filters, responsive themes"),
        ("AI Tools", "Strong working knowledge of Cursor and Claude for accelerated development, debugging, and delivery"),
        ("Other", "Git/GitHub, JUnit/Espresso, third-party SDK integration, UI/UX and responsive design"),
    ]
    for label, text in skills:
        self_width = pdf.w - pdf.l_margin - pdf.r_margin
        pdf.set_x(pdf.l_margin)
        pdf.set_font("Body", "B", 9)
        pdf.set_text_color(*TEAL_DEEP)
        pdf.cell(32, 4.5, label)
        pdf.set_font("Body", "", 9)
        pdf.set_text_color(*INK)
        pdf.multi_cell(self_width - 32, 4.5, text)
        pdf.ln(0.6)

    # ---- Education ----
    pdf.section_title("Education")
    pdf.set_font("Body", "B", 10)
    pdf.cell(0, 5, "Master in Computer Engineering", new_x="LMARGIN", new_y="NEXT")
    pdf.muted("Cyprus International University  ·  Nicosia, Cyprus  ·  Sep 2020 – Jul 2022")
    pdf.ln(1)
    pdf.set_font("Body", "B", 10)
    pdf.set_text_color(*INK)
    pdf.cell(0, 5, "B.S. in Computer Engineering", new_x="LMARGIN", new_y="NEXT")
    pdf.muted("Cyprus International University  ·  Nicosia, Cyprus  ·  Sep 2016 – Jul 2020")

    # ---- Languages ----
    pdf.section_title("Languages")
    pdf.body_text("Urdu (Native)  ·  English (Proficient)  ·  Turkish (Basic)", size=9.5, leading=5)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(OUT))
    print(f"Created: {OUT}")


if __name__ == "__main__":
    build()
