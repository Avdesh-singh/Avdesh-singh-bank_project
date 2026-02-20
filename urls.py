<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Account Balance</h1>
   <form action="" method="post">
    {% csrf_token %}
     Account Number: <input type="text" name="acc">
    pin : <input type="text" name="pin">
    <button type="submit">CHECK BALANCE</button>
   </form>

        <p>{{ msg }}</p>


</body>
</html>