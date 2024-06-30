function passInfo() {
    var name = document.getElementById('name').value;
    var identity = document.getElementById('identity').value;
    
    if (name === "" || identity === "") {
        alert("Please fill out all required fields.");
        return;
    }
    
    var url = 'main.html?name=' + encodeURIComponent(name) + '&identity=' + encodeURIComponent(identity);
    document.location.href = url;
}

document.getElementById('reservationForm').addEventListener('submit', function(event) {
    event.preventDefault();
    passInfo();
});
