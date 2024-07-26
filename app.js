const overlay = document.querySelector('.overlay');
const title = document.querySelector('.title');
const subtitle = document.querySelector('.subtitle');
const text = document.querySelector('.text');
const moon = document.querySelector('.moon');
const pizza = document.querySelector('.pizza');
const boton = document.querySelector('.boton');
const noodles = document.querySelector('.noodles');

TweenMax.from(title, {
  duration: 2,
  y: 100,
  opacity: 0,
});

TweenMax.to(title, {
  delay: 4,
  duration: 2,
  y: -100,
  opacity: 0,
});

TweenMax.from(subtitle, {
  delay: 4,
  duration: 2,
  y: 100,
  opacity: 0,
});

TweenMax.to(subtitle, {
  delay: 8,
  duration: 2,
  y: -100,
  opacity: 0,
});

TweenMax.from(moon, {
  delay: 4,
  duration: 2,
  x: -100,
  opacity: 0,
});

TweenMax.from(noodles, {
  delay: 4,
  duration: 2,
  x: -100,
  opacity: 0,
});

TweenMax.from(text, {
  delay: 8,
  duration: 2,
  y: 100,
  opacity: 0,
});

TweenMax.to(text, {
  delay: 12,
  duration: 2,
  y: -100,
  opacity: 0,
});

TweenMax.from(pizza, {
  delay: 8,
  duration: 2,
  x: 100,
  opacity: 0,
});

TweenMax.to(overlay, {
  delay: 12,
  duration: 2,
  y: '-100%',
});

// Hide video controls when mouse is inactive
const video = document.getElementById('video');
let timeout;

document.addEventListener('mousemove', function() {
    video.controls = true;
    clearTimeout(timeout);
    timeout = setTimeout(function() {
        video.controls = false;
    }, 3000);
});

video.addEventListener('click', function() {
    video.controls = true;
});

// Add images to photo grids
const samirPhotos = [
    'img/samir/1.jpg', 'img/samir/2.jpg', 'img/samir/3.jpg',
    'img/samir/4.jpg', 'img/samir/5.jpg'
];

const sallyPhotos = [
    'img/sally/1.jpg', 'img/sally/2.png', 'img/sally/3.png',
    'img/sally/4.png', 'img/sally/5.png'
];

const samirContainer = document.getElementById('samir-photos');
const sallyContainer = document.getElementById('sally-photos');

function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

shuffle(samirPhotos);
shuffle(sallyPhotos);

function getRandomPositionSamir(containerRect, videoRect) {
    const x = Math.random() * (videoRect.left - containerRect.left - 80); // Avoid overlapping the video
    const y = Math.random() * (containerRect.height - 80); // Ensure images stay within the height of the container
    return { x, y };
}

function getRandomPositionSally(containerRect, videoRect) {
    const x = Math.random() * (containerRect.width - videoRect.right - 80); // Avoid overlapping the video
    const y = Math.random() * (containerRect.height - 80); // Ensure images stay within the height of the container
    return { x: videoRect.right + x, y }; // Position Sally's images to the right of the video
}

window.onload = function() {
    const container = document.querySelector('.content-images');
    const containerRect = container.getBoundingClientRect();
    const videoRect = video.getBoundingClientRect();

    samirPhotos.forEach(src => {
        const img = document.createElement('img');
        img.src = src;
        img.className = 'samir-photo';
        img.style.transform = `rotate(${Math.floor(Math.random() * 20 - 10)}deg)`;

        const { x, y } = getRandomPositionSamir(containerRect, videoRect);
        img.style.position = 'absolute';
        img.style.left = `${x}px`;
        img.style.top = `${y}px`;

        samirContainer.appendChild(img);
    });

    sallyPhotos.forEach(src => {
        const containerDiv = document.createElement('div');
        containerDiv.className = 'sally-photo-container';
        containerDiv.style.position = 'absolute';

        const { x, y } = getRandomPositionSally(containerRect, videoRect);
        containerDiv.style.left = `${x}px`;
        containerDiv.style.top = `${y}px`;

        const img = document.createElement('img');
        img.src = src;
        img.className = 'sally-photo';
        img.style.transform = `rotate(${Math.floor(Math.random() * 20 - 10)}deg)`;

        const heart = document.createElement('div');
        heart.className = 'sally-heart';
        heart.textContent = "❤️"; // Insert heart emoji

        containerDiv.appendChild(img);
        containerDiv.appendChild(heart);
        sallyContainer.appendChild(containerDiv);
    });
};

