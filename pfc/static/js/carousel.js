let i = 0;

const slideShow = document.getElementById('animal-carousel');
const precedent = document.getElementById('previous');
const suivant = document.getElementById('next');

const carouselPics = document.querySelectorAll('.carousel-img');
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

/*Display 3 cards for deskstop*/

const slideShow3 = document.getElementById('animal-carousel3');
const precedent3 = document.getElementById('previous3');
const suivant3 = document.getElementById('next3');

const carouselPics3 = document.querySelectorAll('.carousel3-img');
carouselPics3[0].classList.toggle('hidden');
carouselPics3[1].classList.toggle('hidden');
carouselPics3[2].classList.toggle('hidden');

suivant3.addEventListener('click', getThreeNextPic);
suivant3.addEventListener("keydown", function(e) {
  if(e.key==13){
    getThreeNextPic()
    }
});

function getThreeNextPic() {
  const carouselPics3 = document.querySelectorAll('.carousel3-img');
  if (i < carouselPics3.length - 3) {
    carouselPics3[i].classList.toggle('hidden');
    carouselPics3[i+3].classList.toggle('hidden');
    i++;   
  };
}

precedent3.addEventListener('click', getThreePreviousPic);
precedent3.addEventListener("keydown", function(e) {
  if(e.key==13){
    getThreePreviousPic()
    }
});

function getThreePreviousPic() {
  const carouselPics3 = document.querySelectorAll('.carousel3-img');
  if (i > 0) {
    carouselPics3[i+2].classList.toggle('hidden');
    carouselPics3[i-1].classList.toggle('hidden');
    i--;   
  }; 
};
