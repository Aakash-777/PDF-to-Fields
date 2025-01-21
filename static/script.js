document.getElementById("pdf").addEventListener("change", async (event) => {
    const pdfInput = event.target.files[0];
    if (!pdfInput) {
        alert("Please upload a PDF file.");
        return;
    }

    const formData = new FormData();
    formData.append("pdf", pdfInput);

    // Show loader
    document.getElementById("loader").style.display = "block";

    try {
        const extractResponse = await fetch("/extract-text", {
            method: "POST",
            body: formData,
        });
        const extractData = await extractResponse.json();

        if (extractData.error) {
            alert("Error extracting text: " + extractData.error);
            return;
        }

        const extractedText = extractData.text || "";
        document.getElementById("output").textContent = extractedText;

        const populateResponse = await fetch("/extract-details", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: extractedText }),
        });
        const populateData = await populateResponse.json();

        if (populateData.error) {
            alert("Error populating fields: " + populateData.error);
            return;
        }

        document.getElementById("name").value = populateData.Name || "";
        document.getElementById("phone").value = populateData["Phone Number"] || "";
        document.getElementById("address").value = populateData.Address || "";
    } catch (error) {
        alert("An error occurred: " + error.message);
    } finally {
        // Hide loader after processing
        document.getElementById("loader").style.display = "none";
    }
});
