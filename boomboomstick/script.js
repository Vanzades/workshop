// JavaScript untuk interaksi sederhana
document.addEventListener('DOMContentLoaded', () => {
    console.log('Landing page loaded successfully!');

    // Tambahkan fitur interaksi di sini jika diperlukan
    const buttons = document.querySelectorAll('.button');

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            alert('Tombol telah diklik!');
        });
    });
});
