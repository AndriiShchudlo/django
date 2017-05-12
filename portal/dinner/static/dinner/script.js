function addFood(foodName, categoryId) {
    document.getElementById(categoryId).innerHTML = foodName;
    foods = {
    'first': document.getElementById(1).innerHTML,
    'garnir': document.getElementById(2).innerHTML,
    'salat': document.getElementById(3).innerHTML ,
    'miasne': document.getElementById(4).innerHTML,
    'fruits': document.getElementById(5).innerHTML,
    'complex': document.getElementById(6).innerHTML,
    }

    $.ajax({
        type: 'GET',
        async: true,
        url: '/get_price/',
        data: foods,
        success: function(data) {
        $('#price').text(data.price);
},
dataType: 'json',
});
    if ($('#price').text() != '')
        $('#customDinner_btn').removeAttr('disabled');
    else
        $('#customDinner_btn').attr('disabled','disable');
}


function deleteFood(categoryId) {
    document.getElementById(categoryId).innerHTML = "";
    foods = {
    'first': document.getElementById(1).innerHTML,
    'garnir': document.getElementById(2).innerHTML,
    'salat': document.getElementById(3).innerHTML ,
    'miasne': document.getElementById(4).innerHTML,
    'fruits': document.getElementById(5).innerHTML,
    'complex': document.getElementById(6).innerHTML,
    }

    $.ajax({
        type: 'GET',
        async: true,
        url: '/get_price/',
        data: foods,
        success: function(data) {
        $('#price').text(data.price);
},
dataType: 'json',
});
    if ($('#price').text() != '')
        $('#customDinner_btn').removeAttr('disabled');
    else
        $('#customDinner_btn').attr('disabled','disable');
}

function customDinner() {
    foods = {
    'first': document.getElementById(1).innerHTML,
    'garnir': document.getElementById(2).innerHTML,
    'salat': document.getElementById(3).innerHTML ,
    'miasne': document.getElementById(4).innerHTML,
    'fruits': document.getElementById(5).innerHTML,
    'complex': document.getElementById(6).innerHTML,
    'dinnerDate': document.getElementById("dinnerDate").innerHTML,
    }
    $.ajax({
        type: 'GET',
        async: true,
        url: '/addDinner/',
        data: foods,
        success: function(data) {
        $('#1').text("");
        $('#2').text("");
        $('#3').text("");
        $('#4').text("");
        $('#5').text("");
        $('#6').text("");
        $('#price').text("");
        if (data=="True"){
            $('#confirmation').text("Замовлення успішно виконане. Ви можете покинути сайт, або зробити ще одне замовлення. Для зміни дати замовлення перейдіть на головну сторінку")
        }
},
dataType: 'json',
});
}
