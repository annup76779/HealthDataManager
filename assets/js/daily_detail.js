async function submitDailyCheckup(event) {
    event.preventDefault(); // Prevent the default form submission

    // Gather form data
    const formData = {
        blood_sugar_morning: document.getElementById("blood_sugar_morning")
            .value,
        blood_sugar_after_breakfast: document.getElementById(
            "blood_sugar_after_breakfast"
        ).value,
        blood_sugar_before_lunch: document.getElementById(
            "blood_sugar_before_lunch"
        ).value,
        blood_sugar_after_lunch: document.getElementById(
            "blood_sugar_after_lunch"
        ).value,
        blood_sugar_before_dinner: document.getElementById(
            "blood_sugar_before_dinner"
        ).value,
        blood_sugar_after_dinner: document.getElementById(
            "blood_sugar_after_dinner"
        ).value,
        blood_sugar_before_bedtime: document.getElementById(
            "blood_sugar_before_bedtime"
        ).value,
        medication_taken: document.getElementById("medication_taken").checked,
        diet_details: document.getElementById("diet_details").value,
        foot_check_completed: document.getElementById("foot_check_completed")
            .checked,
        exercise_minutes: document.getElementById("exercise_minutes").value,
    };

    try {
        const response = await fetch("/api/daily_checkup", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken"), // Include CSRF token for Django
            },
            body: JSON.stringify(formData),
        });

        if (response.ok) {
            // If submission is successful, redirect to a page to view all daily checkups
            window.location.href = "/api/get_daily_details";
        } else {
            // Handle errors by showing an alert with the message
            const errorData = await response.json();
            notification.error(JSON.stringify(errorMessage));
        }
    } catch (error) {
        notification.error(
            "An unexpected error occurred. Please try again later."
        );
    }
}

let currentPage = 1;

// Fetch daily checkups from API
async function fetchDailyCheckups(url) {
    try {
        const response = await fetch(url, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        });

        if (response.ok) {
            const data = await response.json();
            displayCheckups(data.results); // Function to display the checkups
            setupPagination(data.count, data.next, data.previous);
        } else {
            alert("Failed to fetch daily checkups.");
        }
    } catch (error) {
        alert("An unexpected error occurred. Please try again later.");
    }
}

// Display daily checkups on the page
function displayCheckups(checkups) {
    const checkupContainer = document.getElementById("checkupContainer");
    checkupContainer.innerHTML = ""; // Clear the previous content

    checkups.forEach((checkup) => {
        const checkupDiv = document.createElement("div");
        checkupDiv.classList.add("checkup-item");
        checkupDiv.classList.add("col-md-4");
        checkupDiv.classList.add("col-12");

        checkupDiv.innerHTML = `
                    <h4>Checkup on ${checkup.date_recorded}</h4>
                    <p><strong>Blood Sugar Morning (Before Breakfast):</strong> ${
                        checkup.blood_sugar_morning || "N/A"
                    }</p>
                    <p><strong>Blood Sugar After Breakfast:</strong> ${
                        checkup.blood_sugar_after_breakfast || "N/A"
                    }</p>
                    <p><strong>Blood Sugar Before Lunch:</strong> ${
                        checkup.blood_sugar_before_lunch || "N/A"
                    }</p>
                    <p><strong>Blood Sugar After Lunch:</strong> ${
                        checkup.blood_sugar_after_lunch || "N/A"
                    }</p>
                    <p><strong>Blood Sugar Before Dinner:</strong> ${
                        checkup.blood_sugar_before_dinner || "N/A"
                    }</p>
                    <p><strong>Blood Sugar After Dinner:</strong> ${
                        checkup.blood_sugar_after_dinner || "N/A"
                    }</p>
                    <p><strong>Blood Sugar Before Bedtime:</strong> ${
                        checkup.blood_sugar_before_bedtime || "N/A"
                    }</p>
                    <p><strong>Medication Taken:</strong> ${
                        checkup.medication_taken ? "Yes" : "No"
                    }</p>
                    <p><strong>Foot Check Completed:</strong> ${
                        checkup.foot_check_completed ? "Yes" : "No"
                    }</p>
                    <p><strong>Exercise Minutes:</strong> ${
                        checkup.exercise_minutes || "N/A"
                    }</p>
                    <p><strong>Diet Details:</strong> ${
                        checkup.diet_details || "No details provided"
                    }</p>
                    <hr>
                `;
        checkupContainer.appendChild(checkupDiv);
    });
}

// Setup pagination controls
function setupPagination(totalCount, nextPage, prevPage) {
    const pagination = document.getElementById("pagination");
    pagination.innerHTML = ""; // Clear previous pagination controls

    // Create "Previous" button
    if (prevPage) {
        const prevButton = document.createElement("button");
        prevButton.classList.add("btn", "btn-outline-primary");
        prevButton.textContent = "Previous";
        prevButton.onclick = () => fetchDailyCheckups(prevPage);
        pagination.appendChild(prevButton);
    }

    // Create "Next" button
    if (nextPage) {
        const nextButton = document.createElement("button");
        nextButton.classList.add("btn", "btn-outline-primary");
        nextButton.textContent = "Next";
        nextButton.onclick = () => fetchDailyCheckups(nextPage);
        pagination.appendChild(nextButton);
    }
}
