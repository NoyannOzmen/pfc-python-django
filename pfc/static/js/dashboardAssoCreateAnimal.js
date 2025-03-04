document.addEventListener('DOMContentLoaded', ()=> {
    handleAddTag();
});


function handleAddTag() {
    
    const addTagBtn = document.getElementById('create-tag');
    const addTagModal =  document.getElementById('create-tags-modal');
    const addTagForm = document.getElementById('create-tags-form');
    
    addTagBtn.addEventListener('click', (event)=>{
        event.preventDefault();
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

    addTagForm.addEventListener('submit', (event)=>{
        event.preventDefault();
        const selectTagForm = document.getElementById('tags-animal'); 
        selectTagForm.innerHTML='';

        data.forEach(tag => {
            const wrapper = document.createElement('div');
            wrapper.classList.add('flex', 'gap-x-1.5');

            const tagOption = document.createElement('input');
            tagOption.type = 'checkbox';
            tagOption.id=`tag_${tag.id}`;
            tagOption.name=`tag_${tag.id}`;
            tagOption.value=`${tag.id}`;
            tagOption.classList.add('leading-3');

            wrapper.appendChild(tagOption);

            const tagLabel = document.createElement('label');
            tagLabel.htmlFor=`tag_${tag.id}`;
            tagLabel.classList.add('block', 'font-grands','font-semibold','text-xs','leading-3');
            tagLabel.innerText=`${tag.nom}`

            wrapper.appendChild(tagLabel);

            selectTagForm.appendChild(wrapper);
        });
        addTagForm.reset();
        addTagModal.classList.toggle('hidden');
        })
    }