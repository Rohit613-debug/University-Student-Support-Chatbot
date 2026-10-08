
const chatForm = document.getElementById("chat-form");
const userInput = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");
const sendButton = document.getElementById("send-button");

function addMessage(text, sender) {
    const message = document.createElement("div");

    message.className = sender === "user"
        ? "user-message"
        : "bot-message";

    message.textContent = text;

    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;
}

chatForm.addEventListener("submit", async function(event) {
    event.preventDefault();

    const question = userInput.value.trim();

    if (!question) {
        return;
    }

    addMessage(question, "user");
    userInput.value = "";
    sendButton.disabled = true;

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: question })
        });

        if (!response.ok) {
            throw new Error("Unable to get response");
        }

        const data = await response.json();
        addMessage(data.response, "bot");

    } catch (error) {
        addMessage(
            "Sorry, something went wrong. Please try again.",
            "bot"
        );
        console.error(error);
    } finally {
        sendButton.disabled = false;
        userInput.focus();
    }
});
