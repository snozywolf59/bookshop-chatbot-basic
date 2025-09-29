<script setup lang="ts">
import { ref } from 'vue';

defineProps<{
    messages: {
        text: string;
        sender: 'user' | 'bot';
        intent?: string;
        meta?: { title?: string; quantity?: number; author?: string; price?: number }
    }[];
}>();

const showModal = ref(false);
const currentOrder = ref<any>(null);

function openModal(meta: any) {
    currentOrder.value = { ...meta };
    showModal.value = true;
}

function confirmOrder() {
    alert(`Đặt thành công ${currentOrder.value.quantity} cuốn '${currentOrder.value.title}'`);
    showModal.value = false;
}
</script>

<template>
    <div class="chat-container">
        <div class="chat-window">
            <div v-for="(msg, index) in messages" :key="index" :class="['message', msg.sender]">
                <div class="message-content">
                    <div class="message-text">{{ msg.text }}</div>

                    <!-- Nếu intent = mua_sach thì hiển thị nút -->
                    <div v-if="msg.sender === 'bot' && msg.intent === 'mua_sach'" class="action-section">
                        <button class="confirm-btn" @click="openModal(msg.meta)">
                            <span class="btn-icon">📦</span>
                            Xác nhận đơn hàng
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal xác nhận -->
    <div v-if="showModal" class="modal-overlay" @click.self="showModal = false">
        <div class="modal">
            <div class="modal-header">
                <h3>📚 Xác nhận đơn hàng</h3>
                <button class="close-btn" @click="showModal = false">✕</button>
            </div>

            <div class="modal-body">
                <div class="info-row">
                    <span class="label">Sách:</span>
                    <span class="value">{{ currentOrder?.title }}</span>
                </div>
                <div class="info-row">
                    <span class="label">Tác giả:</span>
                    <span class="value">{{ currentOrder?.author }}</span>
                </div>
                <div class="info-row">
                    <span class="label">Đơn giá:</span>
                    <span class="value price">{{ currentOrder?.price?.toLocaleString() }}đ</span>
                </div>

                <div class="quantity-section">
                    <label class="label">Số lượng:</label>
                    <input type="number" v-model.number="currentOrder.quantity" min="1" class="quantity-input" />
                </div>

                <div class="total-section">
                    <span class="label">Tổng tiền:</span>
                    <span class="total-price">{{ (currentOrder?.price * currentOrder?.quantity)?.toLocaleString()
                    }}đ</span>
                </div>
            </div>

            <div class="modal-actions">
                <button class="btn-cancel" @click="showModal = false">Hủy</button>
                <button class="btn-confirm" @click="confirmOrder">✓ Xác nhận</button>
            </div>
        </div>
    </div>
</template>

<style scoped>
* {
    box-sizing: border-box;
}

