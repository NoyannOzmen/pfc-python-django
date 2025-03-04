const shortSearch = document.getElementById('fullSearch');
const filters = document.getElementById('searchCriterias');

const deployButton = document.getElementById('deploy');

deployButton.addEventListener("click", deploySearch);
deployButton.addEventListener("keydown", function(e) {
  if(e.key==13){
    deploySearch();
   }
})

function deploySearch() {
  shortSearch.classList.toggle('hidden');
  filters.classList.toggle('hidden');
}