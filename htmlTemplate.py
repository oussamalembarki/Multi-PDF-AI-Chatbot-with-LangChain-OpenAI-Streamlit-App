css = '''
<style>
.chat-message {
    padding: 1rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
    max-width: 80%;
}

.chat-message.user {
    background-color: #f0f2f6;
    margin-left: auto;
    border-bottom-right-radius: 0;
    color: #222;
}

.chat-message.bot {
    background-color: #eaf7ff;
    margin-right: auto;
    border-bottom-left-radius: 0;
    color: #222;
}

.chat-message .avatar {
    width: 32px;
    height: 32px;
    margin-right: 0.75rem;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
}

.chat-message .avatar img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
}

.chat-message .message {
    flex: 1;
    padding: 0;
    line-height: 1.5;
    font-size: 0.9rem;
    color: inherit;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://cdn-icons-png.flaticon.com/512/4712/4712035.png">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''