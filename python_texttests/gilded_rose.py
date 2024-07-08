class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1

            if item.name != "Sulfuras, Hand of Ragnaros" and item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name !="Aged Brie":
                if (item.sell_in >= 0 and item.quality > 0) or (item.sell_in < 0 and item.quality == 1):
                    item.quality -= 1
                elif item.sell_in < 0 and item.quality > 1:
                    item.quality -= 2

            if item.name == "Aged Brie" and item.quality < 50:
                if item.sell_in >= 0:
                    item.quality += 1
                elif item.sell_in < 0:
                    item.quality += 2

            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in >= 10 and item.quality < 50:
                    item.quality += 1
                elif 5 <= item.sell_in < 10:
                    if item.quality <= 48:
                        item.quality += 2
                    elif item.quality == 49:
                        item.quality += 1
                elif 0 <= item.sell_in < 5:
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
