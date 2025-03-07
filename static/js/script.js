document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("upload-form");

    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        let formData = new FormData(form);
        let resultDiv = document.getElementById("result");
        resultDiv.innerHTML = "Processing...";

        try {
            let response = await fetch("/", {
                method: "POST",
                body: formData,
            });

            let data = await response.json();
            resultDiv.innerHTML = `Prediction: <strong>${data.prediction}</strong>`;
        } catch (error) {
            resultDiv.innerHTML = "Error processing image!";
        }
    });
});
