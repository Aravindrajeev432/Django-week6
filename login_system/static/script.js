var fnameError = document.getElementById('fname-error')
var lnameError = document.getElementById('lname-error')
var emailError = document.getElementById('email-error')
var mobileError = document.getElementById('mobile-error')
var addressError = document.getElementById('address-error')
var submitError = document.getElementById('btnError')
var passError = document.getElementById('pass-error')
var cityError = document.getElementById('city-error')
var zipError = document.getElementById('zip-error')
var stateError = document.getElementById('state-error')
var unameError = documnet.getElementById('uname-error')
function validateFName(){
    var name = document.getElementById('fname_id').value;

    if(name.length == 0){
        fnameError.innerHTML = 'Name required';
        return false;
    }
    if(!name.match(/^[a-zA-Z ]+$/)){
        fnameError.innerHTML = 'Name cannot contain numbers';
        return false;
    }
    fnameError.innerHTML = '<i class="fa fa-check" aria-hidden="true" style="color:green;"></i>';
    return true;
}
function validateLName(){
    var name = document.getElementById('lname_id').value;

    if(name.length == 0){
        lnameError.innerHTML = 'Name required';
        return false;
    }
    if(!name.match(/^[a-zA-Z ]+$/)){
        lnameError.innerHTML = 'Name cannot contain numbers';
        return false;
    }
    lnameError.innerHTML = '<i class="fa fa-check" aria-hidden="true" style="color:green;"></i>';
    return true;
}
function validateUName(){
    var uname = document.getElementById('uname_id').value;

    if(uname.length == 0){
        unameError.innerHTML = 'User name required';
        return false;
    }
    if(!uname.match(/^[a-zA-Z ]+$/)){
        unameError.innerHTML = 'User name cannot contain numbers';
        return false;
    }
    unameError.innerHTML = '<i class="fa fa-check" aria-hidden="true" style="color:green;"></i>';
    return true;
}

function validateMobile(){
    var mobile = document.getElementById('phone_id').value;
    console.log(mobile)
    if(mobile.length==0){
        mobileError.innerHTML = 'Mobile no required'
        return false;
    }
    if(mobile.length !==10){
        mobileError.innerHTML = 'Mobile no should be 10 digits'
        return false;
    }
    if(!mobile.match(/^[0-9]{10}$/)){
        mobileError.innerHTML = 'Mobile no required';
        return false;
    }
    mobileError.innerHTML = '<i class="fa fa-check" aria-hidden="true" style="color:green;"></i>';
    return true;
}
function validateEmail(){
    var email =  document.getElementById('email_id').value;
    if(email.length==0){
        emailError.innerHTML = 'Email required'
        return false;
    }
    if(!email.match(/^[A-Za-z\._\-[0-9]*[@][A-Za-z]*[\.][a-z]{2,4}$/)){
        emailError.innerHTML = 'Email Invalid'
        return false;
    }
    emailError.innerHTML = '<i class="fa fa-check" aria-hidden="true" style="color:green;"></i>';
    return true;
}
function validatePassword(){
    var pass= document.getElementById('pass_id').value;
    console.log(pass)
    if(pass.length==0){
        passError.innerHTML="Please include password"
        return false;
    }
    if(!pass.match(/^[A-Za-z]\w{7,14}$/)){
        passError.innerHTML ='Password must contain 6 to 20 characters with at least one numeric digit, one uppercase and one lowercase letter '
        return false;

    }
    passError.innerHTML ='<i class="fa fa-check" aria-hidden="true" style="color:green;"></i>';
    return true;
}

function validateAddress(){
    var address = document.getElementById('address_id').value;
    var required = 10;
    var left = required -address.length;
    if(left > 0){
        addressError.innerHTML =left + 'more character required'
        return false;
    }
    addressError.innerHTML = '<i class="fa fa-check" aria-hidden="true" style="color:green;"></i>';
    return true;
}
function validateCity(){
var city =document.getElementById('city_id').value;

if(city.length==0){
    cityError.innerHTML="Please include city name"
    return false;

}
if(!city.match(/^[a-zA-Z ]+$/)){
    cityError.innerHTML = 'City name cannot contain numbers';
    return false;
}
cityError.innerHTML = '<i class="fa fa-check" aria-hidden="true" style="color:green;"></i>';
    return true;


    }
    function validateState(){
        var state = document.getElementById('state_id').value;
        console.log(state);
        if (state=='State'){
            console.log('True')
            stateError.innerHTML='Please select a state';
            return false;
        }
        
        stateError.innerHTML='<i class="fa fa-check" aria-hidden="true" style="color:green;"></i>';
        return true;

    }

function validateZip(){
    var zip = document.getElementById('zip_id').value;
    if(zip.length==0){
        zipError.innerHTML = 'Please include zipcode'
        return false;
    }
    if(!zip.match(/^[0-9]{6}$/)){
        zipError.innerHTML = 'Zip code must have 6 digits'
        return false;
    }
    zipError.innerHTML = '<i class="fa fa-check" aria-hidden="true" style="color:green;"></i>';
    return true;

}



function validateForm(){
    if(!validateFName() || !validateLName() || !validateMobile() || !validateEmail() || !validatePassword() || !validateAddress() || !validateCity() || !validateZip() || !validateUName()){
        submitError.style.display = 'block';
        submitError.innerHTML = 'Please fix error to submit'
        setTimeout(function(){submitError.style.display = 'none';}, 3000);
        return false;
    }
}