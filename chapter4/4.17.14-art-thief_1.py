from operator import attrgetter
from ArtItem import ArtItem





class ArtThief:
    def __init__(self):
        # shall items be sorted? yes by best value/weight ratio
        self.items = []
        self.found = []

    def setup_items(self, items):
        self.items = items

    def find_best_item_for(self, avail_weight):

        remainingitems = items
        stolenitems = []
        remainingweight = avail_weight
        min_weight = self.get_min_weight(remainingitems)

        if remainingitems is None or min_weight > remainingweight:
            return[]
        else: # handle divided-problem "dynamic"
            result = self.find_best_in_sub(remainingitems, stolenitems, remainingweight)

            return result



    def get_min_weight(self, input_items=[]):
        if not input_items:
            return 0
        min_weight = min(input_items, key=attrgetter('weight'))
        return min_weight.weight

    def get_total_weight(self, input_items):
        total_weight = sum(item.weight for item in input_items)
        return total_weight

    def get_total_value(self, input_items):
        total_value = sum(item.value for item in input_items)
        return total_value

    def find_best_in_sub(self, remainingitems=[], stolenitems=[], remainingweight=0):

        if not remainingitems:
            return stolenitems
        else:  # handle divided-problem "dynamic"
            for item in remainingitems:
                stolenitemss_cp = stolenitems[:]
                remainingitems_cp = remainingitems[:]

                if item.weight < remainingweight:
                    stolenitemss_cp.append(item)
                    remainingitems_cp.remove(item)  # cannot do this , object pointer
                    sub_remainingweight = remainingweight - item.weight
                    subs_tolen = self.find_best_in_sub(remainingitems_cp, stolenitemss_cp, sub_remainingweight)
                    sub_total_value = self.get_total_value(subs_tolen)
                    bestvalue = self.get_total_value(self.found)
                    if sub_total_value > bestvalue:
                        self.found = stolenitemss_cp
                        print("bestvalue, %s, sub total value %s"%(bestvalue,sub_total_value))
                        print(" ".join([str(word) for word in self.found]))
            return stolenitems

    def print_result(self, result):
        for i in result:
            print(i)

items = [ArtItem(1, 2, 3),
         ArtItem(2, 3, 4),
         ArtItem(3, 4, 8),
         ArtItem(4, 5, 8),
         ArtItem(5, 9, 10)]

#items = [ArtItem(11, 5, 8), ArtItem(12, 16, 18)]

at = ArtThief()
at.setup_items(items)
result = at.find_best_item_for(20)
print("\nresult:")
print("\n".join([str(word) for word in at.found]))
#at.print_result(result)
# failed,  cannot only based on the best ratio to pick up item

