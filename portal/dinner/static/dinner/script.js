/**
 * Created by andriis on 10/05/17.
 */
function addFood(foodName, categoryId) {
    document.getElementById(categoryId).innerHTML = foodName;
    if ( document.getElementById("1").innerHTML != "" &&
         document.getElementById("2").innerHTML != "" &&
         document.getElementById("3").innerHTML != "" &&
         document.getElementById("4").innerHTML != "" &&
         document.getElementById("5").innerHTML == "" &&
         document.getElementById("6").innerHTML == ""
    )
        $('#price').text('45 грн');
}