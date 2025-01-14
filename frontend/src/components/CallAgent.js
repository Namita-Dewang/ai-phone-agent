import React, { useState, useRef } from 'react';
import styled from 'styled-components';
import AudioRecorder from './AudioRecorder';
import Conversation from './Conversation';
import axios from 'axios';

const Container = styled.div`
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
`;

const AudioPlayer = styled.audio`
  width: 100%;
  margin: 10px 0;
`;

const StatusMessage = styled.p`
  color: ${props => props.error ? 'red' : '#666'};
  text-align: center;
`;

const CallAgent = () => {
  const [messages, setMessages] = useState([]);
  const [isProcessing, setIsProcessing] = useState(false);
  const [error, setError] = useState(null);
  const audioRef = useRef(null);

  const playAudioResponse = async (audioUrl) => {
    try {
      const fullUrl = `http://localhost:5000${audioUrl}`;
      if (audioRef.current) {
        audioRef.current.src = fullUrl;
        await audioRef.current.load();
        await audioRef.current.play();
      }
    } catch (error) {
      console.error('Error playing audio:', error);
      setError('Failed to play audio response');
    }
  };

  const handleRecordingComplete = async (blob) => {
    setIsProcessing(true);
    setError(null);
    
    const formData = new FormData();
    formData.append('audio', blob);

    try {
      const response = await axios.post('http://localhost:5000/transcribe', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      const { transcription, deepseek_response, audio_url } = response.data;

      // Add messages to conversation
      setMessages(prev => [
        ...prev,
        { text: transcription[0], isUser: true },
        { text: deepseek_response, isUser: false }
      ]);

      // Play the audio response
      if (audio_url) {
        await playAudioResponse(audio_url);
      }

    } catch (error) {
      console.error('Error:', error);
      setError('Failed to process recording');
    } finally {
      setIsProcessing(false);
    }
  };

  return (
    <Container>
      <h1>AI Sales Agent</h1>
      <AudioRecorder onRecordingComplete={handleRecordingComplete} />
      {isProcessing && <StatusMessage>Processing your message...</StatusMessage>}
      {error && <StatusMessage error>{error}</StatusMessage>}
      <audio ref={audioRef} style={{ display: 'none' }} />
      <Conversation messages={messages} />
    </Container>
  );
};

export default CallAgent; 