document.addEventListener('DOMContentLoaded', function() {
  const boton = document.querySelector('.cambiar-chino');
  const textElement = document.getElementById('text-content');

  const textoIngles = `
      Hello, my love.
      <br>
      I hope you have an amazing day today and that every time you watch this video, it can bring a smile to your face and make you feel much better.
      <br>
      I want to express to you how much it means to me that you're with me, how much you mean to me.
      <br>
      Since I met you in that game, I've felt a strong connection with you. From the first moment you spoke to me, I felt that you were an excellent person, and the truth is that I wasn't wrong.
      <br>
      <br>
      All the time I've spent with you has been as valuable as it has been meaningful to me. Everything has been so beautiful and satisfying that I want to feel this for my whole life... I feel that if I hadn't met you that day, my life would still be gray and dull. Everything I did would still be meaningless; everything would be boring and common to me. But here you are, giving me beautiful moments and lessons to nourish me with everything you leave behind, making me laugh and turning gray days into better ones, bringing me happiness and harmony both together and alone, making me know that I can always improve in things and be a better person, a better boyfriend and friend, a better family member and a good companion.
      <br>
      <br>
      Thank you for appearing in my life, thank you for provoking the best sensations in me that want to surface every time they appear, thank you for not letting me die alone in a world full of ashes everywhere, thank you for easing the pains and accompanying me in moments of bitterness even if you don't know it, thank you for being the best girlfriend I could have, for giving me details that no one had ever given me, for being so strong and resilient after all the problems we've had, for teaching me that love has no limits and that with love everything is possible, thank you for being so you, for teaching me a bit about your past, for making me understand that my little girl needs so much pure and true love, a special love, that surpasses the barriers of the normal and transcends the cruel truths and the pressures of society.
  `;

  const textoChino = `
      亲爱的，
      <br>
      我希望你今天过得非常美好，每次你看到这个视频时，都能让你露出笑容，让你感觉更好。
      <br>
      我想表达的是，你和我在一起对我来说意义重大，你对我来说真的非常重要。
      <br>
      从我在那次游戏中认识你开始，我就感受到了与你之间的强烈连接。从你第一次和我说话时，我就感觉到你是一个非常优秀的人，事实证明我没有错。
      <br>
      <br>
      我和你在一起的所有时间对我来说都是如此宝贵和有意义。一切都如此美丽和令人满意，我希望这种感觉能伴随我一生。我觉得如果那天我没有认识你，我的生活现在可能还是灰暗和无趣。我做的每一件事都可能没有意义，一切对我来说都将是乏味和平淡的。但你在这里，给了我美好的时光和经验，让我从中汲取养分，让我笑容满面，把灰暗的日子变得更加美好，带给我幸福与和谐，无论我们在一起还是分开，让我知道我可以不断进步，成为一个更好的人、更好的男朋友和朋友、更好的家人以及更好的伴侣。
      <br>
      <br>
      我记得我们的第一次约会，我有多么紧张，而你用你的微笑和温暖的话语让我感到轻松。正是那一刻，我知道我想要与你共度更多时光，更好地了解你，建立一种特别的关系。
      <br>
      感谢你出现在我的生活中，感谢你激发了我内心的美好感受，让它们每次浮现出来时都让我感到愉快，感谢你没有让我在一个满是灰烬的世界里孤单地生活，感谢你在我痛苦的时候给予我安慰，即使你可能不知道，感谢你成为我最好的女朋友，给我之前没人给予的细节，感谢你在我们经历过的所有问题后仍然如此坚强和富有韧性，感谢你教会我爱是没有界限的，爱能让一切变得可能，感谢你做你自己，教会我一点你的过去，让我明白我的小女孩需要如此纯真和真实的爱，一种特殊的爱，超越了常规的界限，超越了残酷的现实和社会的压力。
  `;

  // Variable to keep track of the current language
  let isChinese = false;

  boton.addEventListener('click', function() {
      if (isChinese) {
          textElement.innerHTML = textoIngles;
      } else {
          textElement.innerHTML = textoChino;
      }
      isChinese = !isChinese; // Toggle the language
  });
});



