"""Generate an ATS-friendly CV PDF for Muhammed Fahmi.

Usage:
    python3 scripts/generate_cv.py

Output: Muhammed-Fahmi-CV.pdf at the repo root.

Design rules (ATS-friendly):
- Single column, no tables, no images, no text boxes.
- Standard font family (Helvetica).
- No emojis, icons, or decorative unicode.
- Clear section headings, reverse-chronological experience.
- Selectable, searchable text (generated with ReportLab flowables).
"""

from pathlib import Path

from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)

OUTPUT = Path(__file__).resolve().parent.parent / "Muhammed-Fahmi-CV.pdf"

BASE_FONT = "Helvetica"
BOLD_FONT = "Helvetica-Bold"

styles = getSampleStyleSheet()

name_style = ParagraphStyle(
    "Name",
    parent=styles["Normal"],
    fontName=BOLD_FONT,
    fontSize=20,
    leading=24,
    spaceAfter=2,
    alignment=TA_LEFT,
)
title_style = ParagraphStyle(
    "Title",
    parent=styles["Normal"],
    fontName=BASE_FONT,
    fontSize=11,
    leading=14,
    spaceAfter=2,
    alignment=TA_LEFT,
)
contact_style = ParagraphStyle(
    "Contact",
    parent=styles["Normal"],
    fontName=BASE_FONT,
    fontSize=10,
    leading=13,
    spaceAfter=10,
    alignment=TA_LEFT,
)
section_style = ParagraphStyle(
    "Section",
    parent=styles["Normal"],
    fontName=BOLD_FONT,
    fontSize=12,
    leading=14,
    spaceBefore=10,
    spaceAfter=4,
    textColor="#000000",
)
role_style = ParagraphStyle(
    "Role",
    parent=styles["Normal"],
    fontName=BOLD_FONT,
    fontSize=11,
    leading=14,
    spaceBefore=4,
    spaceAfter=0,
)
meta_style = ParagraphStyle(
    "Meta",
    parent=styles["Normal"],
    fontName=BASE_FONT,
    fontSize=10,
    leading=13,
    spaceAfter=3,
)
sub_style = ParagraphStyle(
    "Sub",
    parent=styles["Normal"],
    fontName=BOLD_FONT,
    fontSize=10,
    leading=13,
    spaceBefore=4,
    spaceAfter=2,
)
body_style = ParagraphStyle(
    "Body",
    parent=styles["Normal"],
    fontName=BASE_FONT,
    fontSize=10,
    leading=13,
    spaceAfter=4,
)
bullet_style = ParagraphStyle(
    "Bullet",
    parent=styles["Normal"],
    fontName=BASE_FONT,
    fontSize=10,
    leading=13,
    leftIndent=14,
    firstLineIndent=-14,
    spaceAfter=2,
)
bullet_group_trailer = ParagraphStyle(
    "BulletTrailer",
    parent=styles["Normal"],
    fontName=BASE_FONT,
    fontSize=2,
    leading=4,
    spaceAfter=4,
)


def section(title):
    return Paragraph(title.upper(), section_style)


def bullets(items):
    flowables = [Paragraph("- " + text, bullet_style) for text in items]
    flowables.append(Spacer(1, 4))
    return flowables


