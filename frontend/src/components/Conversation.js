import React from 'react';
import styled from 'styled-components';

const ConversationContainer = styled.div`
  margin: 20px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
`;

const Message = styled.div`
  margin: 10px 0;
  padding: 10px;
  border-radius: 5px;
  background-color: ${props => props.isUser ? '#e3f2fd' : '#f5f5f5'};
`;

const Conversation = ({ messages }) => {
  return (
    <ConversationContainer>
      {messages.map((message, index) => (
        <Message key={index} isUser={message.isUser}>
          <strong>{message.isUser ? 'You' : 'AI Agent'}:</strong> {message.text}
        </Message>
      ))}
    </ConversationContainer>
  );
};

export default Conversation; 