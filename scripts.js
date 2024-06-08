document.addEventListener("DOMContentLoaded", function() {
    const configForm = document.getElementById("config-form");
    const responseForm = document.getElementById("response-form");
    const responseDiv = document.getElementById("response");

    configForm.addEventListener("submit", function(event) {
        event.preventDefault();
        const configData = {
            prompt: document.getElementById("prompt").value,
            temperature: parseFloat(document.getElementById("temperature").value),
            max_tokens: parseInt(document.getElementById("max_tokens").value),
            engine: document.getElementById("engine").value
        };
        fetch('/set-config', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(configData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === "success") {
                alert("Configuration updated successfully!");
            } else {
                alert("Error updating configuration: " + data.error);
            }
        });
    });

    responseForm.addEventListener("submit", function(event) {
        event.preventDefault();
        const inputData = {
            input: document.getElementById("user-input").value
        };
        fetch('/generate-response', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(inputData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.response) {
                responseDiv.innerText = data.response;
            } else {
                responseDiv.innerText = "Error: " + data.error;
            }
        });
    });
});
