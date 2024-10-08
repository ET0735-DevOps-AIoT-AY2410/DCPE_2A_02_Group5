//Request account details
document.addEventListener('DOMContentLoaded', () => {
    fetch(`${ip}/session`, {
        method: 'GET'
    })

    .then(response => {
        return response.json();
    })

    .then(data => {
        console.log('Session data:', data);
        if (!data.loggedIn) {
            console.log('User not logged in, redirecting to login page');
            window.location.href = '/';
        } 
        else {
            document.getElementById('name').innerHTML = data.name;
            document.getElementById('identity').innerHTML = data.identity;
        }
    })
});

