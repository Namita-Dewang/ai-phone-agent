from flask import Flask, request, jsonify, render_template, send_file
from flask_cors import CORS
import os
from dotenv import load_dotenv
import logging
from smallest import Smallest
import time
import torch
from faster_whisper import WhisperModel
# Import the process_customer_message function from CrewAgent
from latest_ai_development.main import process_customer_message

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'audio_files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize clients
smallest_api_key = os.getenv("SMALLEST_API_KEY")
smallest_client = Smallest(api_key=smallest_api_key)

# Initialize Whisper model
whisper_model = WhisperModel("small", device="cuda" if torch.cuda.is_available() else "cpu")
logger.info(f"Whisper model loaded on: {'cuda' if torch.cuda.is_available() else 'cpu'}")

def transcribe_audio(audio_file):
    """Transcribe audio using Faster Whisper"""
    try:
        # Save temporary file
        temp_path = os.path.join(UPLOAD_FOLDER, "temp_audio.wav")
        audio_file.save(temp_path)
        
        # Transcribe with Faster Whisper
        segments, info = whisper_model.transcribe(temp_path)
        transcription = " ".join([segment.text for segment in segments])
        
        # Clean up temp file
        os.remove(temp_path)
        
        return {
            "success": True,
            "transcription": [transcription]
        }
    except Exception as e:
        logger.error(f"Transcription error: {e}")
        return {
            "success": False,
            "error": str(e)
        }

def process_with_crew(transcription):
    """Process transcription with CrewAgent's main.py and get response"""
    try:
        # Join the transcription segments into a single string
        transcription_text = " ".join(transcription)
        
        # Use CrewAgent's main.py to process the message
        response = process_customer_message(transcription_text)
        return response
    except Exception as e:
        logger.error(f"CrewAgent error: {e}")
        return "Error processing your request"

@app.route('/transcribe', methods=['POST'])
def transcribe():
    try:
        if 'audio' not in request.files:
            return jsonify({"error": "No audio file provided"}), 400
            
        audio_file = request.files['audio']
        
        # Get transcription from Whisper
        result = transcribe_audio(audio_file)
        
        if result["success"]:
            # Process with CrewAgent through main.py
            crew_response = process_with_crew(result["transcription"])
            
            # Generate audio response using Smallest
            filename = f"response_{int(time.time())}.wav"
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            # Synthesize audio and save it
            smallest_client.synthesize(crew_response, save_as=file_path)
            
            return jsonify({
                "success": True,
                "transcription": result["transcription"],
                "crew_response": crew_response,
                "audio_url": f"/audio/{filename}"
            })
        else:
            return jsonify({"error": result["error"]}), 500

    except Exception as e:
        logger.error(f"Request error: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'audio' not in request.files:
            return "No audio file uploaded", 400
        audio_file = request.files['audio']
        result = transcribe_audio(audio_file)
        return render_template('result.html', result=result)

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "whisper_device": "cuda" if torch.cuda.is_available() else "cpu"
    })

@app.route('/audio/<filename>')
def serve_audio(filename):
    try:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if not os.path.exists(file_path):
            logger.error(f"Audio file not found: {file_path}")
            return jsonify({"error": "Audio file not found"}), 404
        
        return send_file(
            file_path,
            mimetype='audio/wav',
            as_attachment=False
        )
    except Exception as e:
        logger.error(f"Error serving audio: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)