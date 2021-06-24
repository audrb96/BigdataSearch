function reset(){
    var prefix = document.getElementById("prefix");
    prefix.value="";

}

function suggestion() {
    var prefix = document.getElementById("prefix");

    var prefix_value = prefix.value;

    if (prefix_value ==""){
        alert('Write your lyrics');
        return;
    }

    var formData = new FormData();
    formData.append("context", prefix_value );

    fetch(
        "/kogpt2",
        {
            method: "POST",
            body:formData
        }
    )
    .then(response => {
        if (response.status == 200){
            return response
        }
        else{
            throw Error("Failed");
        }
    })

    .then(response => response.json())
    .then(response => {
        var element = document.getElementById("context");
            element.innerHTML = response[0];

    })
    .catch(e => {

        var element = document.getElementById("context");
        element.textContent = e;
    })
}

