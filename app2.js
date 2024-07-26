document.addEventListener('DOMContentLoaded', function() {
    const boton = document.querySelector('.cambiar-chino');
    const textElement = document.getElementById('text-content2');

    const textoIngles = `
        Dear Sally,
        <br>
        <br>
        Today, we find ourselves in a beautiful place, celebrating the wonder of being together, and tomorrow marks one month since our lives intertwined in a way I can only describe as magical. In this short time, you have transformed my world in ways I never thought possible, and I want to take a moment to remind you just how fantastic you are.
        <br>
        <br>
        From the first moment I met you, I knew I had found someone special. You are like a beacon of light in the darkness, guiding me and giving me hope on the darkest days. Your smile, radiant and genuine, has the power to light up any room, and your laughter, so contagious and pure, could warm the coldest heart.
        <br>
        There is an innate beauty in you, a grace that transcends the physical and touches the soul. It’s not just your beautiful face or your deep, captivating eyes, but the way you carry yourself with silent strength and unwavering determination. Every day, you inspire me with your courage and your ability to face any challenge life throws at you.
        <br>
        <br>
        But beyond that strength, there is a sweetness in you that I adore. You are kind, generous, and always willing to give your best. Your words have the power to comfort and heal, and your presence is like a balm to my restless spirit.
        <br>
        <br>
        I trust you with all my being because I know that behind those vibrant eyes lies a heart beating with love and compassion. You are the reason I believe in goodness and the possibility of true love. You’ve shown me that happiness is not a destination but a journey, and I feel incredibly lucky to be on this journey with you.
        <br>
        <br>
        I want you to know that I see you, I truly see you. I see your achievements and your struggles, your dreams and your fears. And in each of those aspects, I see a person worthy of all the love and happiness in the world. You are incredibly strong, but you are also human, and that is what makes you so extraordinary.
        <br>
        <br>
        Every moment with you is a gift I treasure deeply. From deep conversations to shared laughter, from comfortable silences to moments of vulnerability. You have awakened in me a part I thought I had lost long ago: my inner child. With you, I can be genuine, without masks or pretenses, and that is something I will be eternally grateful for.
        <br>
        <br>
        I want you to know that I will always be here for you, supporting you and loving you unconditionally. You are my muse, my love, my best friend. No matter what the future holds for us, I am committed to making each day a reflection of the joy and love we share.
        <br>
        <br>
        So, on the eve of our first month together, I want to thank you for being exactly who you are. You are beautiful, not just on the outside, but in every corner of your being. You have a light that cannot be extinguished, a strength that cannot be broken, and a love that is infinitely deep.
        <br>
        <br>
        I love you more than words can express, and I am eager to see what wonders the coming months and years will bring. You are my everything, and you always will be.
        <br>
        <br>
        With all my love,
        <br>
        <br>
        Samuel.
    `;

    const textoChino = `
        亲爱的 Sally，
        <br>
        <br>
        今天，我们在美好的时光中相聚，庆祝着彼此的奇妙相遇，明天将是我们在一起一个月的纪念日。在这段短暂的时间里，你已以一种我从未想过的方式改变了我的世界，我想借此机会提醒你，你是多么的了不起。
        <br>
        <br>
        从我第一次见到你时，我就知道我找到了一个特别的人。你就像黑暗中的一束光，指引着我，给我希望。你的微笑，如此光辉而真挚，能点亮任何房间，你的笑声，如此传染且纯粹，能够温暖最冰冷的心灵。
        <br>
        你的美丽不仅仅在于外表，更多地体现在你那份优雅的气质和坚定不移的决心上。每天，你都以你的勇气和应对生活挑战的能力激励着我。
        <br>
        <br>
        然而，除了那种力量，你还有一种我非常珍爱的甜美。你善良、慷慨，总是愿意付出最好的自己。你的话语有安慰和治愈的力量，你的存在是我不安灵魂的良药。
        <br>
        <br>
        我完全信任你，因为我知道在你那双充满活力的眼睛背后，是一个充满爱与同情的心。你是我相信美好和真爱的理由。你让我相信，幸福不是一个终点，而是一段旅程，我感到无比幸运能与你一同踏上这段旅程。
        <br>
        <br>
        我希望你知道，我看到你的一切，看到你的成就和挣扎，看到你的梦想和恐惧。在这些方面，我看到一个值得拥有世界上所有爱与幸福的人。你非常坚强，但你也是人，这使你变得如此非凡。
        <br>
        <br>
        每一刻与你在一起都是我珍惜的礼物。从深入的交谈到共享的欢笑，从舒适的沉默到脆弱的时刻。你唤醒了我以为早已失去的部分：我内心的孩子。与你在一起，我可以做真实的自己，不用戴面具或伪装，这让我非常感激。
        <br>
        <br>
        我想让你知道，我将永远支持你，毫无条件地爱着你。你是我的灵感，我的爱，我最好的朋友。无论未来会带来什么，我都致力于让每一天都反映出我们分享的快乐和爱。
        <br>
        <br>
        所以，在我们一起的第一个月即将来临之际，我想感谢你做你自己。你是美丽的，不仅仅在外表上，而是在你整个存在的每一个角落。你拥有一种无法熄灭的光芒，一种无法破碎的力量，以及一种深不可测的爱。
        <br>
        <br>
        我爱你超过言语所能表达的，我迫不及待地想看看未来的几个月和几年会带来什么奇迹。你是我的一切，永远是。
        <br>
        <br>
        用我所有的爱，
        <br>
        <br>
        Samuel.
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