.chat-container {
    width: 400px;
    margin: 0 auto;
    background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
    border-radius: 16px;
    padding: 16px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.chat-window {
    background: white;
    border-radius: 12px;
    padding: 16px;
    height: 400px;
    overflow-y: auto;
    scrollbar-width: thin;
    scrollbar-color: #66bb6a #f5f5f5;
}

.chat-window::-webkit-scrollbar {
    width: 8px;
}

.chat-window::-webkit-scrollbar-track {
    background: #f5f5f5;
    border-radius: 4px;
}

.chat-window::-webkit-scrollbar-thumb {
    background: #66bb6a;
    border-radius: 4px;
}

.message {
    margin: 12px 0;
    display: flex;
    animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.message.user {
    justify-content: flex-end;
}

.message.bot {
    justify-content: flex-start;
}

.message-content {
    max-width: 70%;
}

.message-text {
    padding: 12px 16px;
    border-radius: 18px;
    word-wrap: break-word;
    line-height: 1.5;
}

.message.user .message-text {
    background: linear-gradient(135deg, #43a047 0%, #66bb6a 100%);
    color: white;
    border-bottom-right-radius: 4px;
    box-shadow: 0 2px 6px rgba(67, 160, 71, 0.3);
}

.message.bot .message-text {
    background: #f1f8f4;
    color: #2e7d32;
    border-bottom-left-radius: 4px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
}

.action-section {
    margin-top: 8px;
}

.confirm-btn {
    padding: 10px 20px;
    background: linear-gradient(135deg, #43a047 0%, #66bb6a 100%);
    color: white;
    border: none;
    border-radius: 12px;
    cursor: pointer;
    font-size: 14px;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: all 0.3s ease;
    box-shadow: 0 3px 8px rgba(67, 160, 71, 0.3);
}

.confirm-btn:hover {
    background: linear-gradient(135deg, #388e3c 0%, #43a047 100%);
    transform: translateY(-2px);
    box-shadow: 0 5px 12px rgba(67, 160, 71, 0.4);
}

.confirm-btn:active {
    transform: translateY(0);
}

.btn-icon {
    font-size: 16px;
}

/* Modal styles */
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.6);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
    animation: fadeIn 0.2s ease-out;
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }

    to {
        opacity: 1;
    }
}

.modal {
    background: white;
    border-radius: 20px;
    width: 90%;
    max-width: 400px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
    animation: slideUp 0.3s ease-out;
}

@keyframes slideUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.modal-header {
    padding: 24px 24px 16px;
    border-bottom: 2px solid #e8f5e9;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.modal-header h3 {
    margin: 0;
    color: #2e7d32;
    font-size: 20px;
    font-weight: 700;
}

.close-btn {
    background: none;
    border: none;
    font-size: 24px;
    color: #757575;
    cursor: pointer;
    width: 32px;
    height: 32px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    transition: all 0.2s;
}

.close-btn:hover {
    background: #f5f5f5;
    color: #2e7d32;
}

.modal-body {
    padding: 24px;
}

.info-row {
    display: flex;
    justify-content: space-between;
    margin-bottom: 14px;
    padding: 8px 0;
}

.label {
    color: #757575;
    font-weight: 600;
    font-size: 14px;
}

.value {
    color: #2e7d32;
    font-weight: 600;
    text-align: right;
}

.price {
    color: #43a047;
    font-size: 16px;
}

.quantity-section {
    margin: 20px 0;
    padding: 16px;
    background: #f1f8f4;
    border-radius: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.quantity-input {
    width: 80px;
    padding: 8px 12px;
    border: 2px solid #c8e6c9;
    border-radius: 8px;
    font-size: 16px;
    font-weight: 600;
    color: #2e7d32;
    text-align: center;
    transition: all 0.2s;
}

.quantity-input:focus {
    outline: none;
    border-color: #66bb6a;
    box-shadow: 0 0 0 3px rgba(102, 187, 106, 0.1);
}

.total-section {
    margin-top: 20px;
    padding: 16px;
    background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
    border-radius: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.total-price {
    font-size: 24px;
    font-weight: 700;
    color: #2e7d32;
}

.modal-actions {
    padding: 16px 24px 24px;
    display: flex;
    justify-content: flex-end;
    gap: 12px;
}

.modal-actions button {
    padding: 12px 24px;
    border: none;
    border-radius: 12px;
    font-size: 15px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
}

.btn-cancel {
    background: #f5f5f5;
    color: #757575;
}

.btn-cancel:hover {
    background: #eeeeee;
    color: #424242;
}

.btn-confirm {
    background: linear-gradient(135deg, #43a047 0%, #66bb6a 100%);
    color: white;
    box-shadow: 0 3px 8px rgba(67, 160, 71, 0.3);
}

.btn-confirm:hover {
    background: linear-gradient(135deg, #388e3c 0%, #43a047 100%);
    transform: translateY(-2px);
    box-shadow: 0 5px 12px rgba(67, 160, 71, 0.4);
}

.btn-confirm:active,
.btn-cancel:active {
    transform: translateY(0);
}
</style>