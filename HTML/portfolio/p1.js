// let sections = document.querySelectorAll('section');
// let navLinks = document.querySelectorAll('header nav a'); 

// window.onscroll =()=> {
//     sections.forEach(sec => {
//         let top = window.unescapescrollY;
//         let offset = sec.offsetTop - 150;
//         let hight = sec.offsetHeight;
//         let id = sec.getAttribute('id');

//         if(top >= offset && top < offset + hight) {
//             navLinks.forEach(links =>{
//                 links.classlist.remove('active');
//                 document.querySelector('header anv a[href*=' +id+']').classList.add('active');
//             });
//         };
//     });
// };