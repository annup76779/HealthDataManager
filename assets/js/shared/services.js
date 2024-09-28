// Function to retrieve CSRF token from Django's cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }
    return cookieValue;
}

function deleteAccessToDoctor(doctor_id) {
    fetch(`/api/delete_doctor_access/${doctor_id}`, {
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": document.querySelector(
                "input[name=csrfmiddlewaretoken]"
            ).value,
        },
        method: "DELETE",
    })
        .then(function (response) {
            if (response.ok) {
                let row = document.querySelector(`#doctor-access-${doctor_id}`);
                row.remove();
                notification.success("Removed doctor's access");
            } else {
                notification.error("Failed to remove doctor's access");
            }
        })
        .catch(function (error) {
            notification.error("Failed to remove doctor's access");
        });
}
