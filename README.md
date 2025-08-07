# 🤖 Jarvis – AI Desktop Voice Assistant

Jarvis is an AI-powered voice assistant designed for desktops, capable of executing voice commands to launch apps, perform web searches, control the system, and even generate AI-based content. The assistant features a modern PyQt5 GUI with animated visuals, voice feedback, and seamless AI integration using the Groq API.

---

## 🎯 Features

- 🎙️ Real-time voice recognition and response
- 💻 Open and close desktop applications via voice
- 🔍 Voice-based Google and YouTube searches
- ✍️ AI-generated content using the Groq API
- 🪟 Custom PyQt5 GUI with frameless design and animation
- ⚙️ System control functions (shutdown, restart, etc.)
- 🔄 Multithreading for smooth GUI–backend communication

---

## 🧠 Tech Stack

| Technology        | Purpose                             |
|-------------------|-------------------------------------|
| Python            | Core programming language           |
| PyQt5             | GUI design and integration          |
| SpeechRecognition | Voice input processing              |
| gTTS / pyttsx3    | Text-to-speech voice output         |
| Groq API          | AI text generation                  |
| Subprocess        | App and system control              |
| Multithreading    | GUI performance and non-blocking UX |

---

## 🎥 Demo Video

📺 [Watch the Demo on YouTube](https://youtu.be/your-video-link)

> 👁️ Experience Jarvis handling real-time voice commands, launching apps, generating AI content, and interacting smoothly with the user!

---

## 🖼️ Screenshots

> *(Optional – add images in the `/assets` folder and update the links below)*

| GUI Interface | Voice Command in Action |
|---------------|--------------------------|
| ![GUI](assets/gui_view.png) | ![Command](assets/command_demo.png) |

---

## 🚀 Getting Started

### 🔧 Installation

Install required Python packages:


pip install pyqt5 speechrecognition gtts pyttsx3 groq openai




 **✅ Make sure your microphone is working and Python is installed (preferably 3.8+).**


## ▶️ Run the Assistant
python jarvis_main.py


## 📁 Project Structure


Jarvis-AI-Desktop/
├── jarvis_main.py # Main script to run the application
├── gui/
│ └── main_window.ui # PyQt5 GUI layout file
├── assets/
│ ├── animation.gif # Animated assistant graphic
│ └── icon.png # App icon
├── utils/
│ ├── voice_handler.py # Handles voice input/output
│ └── ai_generator.py # Integrates AI content generation via Groq API
├── README.md # Project overview and documentation
└── requirements.txt # List of Python dependencies


## 🛡️ Security & Privacy  
✅ **Voice commands are processed locally**  
🚫 **No audio is stored or transmitted externally**  
🧠 **AI queries are securely handled via Groq API**

---

## 🧩 Possible Future Features  
- ✉️ **Email sending via voice**  
- 🌦️ **Weather updates using OpenWeather API**  
- 🗓️ **Calendar reminders with voice alerts**  
- 🌍 **Multi-language support**  
- 🧠 **Personalized command history & memory**



## 🤝 Contribution

Pull requests are welcome!  
If you'd like to contribute, please **fork the repo** and submit a **Pull Request**.

For major changes, it's recommended to **open an issue first** to discuss what you'd like to change.

Let's collaborate to make this project even better! 🚀


## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](./LICENSE) file for details.




## 🙋‍♀️ About the Creator  
### **Aastha Yadav**  
🎓 **B.Tech in Data Science & Machine Learning**  
💼 **Aspiring Data Scientist | Python Developer | AI Enthusiast**  
📫 **Connect with me on:**  
🔗 [LinkedIn](https://www.linkedin.com/in/aastha-yadav-89b41a332)  
💻 [GitHub](https://github.com/aastha-yadav2)


⭐ If you like this project, give it a star on GitHub and share your feedback!



