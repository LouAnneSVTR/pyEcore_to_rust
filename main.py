from pyecore.resources import ResourceSet, URI
rset = ResourceSet()
resource = rset.get_resource(URI('character_simulator.ecore'))
mm_root = resource.contents[0]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    resource = rset.get_resource(URI('character_simulator.ecore'))
    mm_root = resource.contents[0]

    from pyecore.utils import DynamicEPackage
    MyMetamodel = DynamicEPackage(mm_root)
    #a_instance = MyMetamodel.

    print(mm_root.eClassifiers[7].eStructuralFeatures)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