def build_story():
    story = []

    # Header
    story.append(Paragraph("Muhammed Fahmi", name_style))
    story.append(Paragraph("Senior Application Operations Engineer", title_style))
    story.append(
        Paragraph(
            "Date of Birth: 14 April 1991 | "
            "Cairo, Egypt (currently on-site in KSA)",
            contact_style,
        )
    )
    story.append(
        Paragraph(
            "LinkedIn: linkedin.com/in/muhammedfahmi | "
            "GitHub: github.com/MuhammedF91",
            contact_style,
        )
    )

    # Summary
    story.append(section("Professional Summary"))
    story.append(
        Paragraph(
            "Senior Application Operations Engineer with 4+ years of hands-on experience "
            "supporting enterprise telecom BSS and digital applications. Skilled in Linux "
            "operations, Bash and PowerShell scripting, Oracle SQL, and on-call incident "
            "response. Proven track record running monthly billing cycles, leading L1 teams, "
            "performing root cause analysis, and executing disaster recovery drills on Nokia "
            "BSS platforms. Self-taught DevOps practitioner with a home lab covering Docker, "
            "CI/CD with GitHub Actions, Nginx, and WireGuard VPN.",
            body_style,
        )
    )

    # Technical Skills
    story.append(section("Technical Skills"))
    skills = [
        "<b>Operating Systems:</b> Linux (Red Hat, Ubuntu, Raspberry Pi OS), Windows Server, macOS",
        "<b>Databases:</b> Oracle SQL, Microsoft SQL Server, Oracle XE",
        "<b>Scripting:</b> Bash, PowerShell, Python",
        "<b>Application Platforms:</b> Nokia SurePay, Nokia FlowOne, Nokia Data Refinery, "
        "FOM (Fiber Order Management), CRM, Billing, UPC (Charging System)",
        "<b>Containerization and CI/CD:</b> Docker, Docker Compose, GitHub Actions",
        "<b>Web and Networking:</b> Nginx, WireGuard VPN, Cloudflare DDNS, DNS, DHCP, "
        "IP Addressing, Port Forwarding, Firewall Rules",
        "<b>Reporting and Analytics:</b> Power BI, Excel, Oracle SQL",
        "<b>Version Control:</b> Git, GitHub",
        "<b>DevOps Practices:</b> Log analysis, deployment automation, monitoring, "
        "incident response, root cause analysis",
    ]
    story.extend(bullets(skills))

    # Experience
    story.append(section("Professional Experience"))

    story.append(Paragraph("Senior Application Operations Engineer, Giza Arabia", role_style))
    story.append(Paragraph("April 2026 – Present | On-site, KSA (STC)", meta_style))
    story.extend(
        bullets(
            [
                "Operate and troubleshoot CRM and Billing systems on STC's FOM "
                "(Fiber Order Management) platform.",
                "Work directly on Linux servers via terminal for day-to-day operations "
                "and log analysis.",
                "Write Bash scripts to automate routine operational tasks and monitoring.",
                "Query and investigate application data using Oracle SQL.",
                "Participate in the on-call rotation to handle production incidents "
                "outside business hours.",
            ]
        )
    )

    story.append(Paragraph("Senior Application Support Specialist, SIGMA-EMEA", role_style))
    story.append(Paragraph("September 2021 – March 2026 | Cairo, Egypt", meta_style))
    story.append(Paragraph("STC Specialized Project (KSA) — BSS", sub_style))
    story.extend(
        bullets(
            [
                "Supported Nokia BSS applications (SurePay, FlowOne, Data Refinery).",
                "Ran the monthly billing cycle and acted as the technical SPOC.",
                "Wrote Bash scripts for automation and monitoring.",
                "Led the L1 team and performed Root Cause Analysis (RCA) on failed requests.",
                "Applied application deployments and releases delivered by vendors.",
                "Ran disaster recovery testing and production readiness checks.",
                "Configured promotions and services on UPC (Charging System frontend).",
                "Generated financial reports using Oracle SQL.",
                "Contributed to integration testing, data analysis, and system configuration.",
            ]
        )
    )
    story.append(Paragraph("Redbull Mobile Project (KSA) — Digital Mobile/Web App", sub_style))
    story.extend(
        bullets(
            [
                "Handled tickets and technical requests from end users.",
                "Troubleshot application and database issues using Microsoft SQL Server.",
                "Wrote PowerShell scripts to automate routine tasks and generate reports.",
                "Produced business and operational reports with Power BI and Excel.",
                "Collaborated with business stakeholders to deploy new mobile app features and plans.",
                "Monitored logs and system health via scripting and SQL.",
                "Coordinated with the BSS team (Huawei) to keep data consistent across systems.",
            ]
        )
    )

    story.append(Paragraph("Retail Sales Executive, Orange Egypt", role_style))
    story.append(Paragraph("2019 | Cairo, Egypt", meta_style))
    story.extend(
        bullets(
            [
                "Advised customers on mobile products and consistently exceeded sales targets.",
            ]
        )
    )

    story.append(Paragraph("Retention Executive, beIN Media Group", role_style))
    story.append(Paragraph("2017 – 2018 | Cairo, Egypt", meta_style))
    story.extend(
        bullets(
            [
                "Maintained customer relationships across the GCC region through targeted campaigns.",
                "Resolved customer issues and retained over 100% of the targeted subscriber base.",
            ]
        )
    )

    story.append(Paragraph("Telesales and Tech Support, Raya (Etisalat UAE Project)", role_style))
    story.append(Paragraph("2008 – 2017 | Cairo, Egypt", meta_style))
    story.extend(
        bullets(
            [
                "Sold services via outbound calls and resolved customer technical issues.",
            ]
        )
    )

    # DevOps Projects
    story.append(section("DevOps Projects (Home Lab)"))

    story.append(Paragraph("Home Network Monitor", role_style))
    story.append(
        Paragraph(
            "Tools: Docker, Docker Compose, Python, Flask, Oracle XE, "
            "GitHub Actions, Raspberry Pi.",
            meta_style,
        )
    )
    story.extend(
        bullets(
            [
                "Built a monitoring system with a CI/CD pipeline using GitHub Actions "
                "(build, test, publish images).",
                "Used Mac Mini as the development environment and Raspberry Pi as "
                "the production target.",
                "Enabled secure remote access via Cloudflare DDNS and WireGuard.",
            ]
        )
    )

    story.append(Paragraph("Personal Website", role_style))
    story.append(
        Paragraph(
            "Tools: HTML, CSS, JavaScript, Python, Flask, Oracle XE, Nginx, "
            "Docker Compose, GitHub Actions.",
            meta_style,
        )
    )
    story.extend(
        bullets(
            [
                "Deployed a static frontend with a Flask API and a Dockerized Oracle XE database.",
                "Configured Nginx as a reverse proxy and orchestrated the stack with Docker Compose.",
                "Ran CI with GitHub Actions; tested on Mac Mini, deployed to Raspberry Pi.",
            ]
        )
    )

    story.append(Paragraph("Remote Access with WireGuard VPN", role_style))
    story.append(
        Paragraph(
            "Tools: WireGuard, PiVPN, Cloudflare DDNS, TP-Link Omada ER605.",
            meta_style,
        )
    )
    story.extend(
        bullets(
            [
                "Set up secure remote access to a home network using a Raspberry Pi "
                "as the VPN gateway.",
                "Diagnosed and fixed handshake failures caused by NAT and port forwarding "
                "misconfiguration.",
                "Resolved VPN routing issues with correct AllowedIPs settings and "
                "IP forwarding on the gateway.",
                "Automated DDNS updates using a Cloudflare API script.",
            ]
        )
    )

    story.append(Paragraph("DevOps Learning Lab", role_style))
    story.append(
        Paragraph(
            "Tools: Docker Compose, Oracle DB, Bash scripting.",
            meta_style,
        )
    )
    story.extend(
        bullets(
            [
                "Simulated a DevOps environment with multiple microservices in Docker Compose.",
                "Maintained separate test (Mac Mini) and production (Raspberry Pi) environments.",
            ]
        )
    )

    return story


def main():
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=LETTER,
        leftMargin=0.7 * inch,
        rightMargin=0.7 * inch,
        topMargin=0.6 * inch,
        bottomMargin=0.6 * inch,
        title="Muhammed Fahmi - CV",
        author="Muhammed Fahmi",
        subject="Curriculum Vitae",
        creator="reportlab",
    )
    doc.build(build_story())
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
