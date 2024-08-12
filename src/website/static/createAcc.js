document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const identity = document.getElementById('identity').value;
    const password = document.getElementById('password').value;
    const user = document.getElementById('user').value;

    fetch(`${ip}/signup`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ identity: identity, password: password, user: user})
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = '/browse';
        } else {
            alert('Sign Up failed: ' + data.message);
        }
    })
    .catch(error => console.error('Error:', error));
});