import React from 'react';
import { useReactMediaRecorder } from 'react-media-recorder';
import styled from 'styled-components';

const RecorderContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
`;

const Button = styled.button`
  padding: 10px 20px;
  border-radius: 5px;
  border: none;
  background-color: ${props => props.isRecording ? '#ff4444' : '#4CAF50'};
  color: white;
  cursor: pointer;
`;

const AudioRecorder = ({ onRecordingComplete }) => {
  const {
    status,
    startRecording,
    stopRecording,
    mediaBlobUrl
  } = useReactMediaRecorder({
    audio: true,
    onStop: (blobUrl, blob) => {
      onRecordingComplete(blob);
    }
  });

  const isRecording = status === "recording";

  return (
    <RecorderContainer>
      <Button
        onClick={isRecording ? stopRecording : startRecording}
        isRecording={isRecording}
      >
        {isRecording ? 'Stop Recording' : 'Start Recording'}
      </Button>
      {mediaBlobUrl && (
        <audio src={mediaBlobUrl} controls />
      )}
    </RecorderContainer>
  );
};

export default AudioRecorder; 