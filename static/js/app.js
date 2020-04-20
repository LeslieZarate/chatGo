import { listChats ,systemDate } from './data.js'


// ---------- SECTION CONTACT  -----------------
const currentUser = document.getElementById("chat-user");
const contactUser = parseInt(currentUser.dataset.contact);
const contacts = document.getElementById('contacts'); // pintar lista de chat 

// -------------- SECTION CHAT --------------- 
const chatMessageSubmit = document.getElementById('chat-message-submit');
const messageSend = document.getElementById('message-send');
const nameChat = document.getElementById('name-chat');
const imgChat = document.getElementById('img-chat');
const msgCard = document.querySelector('#msg-card-body');
const idNameChat = parseInt(nameChat.dataset.chatws)
const cardSection = document.getElementById('card-section');


// ----------  SOCKET --------------

let chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/' + idNameChat + '/'
);

chatSocket.onopen = function (e) {
    console.log('connect default')
    fetchMessages(idNameChat)
}

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    if (data['command'] === 'messages') {
        msgCard.innerHTML = '';
        for (let i = 0; i < data['messages'].length; i++) {
            msgCard.appendChild(createMessage(data['messages'][i], contactUser));
        }
    } else if (data['command'] === 'new_message') {
        console.log('deafult messge')
        msgCard.appendChild(createMessage(data['message'], contactUser));
    }
};
chatSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly');
};

// -------------- SECTION CHAT --------------- 

messageSend.addEventListener('keyup', (e) => {
    if (e.keyCode === 13) {  // enter, return
        chatMessageSubmit.click();
    }
})

chatMessageSubmit.addEventListener('click', (e) => {
    const message = { content: messageSend.value, contact: contactUser, chat: idNameChat }
    chatSocket.send(JSON.stringify({ 'command': 'new_message', 'message': message  }));
    messageSend.value = '';
});

const createMessage = (data, currentUser) => {
    const divContent = document.createElement('div');
    const divContImg = document.createElement('div');

    const img = document.createElement('img')
    img.classList.add('rounded-circle', 'user_img_msg')
    img.src = data.contact.user.avatar

    const divContMsg = document.createElement('div')
    const spanMsgTime = document.createElement('span')

    divContImg.classList.add('img_cont_msg')
    divContent.classList.add('d-flex', 'mb-4');

    divContMsg.textContent = data.content;
    spanMsgTime.textContent = systemDate(data.timestamp);

    divContImg.appendChild(img)
    divContMsg.appendChild(spanMsgTime)

    if (data.contact.id === currentUser) {

        divContent.classList.add('justify-content-end');
        divContMsg.classList.add('msg_cotainer_send')
        spanMsgTime.classList.add('msg_time_send')

        divContent.appendChild(divContMsg);
        divContent.appendChild(divContImg);

    }
    else {
        divContent.classList.add('justify-content-start');
        divContMsg.classList.add('msg_cotainer')
        spanMsgTime.classList.add('msg_time')

        divContent.appendChild(divContImg);
        divContent.appendChild(divContMsg);
    }

    return divContent

}

const fetchMessages = (idNameChat) => {
    chatSocket.send(JSON.stringify({ 'command': 'fetch_messages', 'chat': idNameChat }));
}

