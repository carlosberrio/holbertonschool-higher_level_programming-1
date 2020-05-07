#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def se_rep_item(item):
        return (item if item != search else replace)
    return list(map(se_rep_item, my_list))
