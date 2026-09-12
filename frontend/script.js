const sliders = document.querySelectorAll('input[type="range"]');


// Update slider values
sliders.forEach(function(slider) {

    slider.addEventListener('input', function() {

        const value = slider.value;
        const label = slider.previousElementSibling;

        label.querySelector('span').textContent = value;

    });

});


// Collect slider values
function getFloodData() {

    const values = [];

    sliders.forEach(function(slider) {
        values.push(Number(slider.value));
    });

    return values;

}


// Predict button
const predictButton = document.querySelector('.predict-button');

predictButton.addEventListener('click', async function() {

    const values = getFloodData();


    const floodData = {

        MonsoonIntensity: values[0],
        TopographyDrainage: values[1],
        RiverManagement: values[2],
        Deforestation: values[3],
        Urbanization: values[4],
        ClimateChange: values[5],
        DamsQuality: values[6],
        Siltation: values[7],
        AgriculturalPractices: values[8],
        Encroachments: values[9],
        IneffectiveDisasterPreparedness: values[10],
        DrainageSystems: values[11],
        CoastalVulnerability: values[12],
        Landslides: values[13],
        Watersheds: values[14],
        DeterioratingInfrastructure: values[15],
        PopulationScore: values[16],
        WetlandLoss: values[17],
        InadequatePlanning: values[18],
        PoliticalFactors: values[19]

    };


    try {

        // Show loading state
        predictButton.textContent = "Analyzing...";
        predictButton.disabled = true;


        const response = await fetch(
            "https://flood-prediction-3eui.onrender.com/predict",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(floodData)
            }
        );


        const result = await response.json();

        console.log("API response:", result);


        // Get result elements
        const resultCard = document.getElementById("result");
        const riskLevel = document.getElementById("risk-level");
        const probability = document.getElementById("probability");
        const recommendation = document.getElementById("recommendation");


        // Display risk level
        riskLevel.textContent = result.risk_level;


        // Convert probability to percentage
        const percentage =
            (result.Flood_Probability * 100).toFixed(2);


        probability.textContent =
            "Flood Probability: " + percentage + "%";
        const meterFill = document.getElementById("meter-fill");

        meterFill.style.width = percentage + "%";

        meterFill.style.background = result.color_code;    


        // Display recommendation
        recommendation.textContent =
            "Recommendation: " + result.recommendation;


        // Change result colors
        resultCard.style.borderLeftColor = result.color_code;
        riskLevel.style.color = result.color_code;


        // Emergency warning
        let emergencyMessage =
            document.getElementById("emergency-message");


        if (!emergencyMessage) {

            emergencyMessage = document.createElement("div");

            emergencyMessage.id = "emergency-message";

            resultCard.appendChild(emergencyMessage);

        }


        if (result.emergency_action_required) {

            emergencyMessage.textContent =
                "⚠️ EMERGENCY: Immediate action may be required.";

            emergencyMessage.style.display = "block";

        } else {

            emergencyMessage.textContent = "";

            emergencyMessage.style.display = "none";

        }


    } catch (error) {

        console.error("Prediction error:", error);

        document.getElementById("risk-level").textContent =
            "Prediction failed";

        document.getElementById("probability").textContent =
            "";

        document.getElementById("recommendation").textContent =
            "Could not connect to the prediction server.";

    }


    // Restore button
    predictButton.textContent = "Predict Flood Risk";
    predictButton.disabled = false;

});
// Reset all sliders

const resetButton = document.querySelector('.reset-button');

resetButton.addEventListener('click', function() {

    sliders.forEach(function(slider) {

        slider.value = 5;

        const label = slider.previousElementSibling;

        label.querySelector('span').textContent = "5";

    });


    document.getElementById("risk-level").textContent =
        "Waiting for prediction...";

    document.getElementById("probability").textContent =
        "Flood Probability: —";

    document.getElementById("recommendation").textContent =
        "";

    document.getElementById("emergency-message").textContent =
        "";

    document.getElementById("emergency-message").style.display =
        "none";


    const resultCard = document.getElementById("result");

    resultCard.style.borderLeftColor = "#64748b";
    document.getElementById("meter-fill").style.width = "0%";

});