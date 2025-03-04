document.addEventListener('DOMContentLoaded', ()=>{
    handleFilters();
    handlesSearchBar();

    dropDownSearch();
});

function filterCards (searchFlag,animalCards) {

    const speciesFilter = [];
    const speciesCheckboxes = document.querySelectorAll('.species-checkbox');
    speciesCheckboxes.forEach(species => {
        if (species.checked) {
            speciesFilter.push(species.value)
        }
    });
    
    const statutFilter = [];
    const statutCheckboxes = document.querySelectorAll('.statut-checkbox');
    statutCheckboxes.forEach(statut => {
        if (statut.checked) {
            statutFilter.push(statut.value)
        }
    });
    
    const searchBar = document.getElementById('search-bar');
    
    const selectedCards = Array.from(animalCards).filter(animalCard => {
        
        const searchArray = 
        [
            animalCard.dataset.nom.toLowerCase(),
            animalCard.dataset.statut.toLowerCase(),
            animalCard.querySelector('.espece-nom').innerText.toLowerCase()
        ]
        
        
        const F1 = speciesFilter.length ? speciesFilter.includes(animalCard.dataset.espece) : true;
        const F2 = statutFilter.length ? statutFilter.includes(animalCard.dataset.statut) : true;
        const F3 = searchArray.some(e => {return e.includes(searchBar.value.toLowerCase())});
        
        
        if (!searchFlag) {
            return (F1&&F2)
        } else {
            return (F1&&F2&&F3)
        };
        
    });
    
    return selectedCards
    
}

function handleFilters () {
    
    const checkboxes = document.querySelectorAll('.checkbox');
    
    checkboxes.forEach(checkbox => {
        
        checkbox.addEventListener('change', (event) => {
            
            if (event.target.classList.contains('species-checkbox') ) {
                const allSpeciesCheckbox = document.getElementById('espece_all');
                allSpeciesCheckbox.checked=false
            }
            const allStatutCheckbox = document.getElementById('statut_all');
            if (event.target.classList.contains('statut-checkbox') ) {
                allStatutCheckbox.checked=false
            }
            
            const animalCards =  document.querySelectorAll('.animal_card');
            animalCards.forEach(animalCard => {
                animalCard.classList.add('hidden');
            });
            const searchFlag = document.getElementById('search-bar').value.length>3
            
            const visibleCards = filterCards(searchFlag, animalCards);
            
            visibleCards.forEach(visibleCard => {
                visibleCard.classList.remove('hidden');
            });
        })
        
    });
    
    const allSpeciesCheckbox = document.getElementById('espece_all');
    allSpeciesCheckbox.addEventListener('change', () => {
        
        const speciesCheckboxes = document.querySelectorAll('.species-checkbox');
        
        speciesCheckboxes.forEach(checkbox => {
            checkbox.checked=false
        });
        
        const statutFilter = [];
        const statutCheckboxes = document.querySelectorAll('.statut-checkbox');
        statutCheckboxes.forEach(statut => {
            if (statut.checked) {
                statutFilter.push(statut.value)
            }
        });
        
        const animalCards =  document.querySelectorAll('.animal_card');
        animalCards.forEach(animalCard => {
            
            animalCard.classList.add('hidden');
        });
        
        const visibleCards = Array.from(animalCards).filter(animalCard => {
            
            const F2 = statutFilter.length ? statutFilter.includes(animalCard.dataset.statut) : true;
            return F2
            
        })
        
        visibleCards.forEach(visibleCard => {
            visibleCard.classList.remove('hidden');
        });
        
        
    })
    
    const allStatutCheckbox = document.getElementById('statut_all');
    allStatutCheckbox.addEventListener('change', () => {
        
        const statutCheckboxes = document.querySelectorAll('.statut-checkbox');
        
        statutCheckboxes.forEach(checkbox => {
            checkbox.checked=false
        });
        
        const speciesFilter = [];
        const speciesCheckboxes = document.querySelectorAll('.species-checkbox');
        speciesCheckboxes.forEach(species => {
            if (species.checked) {
                speciesFilter.push(species.value)
            }
        });
        
        const animalCards =  document.querySelectorAll('.animal_card');
        animalCards.forEach(animalCard => {
            
            animalCard.classList.add('hidden');
        });
        
        const visibleCards = Array.from(animalCards).filter(animalCard => {
            
            const F2 = speciesFilter.length ? speciesFilter.includes(animalCard.dataset.espece) : true;
            return F2
            
        })
        
        visibleCards.forEach(visibleCard => {
            visibleCard.classList.remove('hidden');
        });
        
        
    })
    
}

function handlesSearchBar () {
    
    const searchBar = document.getElementById('search-bar');
    
    searchBar.addEventListener('input', () => {
        
        const animalCards =  document.querySelectorAll('.animal_card');
        animalCards.forEach(animalCard => {
            animalCard.classList.add('hidden');
        });
        const searchFlag = document.getElementById('search-bar').value.length>3
        
        const visibleCards = filterCards(searchFlag, animalCards);
        
        visibleCards.forEach(visibleCard => {
            visibleCard.classList.remove('hidden');
        });
        
    })
    
}

function dropDownSearch () {
    const searchButton = document.getElementById('search-dropdown-button');
    
    searchButton.addEventListener('click', ()=>{
        const searchFilters = document.getElementById('search-filters');
        searchFilters.classList.toggle('hidden')
    })
}
