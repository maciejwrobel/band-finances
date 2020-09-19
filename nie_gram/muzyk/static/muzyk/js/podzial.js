    function showOptions1() {

        if (document.getElementById("management").checked == true){
            document.getElementById("1").style.display = "block";
            } else {
            document.getElementById("1").style.display = "none";
            document.getElementById("procent-man").value = "0"
            }
            }

    function showOptions3() {


        if (document.getElementById("fundusz").checked == true){
            document.getElementById("3").style.display = "block";
            } else {
            document.getElementById("3").style.display = "none";
            document.getElementById("kwota-na-fundusz").value = "0"
            }
            }

    function calcWynik() {
        let kwo = document.getElementsByName("kwota")[0].value;
        let os = document.getElementsByName("osoby")[0].value;
        let tran = document.getElementsByName("transport")[0].value;
        let hot = document.getElementsByName("hotel")[0].value;
        let go = document.getElementsByName("goscie")[0].value;
        let obs = document.getElementsByName("obsluga")[0].value;
        let pro = document.getElementsByName("procent-man")[0].value;
        let fun = document.getElementsByName("kwota-na-fundusz")[0].value;

        let pokosztach = Number(kwo) - Number(tran) - Number(hot) - Number(obs) - Number(go)
        let manager = Number(pokosztach) * Number(pro) / 100

        let wyn = (Number(pokosztach) - Number(manager) - Number(fun)) / Number(os)
        document.getElementsByName("wyn")[0].value = Math.round(wyn*100)/100;
    }
