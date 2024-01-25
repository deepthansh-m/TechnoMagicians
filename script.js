function likePost(button) {
    var likeCount = button.parentNode.querySelector('.like-count');
    var currentLikes = parseInt(likeCount.innerText);
    likeCount.innerText = (currentLikes + 1) + ' likes';
    button.disabled = true;
}
document.addEventListener("DOMContentLoaded", function () {
    const mobileMenu = document.querySelector('.mobile-menu');
    const dropdownMenu = document.querySelector('.dropdown-menu');
    var loggedInUser = sessionStorage.getItem('loggedInUser');
    document.getElementById('user-greeting').textContent = 'Welcome, ' + loggedInUser;

    mobileMenu.addEventListener('click', toggleDropdown);

    function toggleDropdown() {
        if (dropdownMenu.style.display === 'block') {
            dropdownMenu.style.display = 'none';
        } else {
            dropdownMenu.style.display = 'block';
        }
    }
});
document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();

    var enteredUsername = document.getElementById('username').value;
    var enteredPassword = document.getElementById('password').value;

    var foundUser = users.find(user => user.username === enteredUsername);

    if (foundUser) {
        if (foundUser.password === enteredPassword) {
            alert('Login successfully !');
            sessionStorage.setItem('loggedInUser', enteredUsername);
            window.location.replace('quixil_login.html');
        } else {
            alert('Incorrect password');
        }
    } else {
        alert('Username not found');
        window.location.replace('signup.html');
    }
});