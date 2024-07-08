import unittest

from gilded_rose_2 import *


class TestUpdateQuality(unittest.TestCase):
    def test_sell_in_and_quality_decrease(self):
        """Case to test that 'At the end of each day our system lowers both values [sell_in and quality] for every item'"""
        items = [Item("+5 Dexterity Vest", 10, 20)]
        gildedrose = GildedRose(items)
        gildedrose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(19, items[0].quality)

    def test_quality_degrades_twice_as_fast_after_sell_in_passed(self):
        """Case to test that 'Once the sell by date has passed, Quality degrades twice as fast'"""
        items = [Item("Elixir of the Mongoose", -1, 7)]
        gildedrose = GildedRose(items)
        gildedrose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(5, items[0].quality)

    def test_quality_never_negative(self):
        """Case to test that 'The Quality of an item is never negative'"""
        items = [Item("Elixir of the Mongoose", 5, 0)]
        gildedrose = GildedRose(items)
        gildedrose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_aged_brie_quality_increases(self):
        """Case to test that '"Aged Brie" actually increases in Quality the older it gets'"""
        items = [Item("Aged Brie", 2, 0)]
        gildedrose = GildedRose(items)
        gildedrose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

    def test_quality_never_more_than_50(self):
        """Case to test that 'The Quality of an item is never more than 50'"""
        items = [Item("Aged Brie", 2, 50)]
        gildedrose = GildedRose(items)
        gildedrose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_sell_in_and_quality_dont_decrease(self):
        """Case to test that '"Sulfuras", being a legendary item, never has to be sold or decreases in Quality
        and that 'its Quality is 80 and it never alters'"""
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gildedrose = GildedRose(items)
        gildedrose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_backstage_passes_quality_increases(self):
        """Case to test that '"Backstage passes"...increases in Quality as its SellIn value approaches'"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gildedrose = GildedRose(items)
        gildedrose.update_quality()
        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(21, items[0].quality)

    def test_backstage_passes_quality_increases_by_2_when_sell_in_10_or_less(self):
        """Case to test that '"Backstage passes"...Quality increases by 2 when there are 10 days or less'"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 20)]
        gildedrose = GildedRose(items)
        gildedrose.update_quality()
        self.assertEqual(10, items[0].sell_in)
        self.assertEqual(22, items[0].quality)

    def test_backstage_passes_quality_increases_by_3_when_sell_in_5_or_less(self):
        """Case to test that '"Backstage passes"...Quality increases...by 3 when there are 5 days or less'"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 20)]
        gildedrose = GildedRose(items)
        gildedrose.update_quality()
        self.assertEqual(5, items[0].sell_in)
        self.assertEqual(23, items[0].quality)

    def test_backstage_passes_quality_drops_to_0_after_concert(self):
        """Case to test that '"Backstage passes"...Quality drops to 0 after the concert'"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gildedrose = GildedRose(items)
        gildedrose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_conjured_item_quality_decreases_twice_as_fast_sell_in_positive(self):
        """Case to test that '"Conjured" items degrade in Quality twice as fast as normal items'
        before sell_in has been reached"""
        items = [Item("Conjured Mana Cake", 3, 6)]
        gildedrose = GildedRose(items)
        gildedrose.update_quality()
        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(4, items[0].quality)

    def test_conjured_item_quality_decreases_twice_as_fast_sell_in_negative(self):
        """Case to test that '"Conjured" items degrade in Quality twice as fast as normal items'
        after sell_in has been reached"""
        items = [Item("Conjured Mana Cake", 0, 6)]
        gildedrose = GildedRose(items)
        gildedrose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(2, items[0].quality)


if __name__ == '__main__':
    unittest.main()
