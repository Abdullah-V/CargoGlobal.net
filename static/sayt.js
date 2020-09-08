// deletion confirm
function confir(id){
    var qerar = confirm("Elanı silmək istəyirsiniz?")
    if(qerar == true){
        window.location.href = "/sil/"+id
        alert("Elanınız silindi!")
    }
    else{
        alert("Elanınız silinmədi!")
    }
}

var bar = document.querySelector("#scrolldiv")
console.log(bar)
window.addEventListener("scroll",() => {
    var max = document.body.scrollHeight - innerHeight
    bar.style.width = `${(pageYOffset/max) *100}%`
    console.log(pageYOffset);
})



