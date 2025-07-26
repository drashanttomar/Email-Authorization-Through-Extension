function getEmailBody() {
    let emailBody = document.querySelector("div.a3s"); // Gmail body
    return emailBody ? emailBody.innerText : "";
}

function sendToBackend(content) {
    fetch("http://127.0.0.1:5000/check_email", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ content: content })
    })
    .then(response => response.json())
    .then(data => {
        alert("Email Status: " + data.status);
    })
    .catch(error => {
        console.error("Failed to connect to backend:", error);
        alert("Failed to connect to backend. Please ensure the Flask server is running.");
    });
}

function addScanButton() {
    const button = document.createElement("button");
    button.textContent = "Scan Email";
    button.style.position = "fixed";
    button.style.bottom = "20px";
    button.style.right = "20px";
    button.style.zIndex = "9999";
    button.style.padding = "10px";
    button.style.backgroundColor = "#4CAF50";
    button.style.color = "white";
    button.style.border = "none";
    button.style.borderRadius = "5px";
    button.style.cursor = "pointer";
    
    button.onclick = () => {
        const content = getEmailBody();
        if (content) {
            sendToBackend(content);
        } else {
            alert("No email content found.");
        }
    };

    document.body.appendChild(button);
}

// Wait for Gmail to load
window.addEventListener("load", () => {
    setTimeout(addScanButton, 5000);
});
