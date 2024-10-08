function logout() {
    alert("logout")
    fetch(`${ip}/logout`, {
        method: 'POST',
    }).then(() => {
        window.location.href = '/';
    }).catch(error => console.error('Error during logout:', error));
}

function reserve(){
    alert("Thank you for making a reservation")
    const formData = {
        name: document.getElementById('name').innerHTML,
        bookId: document.getElementById('detail-bookId').textContent,
        identity: document.getElementById('identity').innerHTML,
        bookTitle: document.getElementById('detail-title').textContent,
        location: document.getElementById('location').value,
        reserveTime: new Date().toISOString()
    };

    //Public IP below
    fetch(`${ip}/reserve`, {
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
