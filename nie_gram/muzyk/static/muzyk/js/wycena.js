    function showHide() {

                if(document.getElementById("netto").checked) {
                    document.getElementById("podatek").value = "0";
                    document.getElementById("hiddenBlock").style.display='none';
                } else {
                    document.getElementById("hiddenBlock").style.display='block';
                    }
            }



    function calcWynik() {
        let sta = document.getElementsByName("stawka")[0].value;
        let pod = document.getElementsByName("podatek")[0].value;
        let inn = document.getElementsByName("inne")[0].value;
        let odl = document.getElementsByName("odleglosc")[0].value;
        let car = document.getElementsByName("cars")[0].value;
        let spa = document.getElementsByName("spalanie")[0].value;
        let pal = document.getElementsByName("paliwo")[0].value;
        let noc = document.getElementsByName("hotel")[0].value;

        let transport = Number(car) * Number(odl) * Number(spa) * Number(pal) / 100

        let wyn = (Number(sta) *(1 + (Number(pod) / 100))) + Number(inn) + Number(transport) + Number(noc);
        document.getElementsByName("wyn")[0].value = Math.round(wyn*100)/100;
    }
