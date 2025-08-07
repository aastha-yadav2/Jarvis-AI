modules = [
    "AppOpener",
    "pywhatkit",
    "dotenv",
    "bs4",
    "rich",
    "groq",
    "requests",
    "keyboard",
    "pygame",
    "edge_tts"
]

for module in modules:
    try:
        __import__(module)
        print(f"✅ {module} - found")
    except ModuleNotFoundError as e:
        print(f"❌ {module} - NOT found")
