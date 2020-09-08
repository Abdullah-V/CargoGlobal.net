// deletion confirm
function confir(id){
    var qerar = confirm("elani silmek isteyirsiniz?")
    if(qerar == true){
        window.location.href = "/sil/"+id
        alert("elaniniz silindi!")
    }
    else{
        alert("elaniniz silinmedi!")
    }
}

var bar = document.querySelector("#scrolldiv")
console.log(bar)
window.addEventListener("scroll",() => {
    var max = document.body.scrollHeight - innerHeight
    bar.style.width = `${(pageYOffset/max) *100}%`
    console.log(pageYOffset);
})

