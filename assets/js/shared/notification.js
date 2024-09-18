class NotificationService {
    constructor() {}

    /**
     * Method to register a notification in the web page
     * @param {*} message
     * @param {*} servierty
     */
    #notificationManager = (message, servierty) => {
        let toastElement = `
        <div class="toast align-items-center text-bg-${servierty} border-0" role="alert" aria-live="assertive" aria-atomic="true">
            <div class="d-flex">
                <div class="toast-body">
                ${message}
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
        </div>`;

        let notificationContainer =
            document.getElementById("notification-block");
        if (!notificationContainer) {
            notificationContainer = document.createElement("div");
            notificationContainer.setAttribute("id", "notification-block");
            document.appendChild(notificationContainer);
        }

        notificationContainer.innerHTML += toastElement;
        const toastElList = document.querySelectorAll(".toast");
        const toastList = [...toastElList].map((toastEl) => {
            toastEl.addEventListener("hidden.bs.toast", (event) => {
                event.target.remove();
            });
            return new bootstrap.Toast(toastEl, {});
        });

        toastList.forEach((toast) => {
            toast.show();
        });
    };

    success = (message) => {
        this.#notificationManager(message, "success");
    };

    error = (message) => {
        this.#notificationManager(message, "danger");
    };

    warning = (message) => {
        this.#notificationManager(message, "warning");
    };

    info = (message) => {
        this.#notificationManager(message, "info");
    };
}

/**
 * Provide the notification instance to the current wepage, in which this script is imported
 */
notification = new NotificationService();
