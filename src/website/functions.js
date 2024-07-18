function logout() {
    alert("logout")
    fetch('http://127.0.0.1:5000/logout', {
        method: 'POST',
    }).then(() => {
        window.location.href = 'login.html';
    }).catch(error => console.error('Error during logout:', error));
}

function reserve(){
    alert("reserve")
    const formData = {
        name: document.getElementById('name').innerHTML,
        identity: document.getElementById('identity').innerHTML,
        bookTitle: document.getElementById('detail-title').textContent,
        location: document.getElementById('location').value,
        reserveTime: new Date().toISOString()
    };

    //Public IP below
    fetch('http://127.0.0.1:5000/reserve', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.getElementById('confirmationMessage').style.display = 'block';
            document.getElementById('reservationForm').reset();
        } else {
            alert('Too many books borrowed');
        }
    })
    .catch(error => console.error('Error:', error));
}