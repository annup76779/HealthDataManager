class AuthService {
    AuthService() {}

    async handleSignup(event) {
        event.preventDefault(); // Prevent the default form submission behavior

        const name = document.getElementById("name").value;
        const role = document.getElementById("role").value;
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        try {
            console.log({
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken"), // Ensures CSRF protection in Django
                },
                body: JSON.stringify({
                    name: name,
                    role: role,
                    username: username,
                    password: password,
                }),
            });
            const response = await fetch("/auth/api/signup", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken"), // Ensures CSRF protection in Django
                },
                body: JSON.stringify({
                    name: name,
                    role: role,
                    username: username,
                    password: password,
                }),
            });

            if (response.ok) {
                // Redirect to home page after successful signup
                window.location.href = "/auth/login";
            } else {
                // If there's an error, parse the error message from the response and alert it
                const errorData = await response.json();
                let errorMessage = "";
                if (errorData.detail) {
                    errorMessage = errorData.detail; // General error message
                } else {
                    // If detailed errors are provided for fields
                    for (let field in errorData) {
                        errorMessage += `${field}: ${errorData[field].join(
                            ", "
                        )}\n`;
                    }
                }
                alert("Signup failed:\n" + errorMessage);
            }
        } catch (error) {
            console.error(error);
            // In case of network or other errors, display a general error message
            alert("An unexpected error occurred. Please try again later.");
        }
    }

    async handleLogin(event) {
        event.preventDefault(); // Prevent the default form submission behavior

        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        try {
            const response = await fetch("/auth/api/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken"), // Ensures CSRF protection in Django
                },
                body: JSON.stringify({
                    username: username,
                    password: password,
                }),
            });

            if (response.ok) {
                const data = await response.json();
                alert(data.role === "Patient");
                if (data.role === "Doctor") {
                    // window.location.href = "/auth/doctor_home";
                    alert("Docter Logged in successfully");
                } else if (data.role === "Patient") {
                    // Redirect to home page after successful signup
                    window.location.href = "/api/health-data/";
                }
            } else {
                // If there's an error, parse the error message from the response and alert it
                const errorData = await response.json();
                let errorMessage = "";
                if (errorData.detail) {
                    errorMessage = errorData.detail; // General error message
                } else {
                    // If detailed errors are provided for fields
                    for (let field in errorData) {
                        errorMessage += `${field}: ${errorData[field].join(
                            ", "
                        )}\n`;
                    }
                }
                alert("Signup failed:\n" + errorMessage);
            }
        } catch (error) {
            // In case of network or other errors, display a general error message
            alert("An unexpected error occurred. Please try again later.");
        }
    }
}
