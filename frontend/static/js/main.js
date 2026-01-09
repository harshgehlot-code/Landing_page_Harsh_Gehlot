// Use relative URLs since we're on the same origin
const API_BASE_URL = '/api';

// Get CSRF token from cookies (Django standard)
function getCSRFToken() {
    let cookieValue = null;

    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');

        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();

            // Does this cookie string begin with csrftoken= ?
            if (cookie.substring(0, 10) === 'csrftoken=') {
                cookieValue = decodeURIComponent(cookie.substring(10));
                break;
            }
        }
    }
    return cookieValue;
}


// Utility function for API calls
// async function fetchAPI(url, options = {}) {
//     try {
//         const response = await fetch(url, {
//             ...options,
//             headers: {
//                 'Content-Type': 'application/json',
//                 // "X-CSRFToken": getCSRFToken(),
//                 ...options.headers
//             }
//         });

//         const data = await response.json();

//         if (!response.ok) {
//             throw new Error(data.detail || data.message || 'An error occurred');
//         }

//         return { success: true, data };
//     } catch (error) {
//         console.error('API Error:', error);
//         return { success: false, error: error.message };
//     }
// }
async function fetchAPI(url, options = {}) {
    try {
        const response = await fetch(url, {
            method: options.method || 'GET',
            credentials: 'include', // ⭐ REQUIRED FOR CSRF
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken(), // ⭐ REQUIRED
                ...(options.headers || {})
            },
            body: options.body || null
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || data.message || 'An error occurred');
        }

        return { success: true, data };
    } catch (error) {
        console.error('API Error:', error);
        return { success: false, error: error.message };
    }
}


// Show alert message
function showAlert(containerId, message, type = 'success') {
    const container = document.getElementById(containerId);
    container.innerHTML = `
        <div class="alert alert-${type === 'success' ? 'success' : 'danger'} alert-dismissible fade show" role="alert">
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `;
    
    // Auto-dismiss after 5 seconds
    setTimeout(() => {
        const alert = container.querySelector('.alert');
        if (alert) {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }
    }, 5000);
}

// Load Projects
async function loadProjects() {
    const container = document.getElementById('projectsContainer');
    const loading = document.getElementById('projectsLoading');
    const empty = document.getElementById('projectsEmpty');

    loading.style.display = 'block';
    container.innerHTML = '';
    empty.style.display = 'none';

    const result = await fetchAPI(`${API_BASE_URL}/projects/`);

    loading.style.display = 'none';

    if (!result.success) {
        container.innerHTML = `
            <div class="col-12">
                <div class="alert alert-danger">
                    <i class="bi bi-exclamation-triangle"></i> 
                    Failed to load projects: ${result.error}
                </div>
            </div>
        `;
        return;
    }

    const projects = result.data.results || result.data;

    if (projects.length === 0) {
        empty.style.display = 'block';
        return;
    }

    projects.forEach(project => {
        const imageUrl = project.image ? project.image : 'https://via.placeholder.com/450x350?text=No+Image';
        const card = `
            <div class="col-md-6 col-lg-4">
                <div class="project-card">
                    <img src="${imageUrl}" alt="${escapeHtml(project.name)}" onerror="this.src='https://via.placeholder.com/450x350?text=Image+Not+Found'">
                    <div class="project-card-body">
                        <h5 class="project-card-title">${escapeHtml(project.name)}</h5>
                        <p class="project-card-description">${escapeHtml(project.description)}</p>
                        <button class="btn btn-outline-primary btn-sm w-100">READ MORE</button>
                    </div>
                </div>
            </div>
        `;
        container.innerHTML += card;
    });
}

