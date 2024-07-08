class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1

            if item.name != "Sulfuras, Hand of Ragnaros" and item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name !="Aged Brie" and "Conjured" not in item.name:
                if (item.sell_in >= 0 and item.quality > 0) or (item.sell_in < 0 and item.quality == 1):
                    item.quality -= 1
                elif item.sell_in < 0 and item.quality > 1:
                    item.quality -= 2

            if "Conjured" in item.name:
                if item.sell_in >= 0 and item.quality >= 2:
                    item.quality -= 2
                elif item.sell_in < 0 and item.quality >= 4:
                    item.quality -= 4
                elif item.sell_in < 0 and item.quality < 4:
                    item.quality = 0

            if item.name == "Aged Brie" and item.quality < 50:
                item.quality += 1
                # seeing as there is no statement in the requirements about what happens to Aged Brie after sell-in reaches 0, I have chosen to keep it increasing by 1

            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                """ the requirements state that '"Backstage passes", like aged brie, increases in Quality as its SellIn value approaches'
                but do not state by how much until sell_in is 10 days or less, therefore I have made the assumption that
                when sell_in is greater than 10 days, quality increases by 1 each day"""
                if item.sell_in > 10 and item.quality < 50:
                    item.quality += 1
                elif 5 < item.sell_in <= 10:
                    if item.quality <= 48:
                        item.quality += 2
                    elif item.quality == 49:
                        item.quality += 1
                elif 0 <= item.sell_in <= 5:
                    if item.quality <= 47:
                        item.quality += 3
                    elif 50 > item.quality > 47:
                        item.quality = 50
                elif item.sell_in < 0:
                    item.quality = 0


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
