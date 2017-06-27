from operator import attrgetter
import ArtItem

class ArtThief:
    def __init__(self):
        # shall items be sorted? yes by best value/weight ratio
        self.items = []
        self.found = []

    def setup_items(self, items):
        self.items = items
        self.sort_items_by_value_weight_ratio()

    def find_best_item_for(self, avail_weight):
        if avail_weight <= 0 or avail_weight < self.get_min_weight().weight:
            return
        for item in items:
            if avail_weight >= item.weight:
                self.found.append(item)
                items.remove(item) # only one unique item can be stolen
                avail_weight -= item.weight
                self.find_best_item_for(avail_weight)


    def sort_items_by_value_weight_ratio(self):
        self.items.sort(key=lambda x: x.value/x.weight, reverse=True)
        # for i in self.items:
        #     print(i)

    def get_min_weight(self):
        # items keeps changes while recursive,  get the current min weight
        min_weight = min(items, key=attrgetter('weight'))
        return min_weight

    def print_result(self):
        for i in self.found:
            print(i)


if __name__ == '__main__':
    items = [ArtItem.ArtItem(1, 2, 3),
             ArtItem.ArtItem(2, 3, 4),
             ArtItem.ArtItem(3, 4, 8),
             ArtItem.ArtItem(4, 5, 8),
             ArtItem.ArtItem(5, 9, 10)]

    at = ArtThief()
    at.setup_items(items)
    at.find_best_item_for(20)
    at.print_result()
    # failed,  cannot only based on the best ratio to pick up item