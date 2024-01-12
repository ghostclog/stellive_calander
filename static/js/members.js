let kanna = document.querySelector('#kanna');
let yuni = document.querySelector('#yuni');
let shiro = document.querySelector('#shiro');
let hina = document.querySelector('#hina');
let lize = document.querySelector('#lize');
let tabi = document.querySelector('#tabi');

const moveMember = (stella_name) => {
    window.location.href = '/mains/' + stella_name;
}

kanna.addEventListener('click',() => moveMember('kanna'));
yuni.addEventListener('click',() => moveMember('yuni'));
shiro.addEventListener('click',() => moveMember('shiro'));
hina.addEventListener('click',() => moveMember('hina'));
lize.addEventListener('click',() => moveMember('lize'));
tabi.addEventListener('click',() => moveMember('tabi'));