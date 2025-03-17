let i = 0;

const precedent = document.getElementById('previous');
const suivant = document.getElementById('next');
const carouselPics = document.querySelectorAll('.carousel-img');

if (window.innerWidth < 768 ) {
  carouselPics[0].classList.toggle('hidden');

  suivant.addEventListener('click', getOneNextPic);
  suivant.addEventListener("keydown", function(e) {
    if(e.key==13){
      getOneNextPic()
    }
  });

  function getOneNextPic() {
    const carouselPics = document.querySelectorAll('.carousel-img');
    if (i < carouselPics.length - 1) {
      carouselPics[i].classList.toggle('hidden');
      carouselPics[i+1].classList.toggle('hidden');
      i++;   
    };
  }

  precedent.addEventListener('click', getOnePreviousPic);
  precedent.addEventListener("keydown", function(e) {
    if(e.key==13){
      getOnePreviousPic()
    }
  });

  function getOnePreviousPic() {
    const carouselPics = document.querySelectorAll('.carousel-img');
    if (i > 0) {
      carouselPics[i].classList.toggle('hidden');
      carouselPics[i-1].classList.toggle('hidden');
      i--;   
    };  
  };
} else {
  carouselPics[0].classList.toggle('hidden');
  carouselPics[1].classList.toggle('hidden');
  carouselPics[2].classList.toggle('hidden');

  suivant.addEventListener('click', getThreeNextPic);
  suivant.addEventListener("keydown", function(e) {
    if(e.key==13){
      getThreeNextPic()
      }
  });

  function getThreeNextPic() {
    const carouselPics = document.querySelectorAll('.carousel-img');
    if (i < carouselPics.length - 3) {
      carouselPics[i].classList.toggle('hidden');
      carouselPics[i+3].classList.toggle('hidden');
      i++;   
    };
  }

  precedent.addEventListener('click', getThreePreviousPic);
  precedent.addEventListener("keydown", function(e) {
    if(e.key==13){
      getThreePreviousPic()
      }
  });

  function getThreePreviousPic() {
    const carouselPics = document.querySelectorAll('.carousel-img');
    if (i > 0) {
      carouselPics[i+2].classList.toggle('hidden');
      carouselPics[i-1].classList.toggle('hidden');
      i--;   
    }; 
  };
}
