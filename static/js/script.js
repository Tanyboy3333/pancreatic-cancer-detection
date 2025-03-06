document.getElementById("prediction-form").addEventListener("submit", async function(event) {
    event.preventDefault(); // Prevent default form submission

    // Get input values
    let feature1 = document.getElementById("feature1").value;
    let feature2 = document.getElementById("feature2").value;
    let feature3 = document.getElementById("feature3").value;
    let feature4 = document.getElementById("feature4").value;

    // Prepare data for API request
    let formData = new FormData();
    formData.append("feature1", feature1);
    formData.append("feature2", feature2);
    formData.append("feature3", feature3);
    formData.append("feature4", feature4);

    // Send POST request to Flask API
    let response = await fetch("/predict", {
        method: "POST",
        body: formData
    });

    // Get response JSON
    let result = await response.json();

    // Display prediction result
    document.getElementById("result").innerHTML = `Prediction: ${result.prediction === 1 ? "Positive (Cancer Detected)" : "Negative (No Cancer)"}`;
});
