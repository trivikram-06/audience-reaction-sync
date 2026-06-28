from datetime import datetime
import os

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

from modules.analytics import SessionAnalytics

# ------------------------------------
# Load Analytics
# ------------------------------------

analytics = SessionAnalytics()

# ------------------------------------
# Create Reports Folder
# ------------------------------------

os.makedirs("reports", exist_ok=True)

filename = (
    f"reports/Audience_Report_"
    f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
)

# ------------------------------------
# PDF
# ------------------------------------

doc = SimpleDocTemplate(filename)

styles = getSampleStyleSheet()

story = []

story.append(
    Paragraph(
        "<b><font size=20>"
        "Audience Reaction Report"
        "</font></b>",
        styles["Title"]
    )
)

story.append(Spacer(1, 20))

story.append(
    Paragraph(
        f"<b>Generated:</b> {datetime.now()}",
        styles["Normal"]
    )
)

story.append(Spacer(1, 12))

items = [

    ("Session File", analytics.session_file()),

    ("Session Duration", analytics.session_duration()),

    ("People Detected", analytics.people_count()),

    ("Average Attention",
     f"{analytics.average_attention()} %"),

    ("Average Engagement",
     f"{analytics.average_engagement()} %"),

    ("Highest Engagement",
     f"{analytics.highest_engagement()} %"),

    ("Lowest Engagement",
     f"{analytics.lowest_engagement()} %"),

    ("Average Blink Count",
     analytics.average_blinks()),

    ("Most Attentive Person",
     f"ID {analytics.most_attentive_person()}"),

    ("Least Attentive Person",
     f"ID {analytics.least_attentive_person()}")

]

for title, value in items:

    story.append(
        Paragraph(
            f"<b>{title}</b>: {value}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 8))

story.append(Spacer(1, 20))

story.append(
    Paragraph(
        "<b>Generated Automatically by "
        "Audience Reaction Sync</b>",
        styles["Italic"]
    )
)

doc.build(story)

print("=" * 50)
print("PDF Report Generated Successfully!")
print(filename)
print("=" * 50)