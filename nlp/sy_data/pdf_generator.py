from faker import Faker
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import random

fake = Faker()

def generate_cv_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # fake personal information
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height -50, fake.name())
    c.setFont("Helvetica", 12)
    c.drawString(50, height -80, f"Email: {fake.email()}")
    c.drawString(50, height -100, f"Phone: {fake.phone_number()}")
    c.drawString(50, height -120, f"Address: {fake.address()}")

    # professional summary
    c.drawString(50, height -160, "Summary:")
    c.drawString(70, height -180, fake.paragraph(nb_sentences=2))

    # work experience
    c.drawString(50, height - 200, "Work Experience:")
    y = height - 240

    for _ in range(random.randint(1,5)):
        c.drawString(70, y, f"{fake.job()} at {fake.company()} ({fake.date()} - {fake.date()})")
        y -= 20
        c.drawString(90, y, fake.paragraph(nb_sentences=2))
        y -= 40

    # education
    c.drawString(50, y, "Education:")
    y -= 20
    for _ in range(random.randint(1, 3)):
        c.drawString(70, y, f"{fake.job()} Degree from {random.choice(['Harvard', 'Stanford', 'MIT'])} ({fake.date()} - {fake.date()})")
        y -= 20

    # skills
    c.drawString(50, y, "Skills")
    y -= 20

    skills = ["Python", "Data Analysis", "Machine Learning", "Project Management", "Team Leadership"]
    c.drawString(70, y, ", ".join(random.sample(skills, k=random.randint(2, len(skills)))))

    c.save()
    
for i in range(10):
    filename = f"CV_{i+1}.pdf"
    generate_cv_pdf(filename)
    print(f"Generated PDF: {filename}")

