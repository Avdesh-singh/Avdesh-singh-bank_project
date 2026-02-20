<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="{% static 'css/pin.css' %}">
</head>
<body>
    <h1>PIN GENERATION</h1>
    <div id="container">
        <form action="" method="post">
        {% csrf_token %}
        <label for="">Enter your account number:</label>
        <input type="text" name="acc"> <br><br>
        <label for="">Phone number:</label>
        <input type="number" name="phn"><br><br>
        <label for="">Pin:</label>
        <input type="number" name="pin" id=""><br><br>
        <label for="">Confirm pin:</label>
        <input type="text" name="c_pin"><br><br>
        <button type="submit">SET PIN</button>
    </form>
    </div>
</body>
</html>