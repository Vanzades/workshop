<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Send Email</title>
</head>
<body>
    <h1>Send Email</h1>
    @if (session('success'))
        <p style="color: green;">{{ session('success') }}</p>
    @endif
    <form action="{{ route('send.email') }}" method="POST">
        @csrf
        <label for="email">Recipient Email:</label>
        <input type="email" name="email" id="email" required><br><br>

        <label for="subject">Subject:</label>
        <input type="text" name="subject" id="subject" required><br><br>

        <label for="message">Message:</label>
        <textarea name="message" id="message" required></textarea><br><br>

        <button type="submit">Send Email</button>
    </form>
</body>
</html>