async function loadClients() {
    const container = document.getElementById("clientsContainer");
    const loading = document.getElementById("clientsLoading");
    const empty = document.getElementById("clientsEmpty");

    loading.style.display = "block";
    container.innerHTML = "";
    empty.style.display = "none";

    try {
        const response = await fetch(`${API_BASE_URL}/clients/`);
        const result = await response.json();

        loading.style.display = "none";

        const clients = result.results || result;

        if (!clients || clients.length === 0) {
            empty.style.display = "block";
            return;
        }

        clients.forEach(client => {
            const imageUrl = client.image
                ? client.image
                : "https://via.placeholder.com/100?text=No+Image";

            const card = `
                <div class="col-md-6 col-lg-4">
                    <div class="client-card">
                        <div class="client-avatar">
                            <img src="${imageUrl}"
                                 alt="${escapeHtml(client.name)}"
                                 onerror="this.src='https://via.placeholder.com/100?text=No+Image'">
                        </div>

                        <div class="client-card-body">
                            <p class="client-testimonial">
                                ${escapeHtml(client.description)}
                            </p>
                            <h5 class="client-card-name">
                                ${escapeHtml(client.name)}
                            </h5>
                            <p class="client-designation">
                                ${escapeHtml(client.designation)}
                            </p>
                        </div>
                    </div>
                </div>
            `;

            container.insertAdjacentHTML("beforeend", card);
        });

    } catch (error) {
        loading.style.display = "none";
        container.innerHTML = `
            <div class="col-12">
                <div class="alert alert-danger text-center">
                    Failed to load testimonials
                </div>
            </div>
        `;
    }
}

/* Utility: Escape HTML */
function escapeHtml(text) {
    if (!text) return "";
    return text.replace(/[&<>"']/g, function (m) {
        return ({
            "&": "&amp;",
            "<": "&lt;",
            ">": "&gt;",
            '"': "&quot;",
            "'": "&#039;"
        })[m];
    });
}
/* Load on page load */
// document.addEventListener("DOMContentLoaded", loadClients);






// Escape HTML to prevent XSS
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Handle Contact Form Submission
document.getElementById('contactForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = {
        full_name: document.getElementById('fullName').value.trim(),
        email: document.getElementById('email').value.trim(),
        mobile: document.getElementById('mobile').value.trim(),
        city: document.getElementById('city').value.trim()
    };

    const submitButton = e.target.querySelector('button[type="submit"]');
    const originalText = submitButton.textContent;
    submitButton.disabled = true;
    submitButton.textContent = 'Submitting...';

    const result = await fetchAPI(`${API_BASE_URL}/contacts/`, {
        method: 'POST',
        body: JSON.stringify(formData)
    });

    submitButton.disabled = false;
    submitButton.textContent = originalText;

    if (result.success) {
        showAlert('contactAlert', 'Thank you! Your contact form has been submitted successfully.', 'success');
        e.target.reset();
    } else {
        let errorMessage = result.error;
        if (result.data && result.data.errors) {
            const errors = Object.values(result.data.errors).flat().join(', ');
            errorMessage = errors || errorMessage;
        }
        showAlert('contactAlert', `Error: ${errorMessage}`, 'danger');
    }
});

// Handle Newsletter Form Submission
document.getElementById('newsletterForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const email = document.getElementById('newsletterEmail').value.trim();

    const submitButton = e.target.querySelector('button[type="submit"]');
    const originalText = submitButton.textContent;
    submitButton.disabled = true;
    submitButton.textContent = 'Subscribing...';

    const result = await fetchAPI(`${API_BASE_URL}/newsletter/`, {
        method: 'POST',
        body: JSON.stringify({ email })
    });

    submitButton.disabled = false;
    submitButton.textContent = originalText;

    if (result.success) {
        showAlert('newsletterAlert', 'Successfully subscribed to newsletter!', 'success');
        e.target.reset();
    } else {
        let errorMessage = result.error;
        if (result.data && result.data.errors) {
            const errors = Object.values(result.data.errors).flat().join(', ');
            errorMessage = errors || errorMessage;
        }
        showAlert('newsletterAlert', `Error: ${errorMessage}`, 'danger');
    }
});

// Load data on page load
document.addEventListener('DOMContentLoaded', () => {
    loadProjects();
    loadClients();
});



