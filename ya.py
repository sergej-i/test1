
class SumFromSrcs:
    ''' класс для работы с источниками для суммирования  '''
    def __init__(self):
        self.rc = {}
        self.srcs = []

    def src_add(self, src):
        self.srcs.append(src)

    def srcs_clear(self):
        self.srcs.clear()

    def rc_clear(self):
        self.rc.clear()

    def reset(self):
        self.srcs_clear()
        self.rc.clear()

    def process_item(self, i):
        ''' обработка элемента '''
        item = i.popitem()
        if item[0] in self.rc.keys():
            self.rc[item[0]] += item[1]
        else:
            self.rc[item[0]] = item[1]

    def process_srcs(self):
        ''' находим сумму по источникам '''
        self.rc_clear()
        for src in self.srcs:
            for i in src:
                #print(i)
                self.process_item(i)

    def get_rc(self):
        return self.rc
        
    def get_srcs(self):
        return self.srcs
        


if __name__ == "__main__":
    from ya_lib import gen_name_by_i, gen_val
    from random import randint
    from pprint import pprint

    max_items_count = 10 # ограничим максимальное число генерируемых словарей

    # допустим, что в источниках не известно сколько элементов
    src_a = ({gen_name_by_i(i): gen_val()} for i in range(randint(1, max_items_count)))
    src_b = ({gen_name_by_i(i): gen_val()} for i in range(randint(1, max_items_count)))
    src_c = ({gen_name_by_i(i): gen_val()} for i in range(randint(1, max_items_count)))

    sumFromSrcs = SumFromSrcs()
    sumFromSrcs.src_add(src_a)
    sumFromSrcs.src_add(src_b)
    sumFromSrcs.src_add(src_c)
    sumFromSrcs.process_srcs()

    pprint(sumFromSrcs.get_rc())


