# Save The Village - Village Rescue Game

## 📖 Project Description

**Save The Village** is a console-based RPG game that involves the process of rescuing 7 different villages that have been captured by enemies in sequence. This project is an educational game application developed using data structures and algorithms.

### 🎯 Game Story
As a game hero, you need to rescue 7 villages that have been captured by enemies in sequence. Each village contains various items that will be useful to your character. However, your bag capacity is limited and you will need to make strategic decisions.

## 🚀 Features

### ✅ Core Features
- **7 Different Villages**: At least 3 different items in each village
- **Inventory System**: Bag management with 10 item capacity
- **Stack Operations**: Item addition/removal with `push()` and `pop()`
- **Queue System**: Sequential management of villages to be rescued
- **BST Search System**: Fast search and sorting of items
- **Rescue Requirements**: Special requirements for the last 3 villages

### 🎮 Game Mechanics
- **Bag Management**: Capacity control and warning system
- **Item Usage**: Item consumption with `useItem()` function
- **Progress Tracking**: Tracking which villages have been rescued
- **Search System**: "Do I have item X in my bag?" queries

## 🛠️ Technologies

- **Python 3.11**: Main programming language
- **MongoDB**: Database management
- **Docker & Docker Compose**: Containerization
- **PyMongo**: MongoDB Python driver

## 🚀 Installation and Running

### Running with Docker (Recommended)

1. **Clone the project:**
```bash
git clone https://github.com/username/save-the-village.git
cd save-the-village
```

2. **Set your MongoDB URI:**
```bash
# Mail me for .env file
echo "MONGO_URI=your_mongodb_connection_string" > .env
```


### Manual Installation

1. **Install requirements:**
```bash
pip install -r requirements.txt
```

2. **Set MongoDB connection:**
```python
# Update your URI in services/MongoDB.py file
```

3. **Start the game:**
```bash
python main.py
```

## 🎮 Game Menu

```
==================================================
        VILLAGE RESCUE GAME
==================================================
1. List Villages
2. View Bag  
3. Rescue Village
4. Search Items (BST)
5. Show Game Status
6. Exit
--------------------------------------------------
```

## 📁 Project Structure

```
SaveTheVillage/
├── main.py                 # Main game file
├── models/
│   ├── Items.py           # Item model class
│   ├── Village.py         # Village model class
│   └── Player.py          # Player model class
├── services/
│   └── MongoDB.py         # Database connection
├── utils/
│   ├── BST.py            # Binary Search Tree
│   ├── Stack.py          # Stack implementation
│   └── Queue.py          # Queue implementation
├── data/
│   └── initial_data.json # Initial data
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── compose.yaml          # Docker Compose settings
└── README.md             # This file
```

## 🗄️ Database Structure

### Collections:
- **villages**: Village information and items
- **players**: Player status and inventory
- **items**: Item master data
- **game_progress**: Game progress status

## 🤝 Contributing

1. Fork the project
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project was developed for educational purposes.

## 👥 Development Team

- **Project Leader**: [Kaan Civelek]
- **Backend Developer**: [Nebi Çiftkaldıran & Kaan Civelek]  
- **Database Designer**: [Kaan Civelek]

## 📞 Contact

For questions about the project: [businesskaancivelek@gmail.com]

---

⭐ **Don't forget to star this project if you liked it!** ⭐
