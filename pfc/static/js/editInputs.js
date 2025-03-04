const editBtns = document.querySelectorAll('.material-symbols-outlined');

editBtns.forEach(n => n.addEventListener("click", enableEdit));
editBtns.forEach(n => n.addEventListener("keydown", function(e) {
  if(e.keyCode==13){
    enableEdit(e)
   }
}))

function enableEdit(e) {
  const field = e.target.closest('fieldset')
  const inputs = field.querySelectorAll('input')
  const validate = document.getElementById("validate");
  
  if (validate.classList.contains('hidden')) {
    validate.classList.toggle('hidden')
  }
  
  inputs.forEach((input) => {
    input.disabled = false;
    input.required = true
    input.classList.add('bg-fond')
  })
  
  const terrain = document.getElementById('terrain');
  terrain.required = false
  const prenom = document.getElementById('prenom');
  prenom.required = false
}
