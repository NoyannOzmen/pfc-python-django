const editBtns = document.querySelector('.material-symbols-outlined');

editBtns.addEventListener("click", enableEdit);
editBtns.addEventListener("keydown", function(e) {
  if(e.keyCode==13){
    enableEdit(e)
   }
});

function enableEdit(e) {
  const field = e.target.closest('fieldset')
  const inputs = field.querySelectorAll('input')
  const validate = document.getElementById("validateBtn");
  const area = field.querySelector('textarea')

  if (validate.classList.contains('hidden')) {
  validate.classList.toggle('hidden')
  }

  area.disabled = false;
  area.required = true
  area.classList.add('bg-fond')

  inputs.forEach((input) => {
      input.disabled = false;
      input.required = true
      input.classList.add('bg-fond')
  })
	
  const site = document.getElementById('site');
  site.required = false
  const description = document.getElementById('description');
  description.required = false
}