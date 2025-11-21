document.addEventListener('DOMContentLoaded', () => {
    const makerForm = document.getElementById('maker-list-form');
    const messageDiv = document.getElementById('maker-form-message');

    if (makerForm) {
        makerForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            const emailInput = makerForm.querySelector('input[name="email"]');
            const email = emailInput.value;
            const submitButton = makerForm.querySelector('button[type="submit"]');

            // Disable button and show loading state
            submitButton.disabled = true;
            submitButton.textContent = 'Joining...';
            messageDiv.textContent = '';
            messageDiv.className = 'mt-2 text-sm';

            try {
                const response = await fetch('/join-maker-list', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ email: email }),
                });

                const data = await response.json();

                if (response.ok) {
                    messageDiv.textContent = "You're on the list! 🚀";
                    messageDiv.classList.add('text-green-600');
                    makerForm.reset();
                } else {
                    messageDiv.textContent = data.error || 'Something went wrong. Please try again.';
                    messageDiv.classList.add('text-red-600');
                }
            } catch (error) {
                console.error('Error:', error);
                messageDiv.textContent = 'Network error. Please try again.';
                messageDiv.classList.add('text-red-600');
            } finally {
                submitButton.disabled = false;
                submitButton.textContent = 'Join';
            }
        });
    }
});
