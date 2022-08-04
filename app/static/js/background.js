var select = document.querySelector('select');
var html = document.querySelector('body');
//html.style.backgroundRepeat no-repeat;
//html.style.background cover

//select.addEventListener('change', background);

const dicts = {
    "spongebob": [
        "static/img/CardIcons/Sandys_Rocket_Gallery_(64).jpg",
        "Spongebob",
        "https://www.kaggle.com/datasets/mikhailgaerlan/spongebob-squarepants-completed-transcripts"
    ],
    "ferb": [
        "static/img/CardIcons/62314d426115a19ebb4ad0a0694c1ad2.png",
        "Phineas and Ferb",
        "https://phineasandferb.fandom.com/wiki/Phineas_and_Ferb_Wiki"
    ],
    "harry": [
        "static/img/CardIcons/maxresdefault.jpg",
        "Harry Potter",
        "https://www.kaggle.com/datasets/balabaskar/harry-potter-books-corpora-part-1-7",
    ],
    "unfortunate": [
        "static/img/CardIcons/ad4x-square-1536.jpg",
        "A Series of Unfortunate Events",
        "https://readsnovelonline.com/bk/BookListBySeries?sid=3770"
    ]
}

function background(val){
    var choice = val;//select.value;
    var section = document.getElementById('about')

    var card = document.getElementById('corpus-card');

    if(choice === "ferb"){
        section.style.backgroundImage = "url('https://tvcdn.fancaps.net/1352767.jpg')"
        section.style.backgroundSize = "cover"
    }

    else if(choice === "spongebob"){
        section.style.backgroundImage = "url('https://wallpaperboat.com/wp-content/uploads/2020/04/spongebob-and-patrick-wallpaper-1920x1080-24.jpg')"
        section.style.backgroundSize = "cover"
    }

    else if(choice === "harry"){
        section.style.backgroundImage = "url('https://wallpaperaccess.com/full/22917.jpg')"
        section.style.backgroundSize = "cover"
    }

    else if(choice === "unfortunate"){
        section.style.backgroundImage = "url('https://images.metadata.sky.com/pd-image/d4b2ed44-6e51-4731-8575-50db6c5bb2cd/16-9')"
        section.style.backgroundSize = "cover"
    }

    card.children[0].src = dicts[choice][0];
    card.children[1].children[0].innerHTML = dicts[choice][1];
    card.children[1].children[2].href = dicts[choice][2];
}