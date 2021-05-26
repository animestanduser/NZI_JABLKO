function ocenaPlus(){
    var ocena = parseInt(document.getElementById("id_punkty").value);
    ocena = ocena + 12;
    document.getElementById("id_punkty").value = String(ocena)
    if(ocena >= 1200){
        document.getElementById("id_ranga").value = "wood";
    }
    if(ocena >= 1400){
        document.getElementById("id_ranga").value = "leaf";
    }
    if(ocena >= 1600){
        document.getElementById("id_ranga").value = "gold";
    }
    if(ocena >= 1800){
        document.getElementById("id_ranga").value = "diamond";
    }
}


function ocenaMinus(){
    var ocena = parseInt(document.getElementById("id_punkty").value);
    ocena = ocena - 18;
    document.getElementById("id_punkty").value = String(ocena)
    if(ocena < 1800){
        document.getElementById("id_ranga").value = "gold";
    }
    if(ocena < 1600){
        document.getElementById("id_ranga").value = "leaf";
    }
    if(ocena < 1400){
        document.getElementById("id_ranga").value = "wood";
    }
    if(ocena < 1200){
        document.getElementById("id_ranga").value = "brak";
    }
}


