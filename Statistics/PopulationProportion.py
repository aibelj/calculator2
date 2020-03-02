from RandomNumGen.ItemReturnType import ItemReturnType

class PopulationProportion():
    @staticmethod
    def proportion(data, lstLen, seed):
        subData = ItemReturnType.aList_seed(data, lstLen, seed)
        proportion = len(subData)/len(data)
        return proportion