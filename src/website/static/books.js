// books.js
const books = [
    {
        bookId: "1",
        title: "To Kill a Mockingbird",
        author: "Harper Lee",
        cover: "https://m.media-amazon.com/images/I/81gepf1eMqL._AC_UF1000,1000_QL80_.jpg",
        description: "In the racially charged South, Scout Finch narrates her coming-of-age story alongsbookIde her brother Jem. Their wbookIdowed father, Atticus, is a lawyer defending a black man wrongly accused of assault, exposing the children to the town's deep-rooted prejudices and the importance of compassion and justice.",
        genres: ["Southern Gothic", "Legal Drama"],

    },
    {
        bookId: "2",
        title: "The Hitchhiker's GubookIde to the Galaxy",
        author: "Douglas Adams",
        cover: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNad4-0rUdke9G4vbX9sK9KFnWd5Ul0W3Jgw&s", 
        description: "Earthman Arthur Dent narrowly escapes the destruction of his home planet by hitching a rbookIde on a Vogon spaceship with his friend Ford Prefect, who reveals himself to be an alien researcher for the titular Hitchhiker's GubookIde to the Galaxy. They embark on a zany interstellar journey aboard the stolen spaceship Heart of Gold, encountering eccentric characters like two-headed galactic presbookIdent Zaphod Beeblebrox, the depressed robot Marvin, and Trillian, the woman Arthur once tried to pick up at a party. Their adventures lead them to the answer to the ultimate question of life, the universe, and everything, which turns out to be 42, but the question itself remains elusive.", 
        genres: ["Science Fiction", "Humor"],

    },
    {
        bookId: "3",
        title: "The Great Gatsby",
        author: "F. Scott Fitzgerald",
        cover: "https://cdn.kobo.com/book-images/5addc4c9-fbc1-42d7-a79f-cec7619d4b23/1200/1200/False/the-great-gatsby-a-novel-1.jpg",  
        description: "In the roaring 1920s, Nick Carraway, a MbookIdwesterner who moves to Long Island, becomes fascinated by his wealthy and enigmatic neighbor, Jay Gatsby. Gatsby throws extravagant parties, hoping to reunite with his lost love, Daisy Buchanan, who is married to the brutish Tom Buchanan. Nick gets drawn into their world of luxury, obsession, and ultimately, tragedy, as Gatsby's pursuit of the American Dream leads to devastating consequences.", 
        genres: ["Tragedy"],

    },
    {
        bookId: "4",
        title: "Dune",
        author: "Frank herbert",
        cover: "https://m.media-amazon.com/images/I/81nq+ewtkcL._AC_UF1000,1000_QL80_.jpg",  
        description: "On the desert planet Arrakis, the sole source of the valuable spice melange, young Paul AtrebookIdes and his family become embroiled in a treacherous power struggle after being entrusted with the planet's stewardship. Betrayed and left for dead, Paul finds refuge with the native Fremen, eventually embracing his destiny as their messianic leader, Muad'Dib, to avenge his family and reclaim control of Arrakis.",
        genres: ["Science Fiction"],
        
    },
    {
        bookId: "5",
        title: "Ready Player One",
        author: "Ernest Cline",
        cover: "https://m.media-amazon.com/images/I/91FGDm7MfIL._AC_UF1000,1000_QL80_.jpg",  
        description: "In a dystopian 2045, teenager Wade Watts escapes the bleak reality of his life by immersing himself in the virtual world of OASIS. When the creator of OASIS dies, he leaves a series of puzzles and challenges within the game, promising his vast fortune and control of OASIS to the winner. Wade joins the global race to find the keys, battling both virtual adversaries and a powerful corporation determined to seize the prize for themselves.",
        genres: ["Science Fiction","Action"],

    },
    {
        bookId: "6",
        title: "Minecraft Redstone Handbook",
        author: "Mojang AB",
        cover: "https://m.media-amazon.com/images/I/617dLkzb9-L._AC_UF1000,1000_QL80_.jpg",  
        description: "Minecraft: Redstone Handbook is an official gubookIdebook that delves into the intricate world of redstone, a versatile in-game resource used for building complex contraptions and mechanisms. It teaches players how to harness the power of redstone to create automatic doors, intricate circuits, hbookIdden traps, and even simple computers within the Minecraft universe.",
        genres: ["Non-Fiction","GubookIde"],
        
    },
    {
        bookId: "7",
        title: "Minecraft Beginners Handbook",
        author: "Mojang AB",
        cover: "https://m.media-amazon.com/images/I/81nbtKexVUL._AC_UF1000,1000_QL80_.jpg",  
        description: "Minecraft: Beginners GubookIde is an official gubookIdebook offering essential tips and strategies for thriving in the Minecraft world. It covers everything from basic survival skills like gathering resources, building shelters, and crafting tools to advanced techniques for farming, exploring, combatting hostile mobs, and navigating different biomes. The gubookIde aims to help players of all levels master the challenges of survival in the blocky universe of Minecraft.",
        genres: ["Non-Fiction","GubookIde"],
        
    },
    {
        bookId: "8",
        title: "Minecraft Construction Handbook",
        author: "Mojang AB",
        cover: "https://m.media-amazon.com/images/I/612HfenZf0L._AC_UF1000,1000_QL80_.jpg",  
        description: "Minecraft: Construction Handbook is an official gubookIdebook that provbookIdes players with creative inspiration and practical tips for building impressive structures in the Minecraft world. It covers a wbookIde range of construction projects, from simple houses and farms to elaborate castles and underwater cities. The handbook includes detailed instructions, step-by-step diagrams, and valuable advice on choosing materials, planning layouts, and incorporating redstone mechanisms. Whether you're a beginner builder or a seasoned architect, this handbook will help you unleash your creativity and build amazing creations in Minecraft.",
        genres: ["Non-Fiction","GubookIde"],
        
    },
    {
        bookId: "9",
        title: "Minecraft Combat Handbook",
        author: "Mojang AB",
        cover: "https://m.media-amazon.com/images/I/61qSsRBSo6L._AC_UF1000,1000_QL80_.jpg",  
        description: "Synopsis: Minecraft: Combat Handbook is an official gubookIdebook that equips players with the knowledge and skills needed to survive and thrive in the dangerous world of Minecraft. It covers a wbookIde range of combat-related topics.",
        genres: ["Non-Fiction","GubookIde"],

    },
    {
        bookId: "10",
        title: "Thinking Fast Thinking Slow",
        author: "Daniel Kahneman",
        cover: "https://m.media-amazon.com/images/I/61fdrEuPJwL._AC_UF1000,1000_QL80_.jpg",  
        description: "Thinking, Fast and Slow explores the two systems that drive the way we think and make decisions: System 1 is fast, intuitive, and emotional; System 2 is slower, more deliberative, and more logical. Kahneman reveals the biases and flaws in our intuitive thinking, showing how these can lead to irrational choices. He offers practical insights on how to recognize and overcome these biases, leading to better decision-making in our personal and professional lives.",
        genres: ["Non-Fiction","Psychology"],

    },
    {
        bookId: "11",
        title: "Surrounded by bookIdiots",
        author: "Thomas Erikson",
        cover: "https://bci.kinokuniya.com/jsp/images/book-img/97817/97817850/9781785042188.JPG",  
        description: "Surrounded by bookIdiots introduces a model of four distinct personality types based on colors (Red, Yellow, Green, and Blue), each with different communication styles, motivations, and behaviors. The book provbookIdes insights and practical tips on how to bookIdentify these types in others and adjust your communication style accordingly to improve interactions in both personal and professional relationships.",
        genres: ["Non-Fiction","Self-Help"],

    },
    {
        bookId: "12",
        title: "The Subtle Art of Not Giving a Fuck",
        author: "Mark Manson",
        cover: "https://m.media-amazon.com/images/I/71QKQ9mwV7L._AC_UF1000,1000_QL80_.jpg",  
        description: "The Subtle Art of Not Giving a F*ck challenges traditional self-help advice and encourages readers to embrace their limitations and imperfections. It argues that true happiness comes not from chasing positive experiences, but from choosing what to care about and accepting life's inevitable struggles. Through humorous anecdotes and blunt honesty, Manson offers a refreshing perspective on finding meaning and fulfillment in a world that constantly tells us to strive for more.",
        genres: ["Non-Fiction","Self-Help"],
        
    },
    {
        bookId: "13",
        title: "Ikigai",
        author: "Hector Garcia and Francesc Miralles",
        cover: "https://m.media-amazon.com/images/I/81l3rZK4lnL._AC_UF1000,1000_QL80_.jpg",  
        description: "Ikigai explores the Japanese concept of 'ikigai', a term often translated as 'reason for being' or 'reason to get up in the morning'. The book delves into the lifestyle and philosophy of centenarians in Okinawa, Japan, known for their longevity and happiness. It uncovers the secrets to their fulfilling lives, highlighting the importance of finding purpose, staying active, nourishing social connections, and embracing simple joys. Ikigai offers practical tips and insights on how to discover and cultivate your own ikigai to lead a more meaningful and fulfilling life.",
        genres: ["Non-Fiction","Self-Help"],

    },
    {
        bookId: "14",
        title: "The Art Of War",
        author: "Sun Tzu",
        cover: "https://jamesclear.com/wp-content/uploads/2015/11/TheArtofWar-by-SunTzu.jpg",  
        description: "The Art of War is an ancient Chinese treatise on military strategy and tactics. It emphasizes the importance of knowing oneself and one's enemy, using deception and cunning to gain advantage, and winning wars through careful planning and positioning rather than brute force. Its teachings have been influential in military, business, and personal development contexts for centuries.",
        genres: ["Non-Fiction","GubookIde","Self-Help"],
        
    },
    {
        bookId: "666",
        title: "The Death Note",
        author: "Shinigami",
        cover: "https://m.media-amazon.com/images/I/31r7n1DIUFL._AC_UF1000,1000_QL80_.jpg",  
        description: `1. The human whose name is written in this note shall die.
        2. This note will not take effect unless the writer has the person's face in their mind when writing his/her name.
        3. If the cause of death is written within 40 seconds of writing the person's name, it will happen.
        4. After writing the cause of death, details of the death should be written in the next 6 minutes and 40 seconds.
        5. This note shall become the property of the human world, once it touches the ground of (arrives in) the human world.
        6. The owner of the note can recognize the image and voice of the original owner, i.e., a god of death.
        7. The human who uses this note can neither go to Heaven nor Hell.`,
        genres: ["Mystery","Thriller"],
    }
];

export default books;
