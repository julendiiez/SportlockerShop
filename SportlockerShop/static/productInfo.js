const box=document.getElementsByClassName("contenidoRopa");
const inputs=document.querySelectorAll(".contenidoRopa input")
const descriptionBox=document.getElementsByClassName("description-box")


const getData1 =(e) =>{
    url1=`/dataDescription/${e.target.name}`
    console.log(url1)
    $.ajax({
        type:'GET',
        url:url1,
        success:function(response){
            const data=response.data
            data.forEach(el => {
                descriptionBox.innerHTML+=`
                ${el.descripcion}`
            
            });
        },
            error:function(error){
                console.log(error)
            }
        });
}
inputs.forEach((input)=>{
    input.addEventListener("click",getData1)
});