// ---------- SECTION CONTACT  -----------------
const renderChatSection = (data, currentUser) => {
    cardSection.innerHTML = '';
    const card = document.createElement('div')
    card.classList.add("card")
    card.innerHTML =  `       
            <div class="card-header msg_head">
                <div class="d-flex bd-highlight">
                    <div class="img_cont">
                        <img src="${data.avatar}" class="rounded-circle user_img" id="img-chat-change">
                        <span class="online_icon"></span>
                    </div>
                    <div class="user_info">
                        <span id='name-chat-change' data-chatws="${data.id}">${data.name}</span>
                        <p>1767 Messages</p>
                    </div>
                    <div class="video_cam">
                        <span><i class="fas fa-video"></i></span>
                        <span><i class="fas fa-phone"></i></span>
                    </div>
                </div>
                <span id="action_menu_btn"><i class="fas fa-ellipsis-v"></i></span>
                <div class="action_menu">
                    <ul>
                        <li><i class="fas fa-user-circle"></i> View profile</li>
                        <li><i class="fas fa-users"></i> Add to close friends</li>
                        <li><i class="fas fa-plus"></i> Add to group</li>
                        <li><i class="fas fa-ban"></i> Block</li>
                    </ul>
                </div>
            </div>

            <div class="card-body msg_card_body" id="msg-card-body-change"></div>
            <div class="card-footer" id="card-footer">
                <div class="input-group">
                    <div class="input-group-append">
                        <span class="input-group-text attach_btn" ><i class="fas fa-paperclip"></i></span>
                    </div>
                    <textarea id="message-send-change" name="" class="form-control type_msg" placeholder="Type your message..."></textarea>
                    <div class="input-group-append" id="chat-message-submit-change">
                        <span class="input-group-text send_btn" ><i class="fas fa-location-arrow"></i></span>
                    </div>
                </div>
            </div>    
    `;
    cardSection.append(card);
    

    const msgCardChange = card.querySelector('#msg-card-body-change')
    chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/chat/' + data.id + '/'
    );
    chatSocket.onopen = function (e) {
        console.log('new connect ')
        chatSocket.send(JSON.stringify({ 'command': 'fetch_messages', 'chat': data.id }));
    }
    chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        if (data['command'] === 'messages') {
            // msgCardChange.innerHTML = '';
            for (let i = 0; i < data['messages'].length; i++) {
                msgCardChange.appendChild(createMessage(data['messages'][i], currentUser));
            }
        } else if (data['command'] === 'new_message') {
            console.log('new connect message')
            msgCardChange.appendChild(createMessage(data['message'], currentUser));
        }
    };
    chatSocket.onclose = function (e) {
        console.error('Chat socket closed unexpectedly');
    };
    
    
    const messageSendChange = card.querySelector('#message-send-change');
    messageSendChange.addEventListener('keyup', (e) => {
        if (e.keyCode === 13) {  // enter, return
            chatMessageSubmitChange.click();
        }
    })


    const chatMessageSubmitChange = card.querySelector('#chat-message-submit-change')
    chatMessageSubmitChange.addEventListener('click', (e) => {
        const messageChange = {
            content: messageSendChange.value,
            contact: currentUser,
            chat: data.id ,
        }
        console.log(messageChange)
        chatSocket.send(JSON.stringify({ 'command': 'new_message', 'message': messageChange,  }));
        messageSendChange.value = '';
    });
    
}

const itemChat = (data, currentUser) => {
    let nameContact;
    let avatarContact;

    if (data.type_chat === 2) {
        nameContact = data.name
        avatarContact = data.avatar
    } else {
        const participants = (data.participants).slice()
        for (let i = 0; i < participants.length; i++) {
            if (participants[i].id != currentUser) {
                nameContact = participants[i].user.username
                avatarContact = participants[i].user.avatar
            }
        }
    }

    const liElement = document.createElement('li');
    liElement.innerHTML = `
        <div class="d-flex bd-highlight" data-chatws=${data.id}>
            <div class="img_cont">
                <img src="${avatarContact}" class="rounded-circle user_img">
                <span class="online_icon"></span>
            </div>
            <div class="user_info">
                <span >${nameContact}</span>
                <p>${data.type_chat}</p>
            </div>
        </div>
          
    `;

    liElement.addEventListener('click', () => {        
        const items = contacts.querySelectorAll('.active')
        if (items.length !== 0) {
            items[0].classList.remove('active')
        }
        liElement.classList.add('active')

        const dataCard = { id : data.id , avatar : avatarContact , name:nameContact }

        renderChatSection(dataCard, currentUser)

    })

    return liElement;
}

const renderChatList = async (currentUser) => {
    contacts.innerHTML = ''
    const data = await listChats(currentUser)
    for (let i = 0; i < data.length; i++) {
        contacts.append(itemChat(data[i], currentUser))
    }
}


renderChatList(contactUser)









