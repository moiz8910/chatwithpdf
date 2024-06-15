css='''
<style>
.chat-message {
    padding: 1.5rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
}
.chat-message.user {
    background-color: #2b313e;
}
.chat-message.bot {
    background-color: #475063;
}
.chat-message .avatar {
    width: 15%;
}
.chat-message avatar img {
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
}
.chat-message .message {
    width: 85%;
}
'''

bot_template ='''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://raw.githubusercontent.com/moiz8910/syncstore/master/download.jpeg
" style="max-height: 78px; max-width: 78px; border-radius: 50%;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template ='''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://raw.githubusercontent.com/moiz8910/syncstore/master/slido-blog-cover-1600x1066px-3.jpg
"style="max-height: 78px; max-width: 78px; border-radius: 50%;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
