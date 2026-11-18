from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Set font for the name
        self.set_font("Helvetica", "B", 16)
        # Move to the right
        self.cell(0, 10, "James Masika Wabuya", align="R", new_x="LMARGIN", new_y="NEXT")
        
        # Set font for contact details
        self.set_font("Helvetica", "", 11)
        self.cell(0, 6, "wabuyajames@gmail.com", align="R", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 6, "+25479235228", align="R", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 6, "Nairobi, Kenya.", align="R", new_x="LMARGIN", new_y="NEXT")
        
        # Add a line break
        self.ln(15)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

# Create PDF instance
pdf = PDF()
pdf.add_page()

# Set margins
pdf.set_left_margin(25)
pdf.set_right_margin(25)

# Date (Optional, using current date based on system)
import datetime
today = datetime.date.today().strftime("%B %d, %Y")
pdf.set_font("Helvetica", "", 11)
pdf.cell(0, 10, today, new_x="LMARGIN", new_y="NEXT")
pdf.ln(5)

# Salutation
pdf.set_font("Helvetica", "", 11)
pdf.cell(0, 10, "Dear Hiring Manager,", new_x="LMARGIN", new_y="NEXT")
pdf.ln(5)

# Body Text
body_text = (
    "Hi. I’m James Masika Wabuya, a Senior Software Engineer applying for the position of "
    "Software Engineer and Artificial Intelligence Lead at the Center for Global Health and Pandemic Intelligence. "
    "I’ve worked with medical recording systems like OpenMRS and a telemedicine health platform, BetaCare, "
    "which serves over 1.5 million users. I am currently leading the development of a medical billing health portal "
    "for service providers in an insurance company. I possess the technical aptitude and soft skills required "
    "to excel in this role."
)

body_text_2 = (
    "I am passionate about health awareness and discovery expanding in Africa, and I believe the greater goal "
    "with AI is to improve health outcomes across the continent. As a great team player and a confident individual, "
    "I humbly forward my candidacy for this position."
)

# Multi-cell allows text wrapping
pdf.multi_cell(0, 7, body_text)
pdf.ln(5)
pdf.multi_cell(0, 7, body_text_2)
pdf.ln(10)

# Sign-off
pdf.cell(0, 10, "Warm Regards,", new_x="LMARGIN", new_y="NEXT")
pdf.ln(5)

# Signature Name (Bold)
pdf.set_font("Helvetica", "B", 11)
pdf.cell(0, 10, "James Masika", new_x="LMARGIN", new_y="NEXT")

# Save the PDF
pdf.output("James_Masika_Cover_Letter.pdf")

print("PDF generated successfully: James_Masika_Cover_Letter.pdf")
