import fpdf

# Create a document:
document = fpdf.FPDF()

# Define the font and color for a title, and add the first page:
document.set_font('Times', 'B', 14)
document.set_text_color(19, 83, 173)
document.add_page()

# Write the title of the document:
document.cell(0, 5, 'PDF test document')
document.ln()

#Write a long paragraph:
document.set_font('Times', '', 12)
document.set_text_color(0)
document.multi_cell(0,5, "This is an example of a long paragraph."*10)
document.ln()

#Write another long paragraph:
document.multi_cell(0,10, "Another long paragraph. Lorem imsum dolor sit amet, consectetur adipiscing elit."*20)

document.output('simple_pdf.pdf')
