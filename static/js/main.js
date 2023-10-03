/* elements*/

const chatElement = document.getElementById('#chat')
const chatOpenElement = document.getElementById('#chat_open')
const chatJoinElement = document.getElementById('#chat_join')
const chatIconElement = document.getElementById('#chat_icon')
const chatWelcomeElement = document.getElementById('#chat_welcome')


/* Event listners */
chatIconElement.addEventListener = function (e) {
    e.preventDefault()
    chatIconElement.classList.add("hidden")
    chatWelcomeElement.classList.remove("hidden")
    return false
}


