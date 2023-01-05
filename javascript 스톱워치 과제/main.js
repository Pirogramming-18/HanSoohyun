let seconds = 0;
let tenMillis = 0;

const appendTens = document.getElementById("tenMillis");
const appendSeconds = document.getElementById("seconds");
const buttonStart= document.getElementById("startbtn");
const buttonStop= document.getElementById("stopbtn");
const buttonReset= document.getElementById("resetbtn");
const appendrecord = document.getElementById("qs");
const appendcheck = document.getElementById("checkall");
const buttontrash = document.getElementsByClassName("fa-solid fa-trash");
let intervalId;


// buttontrash.onClick = function() {
//     appendrecord.innerHTML += "asd"
// }


// appendcheck.onClick = function(){
//     //let as= document.getElementsByClassName('dj')
//     //nm.checked=true
//     appendrecord.innerHTML += "asd"
// }s

buttonStart.onclick = function(){
    clearInterval(intervalId)
    intervalId = setInterval(operateTimer, 10)
}

buttonStop.onclick = function() {
    clearInterval(intervalId)
    let asdf = tenMillis > 9 ? tenMillis : '0' + tenMillis;
    let qwer = seconds > 9 ? seconds : '0' + seconds;
    appendrecord.innerHTML += '<div><input class = "dj" type="checkbox"></input>'+qwer+":"+asdf+"</div>";

}

buttonReset.onclick = function() {
    clearInterval(intervalId)
    tenMillis=0 ; seconds =0
    appendTens.textContent = "00"
    appendSeconds.textContent = "00"
}

function operateTimer(){
    tenMillis++;
    appendTens.textContent = tenMillis > 9 ? tenMillis : '0' + tenMillis
    if(tenMillis > 99){
        seconds++;
        appendSeconds.textContent=seconds > 9 ? seconds : '0' + seconds
        tenMillis=0
        appendTens= "00"
    }
}

