# import wikipedia  # package

# pip : It's a Command used to install the Modules and Packages
# Python install Package

# Set language to English (optional)
# wikipedia.set_lang("en")

# searchContent = wikipedia.search("JSS college")

# print(searchContent)

# # Search for a topic
# results = wikipedia.search("Royal Challengers Bengaluru")
# print("Search Results:\n", results)

# # Get summary of a topic
# summary = wikipedia.summary("Royal Challengers Bengaluru", sentences=2)
# print("\nSummary:\n", summary)

# # Get full page content
# page = wikipedia.page("Royal Challengers Bengaluru")
# print("\nTitle:", page.title)
# print("\nURL:", page.url)
# print("\nContent (First 500 chars):", page.content[:500])


# import pyjokes

# joke = pyjokes.get_joke()

# print(joke)


# pip install qrcode[pil]
# import qrcode
# img = qrcode.make("https://www.Google.com")
# img.save("Google.png")


# from reportlab.lib.pagesizes import LETTER
# from reportlab.pdfgen import canvas

# # Create a new PDF file
# file_path = "sample2_output.pdf"
# c = canvas.Canvas(file_path, pagesize=LETTER)

# # Add text to the PDF
# c.drawString(100, 750, "Thank You")

# # Add another line
# c.drawString(100, 730, "Created using the reportlab library.")

# # Save the PDF
# c.save()
