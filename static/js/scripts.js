document.addEventListener('DOMContentLoaded', () => {
    const socket = io();

    const chatBox = document.getElementById('chat-box');
    const messageInput = document.getElementById('message-input');
    const sendButton = document.getElementById('send-button');

    sendButton.addEventListener('click', () => {
        const message = messageInput.value;
        if (message) {
            socket.emit('send_message', { room: room, message: message });
            messageInput.value = '';
        }
    });

    socket.on('receive_message', (data) => {
        if (data.room === room) {
            const messageElement = document.createElement('div');
            messageElement.textContent = data.message;
            chatBox.appendChild(messageElement);
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    });
});