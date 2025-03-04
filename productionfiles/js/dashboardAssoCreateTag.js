const addTagBtn = document.getElementById('create-tag');
const addTagModal =  document.getElementById('create-tags-modal');
const addTagForm = document.getElementById('create-tags-form');

addTagBtn.addEventListener('click', (event)=>{
    event.preventDefault();
    addTagForm.reset();
    addTagModal.classList.toggle('hidden');
})

const closeBtns = document.querySelectorAll('.cancel');

closeBtns.forEach(btn => {
    btn.addEventListener('click',(event)=>{
        event.preventDefault();
        
        addTagModal.classList.toggle('hidden');
        addTagForm.reset();
    })
    
});

addTagForm.addEventListener('submit', ()=>{
    addTagModal.classList.toggle('hidden');
})