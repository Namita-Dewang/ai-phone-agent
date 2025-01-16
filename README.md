# 🌟 AI Phone Agent

This project is an **AI-powered phone agent** that facilitates interactive conversations using synthesized audio and a web-based user interface. It comprises a backend powered by Python and a frontend built using React.

---

## ✨ Features
- 🎙️ **Audio Interaction**: Record and play audio directly in the browser.
- 🤖 **AI-Powered Responses**: Generate synthesized audio for dynamic conversation.
- 🖥️ **Web Interface**: Interactive React-based UI for seamless user experience.

---

## 📁 Folder Structure
```
ai-phone-agent-main
├── backend
│   ├── app.py                # Backend logic and API endpoints
│   ├── requirements.txt      # Python dependencies
│   └── synthesized_audio.wav # Sample audio output
├── frontend
│   ├── package.json          # Frontend dependencies
│   ├── public
│   │   └── index.html        # HTML template
│   └── src
│       ├── App.js            # Main React component
│       ├── index.js          # Entry point for React
│       └── components        # React components
│           ├── AudioRecorder.js
│           ├── CallAgent.js
│           └── Conversation.js
```

---

## 🛠️ Prerequisites
- **Backend**: Python 3.10+ installed.
- **Frontend**: Node.js (LTS version) installed.

---

## 🚀 Setup and Installation

### Backend
1. Navigate to the `backend` folder:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the backend server:
   ```bash
   python app.py
   ```

### Frontend
1. Navigate to the `frontend` folder:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```

---

## 🧑‍💻 Usage
1. Start the backend and frontend servers.
2. Access the application in your browser at `http://localhost:3000`.
3. Use the web interface to record audio, interact with the AI agent, and view conversation details.

---

## 💻 Technologies Used
- **Backend**: Python (Flask or similar framework assumed)
- **Frontend**: React.js
- **Audio Processing**: Custom Python scripts and web APIs

---

### 📌 Note
Ensure all dependencies are installed and environment variables are correctly configured before running the application.

---

💡 Happy Coding!
