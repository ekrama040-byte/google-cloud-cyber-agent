from google import genai

# Passing the key directly into the client to bypass the Windows system settings
client = genai.Client(api_key="AIzaSyCQ4fQbiG9p_nuR0GCGNhpu7n8q5dGyV7U")

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='Hello Gemini! This is Ekram from Addis Ababa. Are we connected?',
)

print(response.text)
