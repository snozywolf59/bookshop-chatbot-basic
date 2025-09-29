<script setup lang="ts">
import { ref } from "vue";

const text = ref("");
const emit = defineEmits(["send"]);

const sendMessage = () => {
    if (text.value.trim() !== "") {
        emit("send", text.value);
        text.value = "";
    }
};
</script>

<template>
    <div class="chat-input-container">
        <div class="chat-input">
            <input v-model="text" @keyup.enter="sendMessage" placeholder="Nhập tin nhắn của bạn..."
                class="message-input" />
            <button @click="sendMessage" class="send-button" :disabled="!text.trim()">
                <span class="send-icon">📤</span>
                <span class="send-text">Gửi</span>
            </button>
        </div>
    </div>
</template>

<style scoped>
.chat-input-container {
    padding: 16px;
    background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
    border-radius: 16px;
    box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.05);
}

.chat-input {
    display: flex;
    gap: 12px;
    align-items: center;
    background: white;
    padding: 8px;
    border-radius: 16px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    transition: all 0.3s ease;
}

.chat-input:focus-within {
    box-shadow: 0 4px 16px rgba(67, 160, 71, 0.2);
    transform: translateY(-2px);
}

.message-input {
    flex: 1;
    padding: 12px 16px;
    border: 2px solid transparent;
    border-radius: 12px;
    font-size: 15px;
    color: #2e7d32;
    background: #f9fdf9;
    transition: all 0.3s ease;
    outline: none;
}

.message-input::placeholder {
    color: #9e9e9e;
}

.message-input:focus {
    background: white;
    border-color: #66bb6a;
    box-shadow: 0 0 0 3px rgba(102, 187, 106, 0.1);
}

.send-button {
    padding: 12px 24px;
    background: linear-gradient(135deg, #43a047 0%, #66bb6a 100%);
    color: white;
    border: none;
    border-radius: 12px;
    cursor: pointer;
    font-size: 15px;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: all 0.3s ease;
    box-shadow: 0 3px 8px rgba(67, 160, 71, 0.3);
    white-space: nowrap;
}

.send-button:hover:not(:disabled) {
    background: linear-gradient(135deg, #388e3c 0%, #43a047 100%);
    transform: translateY(-2px);
    box-shadow: 0 5px 12px rgba(67, 160, 71, 0.4);
}

.send-button:active:not(:disabled) {
    transform: translateY(0);
}

.send-button:disabled {
    background: #e0e0e0;
    color: #9e9e9e;
    cursor: not-allowed;
    box-shadow: none;
}

.send-icon {
    font-size: 16px;
    display: inline-block;
    transition: transform 0.3s ease;
}

.send-button:hover:not(:disabled) .send-icon {
    transform: translateX(3px);
}

.send-text {
    font-weight: 600;
}

/* Responsive */
@media (max-width: 480px) {
    .send-text {
        display: none;
    }

    .send-button {
        padding: 12px 16px;
    }
}
</style>