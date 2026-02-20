<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="{% static 'css/index.css' %}">
</head>
<body>
    <div id="header">
        <img src="https://cdn.pixabay.com/photo/2017/09/07/08/54/money-2724241_1280.jpg" alt="logo" id="img1">
        <h1>MONEY HEIST BANK</h1>
    </div>
    <div id="items">
    <div class="div1">
        <a href="{% url 'register' %}">
            <img src="{% static 'images/acc.png' %}" alt="">
            <h1>Register</h1>
        </a>
    </div>
   <div class="div1">
     <a href="{% url 'pin' %}">
        <img src="{% static 'images/pin.jpg' %}" alt="">
        <h1>SET PIN</h1>
    </a>
   </div>
    <div class="div1">
        <a href="{% url 'deposit' %}"><img src="{% static 'images/deposit.png' %}" alt="">
        <h1>DEPOSIT</h1>
        </a>
    </div>
   <div class="div1">
     <a href="{% url 'with' %}"><img src="{% static 'images/withdraw.png' %}" alt="">
        <h1>WITHDRAW</h1>
    </a>
   </div>
   <div class="div1">
    <a href="{% url 'balance' %}"><img src="{% static 'images/enquiry.png' %}" alt="">
        <h1>BALANCE ENQUIRY</h1>
    </a>
   </div>
   <div class="div1">
    <a href="{% url 'acc' %}"><img src="{% static 'images/acc_transfer.jpg' %}" alt="">
        <h1>ACCOUNT TRANSFER</h1>
    </a>
   </div>
    </div>
</body>
</html>