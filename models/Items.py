class Item:

    def __init__(self, item_id, name, type, power, description, durability):
        self.item_id = item_id
        self.name = name
        self.type = type
        self.power = power
        self.description = description
        self.durability = durability

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "name": self.name,
            "type": self.type,
            "power": self.power,
            "description": self.description,
            "durability": self.durability,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            item_id=data.get("item_id"),
            name=data.get("name"),
            type=data.get("type"),
            power=data.get("power"),
            description=data.get("description"),
            durability=data.get("durability"),
        )
