document.addEventListener('DOMContentLoaded',() =>{

    tableToggleCollapse();
})

function tableToggleCollapse() {
    
    const rows = document.querySelectorAll('.view');

    rows.forEach(row => row.addEventListener('click', showDetails));

    rows.forEach(row => {
        row.addEventListener("keydown", function(e) {
            if(e.keyCode==13){
              showDetails(row);
             }
          })
      });

    function showDetails(e) {
        //* If clicked : row is e(vent).currentTarget ; if Enter is pressed : row is e(vent)
        let fold = (e.currentTarget) ? e.currentTarget : e;
        const foldNode = fold.nextSibling.nextSibling;
        foldNode.classList.toggle('hidden');
    }
}