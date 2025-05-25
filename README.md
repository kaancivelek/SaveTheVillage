# �� Save The Village - Village Rescue Game

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

## 📊 Data Structures Usage

### 1. **Array/Linked List** - Villages (10 points)
```python
# Representation structure of 7 villages
villages = [
    {"name": "Forest Village", "items": [...], "is_rescued": False},
    {"name": "Mountain Village", "items": [...], "is_rescued": False},
    # ...
]
```

### 2. **Linked List** - Bag Management (15 points)
```python
class Inventory:
    def __init__(self, capacity=10):
        self.items = []
        self.capacity = capacity
        self.current_count = 0
```

### 3. **Stack** - Item Operations (15 points)
```python
def push(item):    # Add item
def pop():         # Remove last item
```

### 4. **Queue** - Village Rescue Order (15 points)
```python
village_queue = [3, 4, 5, 6, 7]  # Villages to be rescued
```

### 5. **Binary Search Tree (BST)** - Search/Sorting (15 points)
```python
# Store items in BST by power points
# Fast search: "Do I have a sword in my bag?"
```

### 6. **Item Usage** - Game Mechanics (20 points)
```python
def useItem(itemName):
    # Item consumption and capacity update
    # Check rescue requirements
```

## 🎯 Game Requirements

### Rescue Requirements (Last 3 Villages)
- **5th Village (Ice Village)**: Axe + Potion required
- **6th Village (Volcano Village)**: Shield + Fire Resistance Potion required  
- **7th Village (Dark Castle)**: Legendary Weapon + Magic Scroll + Crown required

### In-Game Queries
1. ❓ "Which villages need to be rescued?"
2. ❓ "Which village am I in now and which ones have I rescued?"
3. ❓ "What inventories are in which village?"

## 🚀 Installation and Running

### Running with Docker (Recommended)

1. **Clone the project:**
```bash
git clone https://github.com/username/save-the-village.git
cd save-the-village
```

2. **Set your MongoDB URI:**
```bash
# Create .env file
echo "MONGO_URI=your_mongodb_connection_string" > .env
```

3. **Start with Docker:**
```bash
docker-compose up --build
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

## 🏆 Score Distribution

| Feature | Points |
|---------|--------|
| Village Representation Structure | 10 |
| Inventory Management | 15 |
| Stack Operations | 15 |
| Queue Usage | 15 |
| BST Search/Sorting | 15 |
| Item Usage | 20 |
| Console Interface | 10 |
| **Total** | **100** |
| AVL Tree (Bonus) | +10 |

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
