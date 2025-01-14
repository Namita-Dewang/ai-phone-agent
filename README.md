# ai-phone-agent

## 🚀 Overview
This project is a full-stack application featuring a **React-based frontend** and a **Python-powered backend**. It is designed to handle **audio processing**, **language processing**, and deliver an engaging user experience. The backend integrates advanced capabilities for tasks like synthesizing audio and handling AI-powered operations.

---

## 🏗️ Project Structure

### Backend
- **Main Application**: `app.py` serves as the entry point for backend services.
- **Key Modules**:
  - `crew_integration.py`: Manages specific integrations.
  - `langchain_agent.py`: Implements language processing and AI-based interactions.
  - `test.py`: Provides backend test cases.
- **Audio Handling**:
  - `synthesized_audio.wav`: Example audio output.
  - `audio_files`: Directory for storing uploaded audio files.
  - `temp_audio`: Temporary storage during processing.
- **Dependencies**: Managed via `requirements.txt`.

### Frontend
- **Core Files**:
  - `package.json` and `package-lock.json`: Manage dependencies and scripts.
- **Directories**:
  - `public`: Static assets and public-facing files.
  - `src`: Contains React components and business logic.
  - `node_modules`: Auto-generated directory with installed Node.js modules.

---

## 🔧 Features
- **Audio Processing**:
  - Process and synthesize audio files.
  - Temporary storage and seamless handling of audio operations.
- **AI-Powered Language Processing**:
  - Powered by modern AI libraries.
  - Supports advanced language models.
- **Full-Stack Architecture**:
  - React frontend for seamless user experience.
  - Python backend with efficient APIs.

---

## 🚀 Getting Started

### Prerequisites
1. **Backend**:
   - Python 3.8 or higher
   - Install dependencies: `pip install -r requirements.txt`
2. **Frontend**:
   - Node.js 16.x or higher

### Setup Instructions

#### Backend
1. Navigate to the `backend` directory:
   ```bash
   cd backend
