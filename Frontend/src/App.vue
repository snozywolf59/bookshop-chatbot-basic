<script setup lang="ts">
import { ref } from "vue";
import ChatWindow from "./components/ChatWindow.vue";
import ChatInput from "./components/ChatInput.vue";

type Sender = "bot" | "user";

interface Message {
  sender: Sender;
  text: string;
  intent?: string;
  meta?: {
    title?: string; quantity?: number; author?: string; price?: number
  }
}


const messages = ref<Message[]>([
  { sender: "bot", text: "Xin chào 👋! Tôi là chatbot của bạn." },
]);

const handleSend = async (message: string) => {
  messages.value.push({ sender: "user", text: message });

  const res = fetch('http://localhost:8000/chat?user_input=' + encodeURIComponent(message));
  const data = await (await res).json();
  console.log(data)

  messages.value.push({ text: data.message, sender: 'bot', intent: data.intent, meta: data.meta });
};
</script>

<template>
  <div class="app">
    <h1>Chatbot Demo</h1>
    <ChatWindow :messages="messages" />
    <ChatInput @send="handleSend" />
  </div>
</template>

<style scoped>
.app {
  max-width: 500px;
  margin: auto;
  font-family: sans-serif;
}

body {
  background: #f0f2f5;
  margin: 0;
}
</style>
