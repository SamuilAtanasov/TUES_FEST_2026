document.getElementById("messageForm").addEventListener("submit", function(e) {
    e.preventDefault();

    const username = document.getElementById("username").value;
    const message = document.getElementById("message").value;

    const msgBox = document.getElementById("messages");

    const newMsg = document.createElement("div");
    newMsg.classList.add("msg");
    newMsg.innerHTML = `<strong>${username}:</strong> ${message}`;

    msgBox.appendChild(newMsg);

    this.reset();
})