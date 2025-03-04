document.addEventListener('DOMContentLoaded', () => {
    
    makeAdressList();
})


async function gouvApiCall (search) {
    const BASE_URL = 'https://api-adresse.data.gouv.fr/search/?q=';
    
    
    
    const searchParams = search.normalize('NFD').replace(/[\u0300-\u036f]/g, "").replace(/[\s\W]/g, '+');
    let url = BASE_URL+searchParams+'&limit=5'
    
    const res = await fetch(url);
    const foundAddresses = res.json();
    
    return foundAddresses
}


async function makeAdressList () {
    
    const inputApi = document.getElementById('api-gouv');
    const apiContainer = document.getElementById('api-container');
    const addressContainer=document.getElementById('address-container');
    
    
    
    inputApi.addEventListener('keyup', async (event)=> {
        
        if(inputApi.value.length>3)
        {
            const adresses = await gouvApiCall(inputApi.value);
            
            addressContainer.textContent='';
            
            
            adresses.features.forEach((address,i) => {
                
                const addressBox = document.createElement('div');
                addressBox.classList.add('text-sm', 'p-2','hover:bg-accents1', 'hover:text-fond');
                addressBox.role='listitem';
                
                addressBox.addEventListener('click', ()=> {
                    
                    formFiller(address);
                    addressContainer.textContent='';
                    
                })
                
                
                
                const addressText = document.createElement('p');
                addressText.innerText=`${address.properties.label}`;
                
                addressBox.appendChild(addressText);
                addressContainer.appendChild(addressBox);
            });
            
        }
        
        
        
        
    })
    
    
    document.addEventListener('click', (event) =>{
        
        if (!apiContainer.contains(event.target)&& !addressContainer.contains(event.target)) {

            addressContainer.textContent='';
        }
        
    })
}


function formFiller (address) {
    
    const inputStreet = document.getElementById('rue');
    inputStreet.value=address.properties.name;
    const inputCity = document.getElementById('commune');
    inputCity.value=address.properties.city;
    const inputZipCode = document.getElementById('code_postal');
    inputZipCode.value=address.properties.postcode;
    
    
}