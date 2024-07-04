// books.js
const books = [
    {
        title: "To Kill a Mockingbird",
        author: "Harper Lee",
        cover: "./data/book_covers/Mockingbird.jpg",
        description: "In the racially charged South, Scout Finch narrates her coming-of-age story alongside her brother Jem. Their widowed father, Atticus, is a lawyer defending a black man wrongly accused of assault, exposing the children to the town's deep-rooted prejudices and the importance of compassion and justice.",
        genres: ["Southern Gothic", "Legal Drama"],
        availability: ["Main Branch", "North Branch"]
    },
    {
        title: "The Hitchhiker's Guide to the Galaxy",
        author: "Douglas Adams",
        cover: "./data/book_covers/Hitchhiker.jpg", 
        description: "Earthman Arthur Dent narrowly escapes the destruction of his home planet by hitching a ride on a Vogon spaceship with his friend Ford Prefect, who reveals himself to be an alien researcher for the titular Hitchhiker's Guide to the Galaxy. They embark on a zany interstellar journey aboard the stolen spaceship Heart of Gold, encountering eccentric characters like two-headed galactic president Zaphod Beeblebrox, the depressed robot Marvin, and Trillian, the woman Arthur once tried to pick up at a party. Their adventures lead them to the answer to the ultimate question of life, the universe, and everything, which turns out to be 42, but the question itself remains elusive.", 
        genres: ["Science Fiction", "Humor"],
        availability: ["Main Branch", "South Branch", "East Branch"]
    },
    {
        title: "The Great Gatsby",
        author: "F. Scott Fitzgerald",
        cover: "./data/book_covers/Gatsby.jpg",  
        description: "In the roaring 1920s, Nick Carraway, a Midwesterner who moves to Long Island, becomes fascinated by his wealthy and enigmatic neighbor, Jay Gatsby. Gatsby throws extravagant parties, hoping to reunite with his lost love, Daisy Buchanan, who is married to the brutish Tom Buchanan. Nick gets drawn into their world of luxury, obsession, and ultimately, tragedy, as Gatsby's pursuit of the American Dream leads to devastating consequences.", 
        genres: ["Tragedy"],
        availability: ["Main Branch", "East Branch", "West Branch"]
    },
    {
        title: "Dune",
        author: "Frank herbert",
        cover: "./data/book_covers/Dune.jpg",  
        description: "On the desert planet Arrakis, the sole source of the valuable spice melange, young Paul Atreides and his family become embroiled in a treacherous power struggle after being entrusted with the planet's stewardship. Betrayed and left for dead, Paul finds refuge with the native Fremen, eventually embracing his destiny as their messianic leader, Muad'Dib, to avenge his family and reclaim control of Arrakis.",
        genres: ["Science Fiction"],
        availability: ["Main Branch", "North Branch", "West Branch"]
    },
    {
        title: "Ready Player One",
        author: "Ernest Cline",
        cover: "./data/book_covers/Ready_Player_One.jpg",  
        description: "In a dystopian 2045, teenager Wade Watts escapes the bleak reality of his life by immersing himself in the virtual world of OASIS. When the creator of OASIS dies, he leaves a series of puzzles and challenges within the game, promising his vast fortune and control of OASIS to the winner. Wade joins the global race to find the keys, battling both virtual adversaries and a powerful corporation determined to seize the prize for themselves.",
        genres: ["Science Fiction","Action"],
        availability: ["South Branch", "West Branch"]
    },
    {
        title: "Minecraft Redstone Handbook",
        author: "Mojang AB",
        cover: "./data/book_covers/Redstone_Handbook.jpg",  
        description: "Minecraft: Redstone Handbook is an official guidebook that delves into the intricate world of redstone, a versatile in-game resource used for building complex contraptions and mechanisms. It teaches players how to harness the power of redstone to create automatic doors, intricate circuits, hidden traps, and even simple computers within the Minecraft universe.",
        genres: ["Non-Fiction","Guide"],
        availability: ["Main Branch", "North Branch","South Branch","East Branch","West Branch"]
    },
    {
        title: "Minecraft Beginners Handbook",
        author: "Mojang AB",
        cover: "./data/book_covers/Beginner's_Handbook.jpg",  
        description: "Minecraft: Beginners Guide is an official guidebook offering essential tips and strategies for thriving in the Minecraft world. It covers everything from basic survival skills like gathering resources, building shelters, and crafting tools to advanced techniques for farming, exploring, combatting hostile mobs, and navigating different biomes. The guide aims to help players of all levels master the challenges of survival in the blocky universe of Minecraft.",
        genres: ["Non-Fiction","Guide"],
        availability: ["Main Branch", "North Branch", "West Branch"]
    },
    {
        title: "Minecraft Construction Handbook",
        author: "Mojang AB",
        cover: "./data/book_covers/Construction_Handbook.jpg",  
        description: "Minecraft: Construction Handbook is an official guidebook that provides players with creative inspiration and practical tips for building impressive structures in the Minecraft world. It covers a wide range of construction projects, from simple houses and farms to elaborate castles and underwater cities. The handbook includes detailed instructions, step-by-step diagrams, and valuable advice on choosing materials, planning layouts, and incorporating redstone mechanisms. Whether you're a beginner builder or a seasoned architect, this handbook will help you unleash your creativity and build amazing creations in Minecraft.",
        genres: ["Non-Fiction","Guide"],
        availability: ["Main Branch", "North Branch","South Branch"]
    },
    {
        title: "Minecraft Combat Handbook",
        author: "Mojang AB",
        cover: "./data/book_covers/Combat_Handbook.jpg",  
        description: "Synopsis: Minecraft: Combat Handbook is an official guidebook that equips players with the knowledge and skills needed to survive and thrive in the dangerous world of Minecraft. It covers a wide range of combat-related topics.",
        genres: ["Non-Fiction","Guide"],
        availability: ["South Branch", "West Branch"]
    },
    {
        title: "Thinking Fast Thinking Slow",
        author: "Daniel Kahneman",
        cover: "./data/book_covers/TFTS.jpg",  
        description: "Thinking, Fast and Slow explores the two systems that drive the way we think and make decisions: System 1 is fast, intuitive, and emotional; System 2 is slower, more deliberative, and more logical. Kahneman reveals the biases and flaws in our intuitive thinking, showing how these can lead to irrational choices. He offers practical insights on how to recognize and overcome these biases, leading to better decision-making in our personal and professional lives.",
        genres: ["Non-Fiction","Psychology"],
        availability: ["Main Branch", "West Branch"]
    },
    {
        title: "Surrounded by Idiots",
        author: "Thomas Erikson",
        cover: "./data/book_covers/Idiots.jpg",  
        description: "Surrounded by Idiots introduces a model of four distinct personality types based on colors (Red, Yellow, Green, and Blue), each with different communication styles, motivations, and behaviors. The book provides insights and practical tips on how to identify these types in others and adjust your communication style accordingly to improve interactions in both personal and professional relationships.",
        genres: ["Non-Fiction","Self-Help"],
        availability: ["West Branch", "South Branch"]
    },
    {
        title: "The Subtle Art of Not Giving a Fuck",
        author: "Mark Manson",
        cover: "./data/book_covers/No_Fucks_Given.jpg",  
        description: "The Subtle Art of Not Giving a F*ck challenges traditional self-help advice and encourages readers to embrace their limitations and imperfections. It argues that true happiness comes not from chasing positive experiences, but from choosing what to care about and accepting life's inevitable struggles. Through humorous anecdotes and blunt honesty, Manson offers a refreshing perspective on finding meaning and fulfillment in a world that constantly tells us to strive for more.",
        genres: ["Non-Fiction","Self-Help"],
        availability: ["Main Branch", "North Branch","South Branch" ,"East Branch"]
    },
    {
        title: "Ikigai",
        author: "Hector Garcia and Francesc Miralles",
        cover: "./data/book_covers/Ikigai.jpg",  
        description: "Ikigai explores the Japanese concept of 'ikigai', a term often translated as 'reason for being' or 'reason to get up in the morning'. The book delves into the lifestyle and philosophy of centenarians in Okinawa, Japan, known for their longevity and happiness. It uncovers the secrets to their fulfilling lives, highlighting the importance of finding purpose, staying active, nourishing social connections, and embracing simple joys. Ikigai offers practical tips and insights on how to discover and cultivate your own ikigai to lead a more meaningful and fulfilling life.",

        genres: ["Non-Fiction","Self-Help"],
        availability: ["Main Branch", "West Branch"]
    },
    {
        title: "The Art Of War",
        author: "Sun Tzu",
        cover: "./data/book_covers/AOW.jpg",  
        description: "The Art of War is an ancient Chinese treatise on military strategy and tactics. It emphasizes the importance of knowing oneself and one's enemy, using deception and cunning to gain advantage, and winning wars through careful planning and positioning rather than brute force. Its teachings have been influential in military, business, and personal development contexts for centuries.",
        genres: ["Non-Fiction","Guide","Self-Help"],
        availability: ["Main Branch", "North Branch"]
    },
    {
        title: "The Death Note",
        author: "Shinigami",
        cover: "./data/book_covers/Death_Note.jpg",  
        description: `1. The human whose name is written in this note shall die.
        2. This note will not take effect unless the writer has the person's face in their mind when writing his/her name.
        3. If the cause of death is written within 40 seconds of writing the person's name, it will happen.
        4. After writing the cause of death, details of the death should be written in the next 6 minutes and 40 seconds.
        5. This note shall become the property of the human world, once it touches the ground of (arrives in) the human world.
        6. The owner of the note can recognize the image and voice of the original owner, i.e., a god of death.
        7. The human who uses this note can neither go to Heaven nor Hell.`,
        genres: ["Mystery","Thriller"],
        availability: ["Unavailable"]
    }
];

export default books;
