const sliders = document.querySelectorAll('input[type="range"]');


sliders.forEach(function(slider) {

    slider.addEventListener('input', function() {

        const value = slider.value;

        const label = slider.previousElementSibling;

        label.querySelector('span').textContent = value;

    });

});


function getFloodData() {

    const values = [];

    sliders.forEach(function(slider) {
        values.push(Number(slider.value));
    });

    return values;
}


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

    } catch (error) {

        console.error("Prediction error:", error);

    }

});